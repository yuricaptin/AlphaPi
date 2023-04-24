import tensorflow as tf
import cv2
import imghdr
import numpy as np
import smtplib
import os
from email.message import EmailMessage
import configparser
import time
import keras

from keras.layers import Layer
from keras.models import load_model




camera = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

detection_threshold = 0.7
verification_threshold = 0.5

sender_email = ''
sender_app_password = ''

time_between_emails = 60
time_since_last_email = time.time() - time_between_emails

path = ('app_data','input_image')

class L1Dist(Layer):
    def __init__(self, **kwargs):
        super().__init__()

    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)

def preprocess(file_path):
        # Read in image from file path
        byte_img = tf.io.read_file(file_path)
        # Load in the image 
        img = tf.io.decode_jpeg(byte_img)
        
        # Preprocessing steps - resizing the image to be 100x100x3
        img = tf.image.resize(img, (100,100))
        # Scale image to be between 0 and 1 
        img = img / 255.0
        
        # Return image
        return img

model = tf.keras.models.load_model('siamesemodelv2.h5', custom_objects = {'L1Dist': L1Dist, 'BinaryCrossentropy':tf.losses.BinaryCrossentropy})

def verify(model, detection_threshold, verification_threshold):
    # Build results array
    results = []
    for image in os.listdir(os.path.join('app_data', 'verify_image')):
        input_img = preprocess(os.path.join('app_data', 'input_image', 'face_rec.jpg'))
        validation_img = preprocess(os.path.join('app_data', 'verify_image', image))
        
        # Make Predictions 
        result = model.predict(list(np.expand_dims([input_img, validation_img], axis=1)))
        results.append(result)
    
    # Detection Threshold: Metric above which a prediciton is considered positive 
    detection = np.sum(np.array(results) > detection_threshold)
    
    # Verification Threshold: Proportion of positive predictions / total positive samples 
    verification = detection / len(os.listdir(os.path.join('app_data', 'verify_image'))) 
    verified = verification > verification_threshold
    
    return results, verified



while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=7, minSize=(35, 35))

    if len(faces) == 1 and time.time() - time_since_last_email > time_between_emails:
        time_since_last_email = time.time()
        msg = EmailMessage()
        msg['Subject'] = 'Face detected'
        msg['From'] = sender_email
        msg['To'] = ''
        msg.set_content('A face was detected on the camera')

        with open('output.jpg', 'wb') as f:
            cv2.imwrite('output.jpg', frame)
            file_type = imghdr.what(f.name)
            file_name = f.name

            with open('output.jpg', 'rb') as f:
                file_data = f.read()

        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.set_debuglevel(1)
            smtp.login(sender_email, sender_app_password)
            smtp.send_message(msg)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            face_rec = frame[y:y + h, x:x + w]
            with open('face_rec.jpg', 'wb') as g:
                cv2.imwrite(os.path.join('app_data', 'input_image', 'face_rec.jpg'),face_rec)
                file_type1 = imghdr.what(g.name)
                file_name1 = g.name
                
                with open('face_rec.jpg', 'rb') as g:
                    file_data1 = g.read()
            
            results, verified = verify(model, detection_threshold, verification_threshold)
            print(verified)
            if verified == True:
                msg1 = EmailMessage()
                msg1['Subject'] = 'Face recognized'
                msg1['From'] = sender_email
                msg1['To'] = ''
                msg1.set_content('This user is verified and allowed to enter')
                print(1+1)
                
            else:
                msg1 = EmailMessage()
                msg1['Subject'] = 'Face denied'
                msg1['From'] = sender_email
                msg1['To'] = ''
                msg1.set_content('This user is unrecognized, their access is denied')
                print(2+2)
                
            #msg1.add_attachment(file_data1, maintype='image', subtype = file_type1, filename = file_name1)
                    
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.set_debuglevel(1)
                smtp.login(sender_email, sender_app_password)
                smtp.send_message(msg1)
                    

    cv2.imshow('Video Feed', frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

