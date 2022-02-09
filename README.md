# Face recognition for information security using Python OpenCV

Recognizing faces from a dataset made by the user with the project members already on it training a FisherFace model. The application identify if the person is on the training set or is unknown.

The application requires Python 3.

The OpenCV can be installed using the following command:

```
pip install opencv-contrib-python
```

Make sure the contrib module is installed, or the FisherFace model won't work.

To run the application use:

```
python3 face_recognition.py
```

When it starting, the face recognizer will ask if you want to manage the training set, you can add other users or retake the photos from a person already in the database. In this part just type the name of the user, then if it already exists, it will ask if you want to retake the samples. After taking the photos, typing 0 will finish the managment and take you back to the main program.

In the face recognition module, just wait for the model to be trained, reading the csv files that will be created containing the photos of the database. After that it will starting classifying the person in front of the camera.

Note: if you have more than one camera in your computer, consider changing the index in the VideoCamera function.

Sources: https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html
