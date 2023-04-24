# RealProjectPi-Files
This repository contains the files necessary for the creation and training of the model.

## Siamese Neural Network and Training for the Smart Home Security with Facial Recognition using Raspberry Pi

This github repo is for the implementation of the model from the [RealProjectPi-Files](https://github.com/yuricaptin/RealProjectPi-Files) directory.
When the face is detected the program sends 

### Table of Contents 

  - [**Usage**](#usage)
  - [**Contributing**](#contributing)
  - [**License**](#license)

### Usage

This section provides instructions on how to use the code in this repository:

1. Clone the repository:
2. Change the Sender email to one that you have created.
  - The SMTP api allows the program to control the email to send emails.
  - Make sure to turn on 2-step-verification in the settings of your gmail.
  
  
  - Scroll down to app
2. In the `app_data` folder, add images of people you want to be verified into the `verify_image` folder.
3. Make sure that the `haarcascade_frontalface_default.xml` file is in the folder.
4. Also confirm that the new model you have from siamesemodel is converted into `.tflite` format.
4. Run the `AlphaPi.py` script.

### Contributing

This section describes how to contribut to the project. 

Because of this project being a Senior Capstone Project, please send me an email if you would like to continue working on this.

ly01256@georgiasouthern.edu


### License

This section describes the license for the code in this repository. (Replace `LICENSE.md` with the appropriate license file for your project.)

This project is licensed under the terms of the [MIT license](LICENSE.md).
