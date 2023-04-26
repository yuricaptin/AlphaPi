# AlphaPi
This repository contains the files for the app that implements the model.

This program has a hard time recognizing faces with a darker skin tone. Especially with the haar_cascade classifier. With my face there are false positives with an example being under here.
People with lighter skin tones wont have a problem with their face being detected by the haar_cascadeclassifier then getting their facial image through the model. 


![face_rec](https://user-images.githubusercontent.com/61609037/234671703-d95a4b6a-37a1-481f-ba3e-8d69b3a64120.jpg)


The .tflite model does not work currently with this build. Reason being is the different input tensors that were created due to the way the model is structured when being converted to .tflite format. The tensorflow model can be run on the Pi the matter being that the Pi that can run it is only the Raspberry Pi Model 4B with RAM being 4 or 8GB. 
Sadly the Raspberry Pi Model 3B doesn't have the capability of running the model. Even when the model is being run with the .tflite model without the input image being run through the verify function, the delay between actions on camera in real world is about 5 seconds. With major lag being detected throughout the program being run.

The specific error that will happen is with the `ValueError: cannot set tensor: Dimension mismatch. Got 200 instead of 100 for dimension 1 of input 0`. This line is alluding to the input details tensor shape of `[1, 100, 100, 3]`. Through different techniques of concatenating the input_shape as well as the input_details, more issues started to pop up. The .tflite runtime is especially difficult for custom models. It is recommended when using .tflite to have a relatively simple custom model or use one of the pre-trained models being offered by Tensorflow.

## Siamese Neural Network and Training for the Smart Home Security with Facial Recognition using Raspberry Pi

This github repo is for the implementation of the model from the [RealProjectPi-Files](https://github.com/yuricaptin/RealProjectPi-Files) directory.
When the face is detected the program sends a notification with details including the detection of a face as well as if the face was recognized or not.

### Table of Contents 

  - [**Usage**](#usage)
  - [**Contributing**](#contributing)
  - [**License**](#license)
  - [**Example**](#example)

### Usage

This section provides instructions on how to use the code in this repository:

1. Clone the repository:
2. Change the Sender email to one that you have created.
  - The SMTP api allows the program to control the email to send emails.
  - Make sure to turn on 2-step-verification in the settings of your gmail.
  
  ![2stepverificationprocess](https://user-images.githubusercontent.com/61609037/234039161-e8f76f87-9603-4546-8690-43a5c05c23a8.png)

  - Scroll down to App passwords
  
  ![2stepapppassword](https://user-images.githubusercontent.com/61609037/234039361-d554c243-1bbb-43cd-8323-9ea0efe53c22.PNG)
  
  - Then create a new app password. That app password will be the key you want to use for the `sender_app_password` in `AlphaPi.py`.
  
  ![2stepapppasswordcreation](https://user-images.githubusercontent.com/61609037/234039754-bb207225-dc3d-4f67-b2a6-0b4fb3d49c6d.PNG)

3. For the recipient email change it to the one you want the notifications to be sent to.
4. In the `app_data` folder, add images of people you want to be verified into the `verify_image` folder.
5. Make sure that the `haarcascade_frontalface_default.xml` file is in the folder.
6. Also confirm that the new model you have from siamesemodel is converted into `.tflite` format.
7. Run the `AlphaPi.py` script.

### Contributing

This section describes how to contribut to the project. 

Because of this project being a Senior Capstone Project, please send me an email if you would like to continue working on this.

ly01256@georgiasouthern.edu


### License

This section describes the license for the code in this repository. (Replace `LICENSE.md` with the appropriate license file for your project.)

This project is licensed under the terms of the [MIT license](LICENSE.md).


### Example

Below are two screenshots of emails sent from the system.


![Example1](https://user-images.githubusercontent.com/61609037/234041607-2e32cd15-ee30-4c95-ad5b-b6fed3638fa6.PNG)


![Example2](https://user-images.githubusercontent.com/61609037/234041641-fda87e18-06d7-4655-8c28-ea6700c4c387.PNG)
