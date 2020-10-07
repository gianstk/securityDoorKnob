# securityDoorKnob
A personal project for a cool doorknob inside your room by having a facial recognition built into the doorknob. 

## What is this? It is a cool doorknob
Who needs a key? while we all have a unique face. This is my small experiment to build a housing security system. There are several security notes i wrote on this [blog (tumblr)](https://sectrakul.tumblr.com/) including the progress of making this project and other security related blogs.
- The project is implemented and tested on Raspberry Pi and Arduino UNO with camera connecting with a electronic solenoid lock. 
  - Raspbian on Raspberry pi
  - Pyfirmata to control digital pins on Arduino board
- **LBPH algorithm** (Local Binary Patterns Histogram) is implemented using *openCV* library to generate a **haar cascade classifier**, which is mainly for recognizting human face. This is a simple algorithm that provide surprisingly accurate result that works even in the night time (dark environment).

## Training classifier
- The project allows user to generate training data set for training a new classifier by running a *create_dataset.py* script. The script turns the camera and keeps taking a photo at fixed frequencies. Convert the photo into grey scale and write down into the project directory. 
- The classifier is created by executing the *train_model.py* script, resulting in a classifier file.
