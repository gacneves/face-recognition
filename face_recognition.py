import csv
import os
import cv2, numpy

import manage_training_set

def readCSVFiles(images, labels, user_name):
    print('\n Reading training set...')
    for (_, _, files) in os.walk(manage_training_set.USER_CSV_DIR):
        for file in files:
            print(' Reading %s...' % file)
            user_name.append(file.split(sep='.')[0])
            with open(os.path.join(manage_training_set.USER_CSV_DIR, file), newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    list = row[0].split(sep=';')
                    images.append(cv2.imread(list[0], 0))
                    labels.append(int(list[1]))
    print(' Successfully read training set...')

# Initialize application
print('\n### Face recognition: detecting known users ###')

# Managing training set
decision = input('\n Do you want to modify the training set? (y/n): ')
while decision != 'y' and decision != 'n':  
    decision = input(' Type a valid option. Do you want to modify the training set? (y/n): ')
if decision == 'y':
    manage_training_set.manageTrainingSet()

# Generate csv files for the training set users
manage_training_set.generateCSVFile()

images, labels, user_name = [], [], []
readCSVFiles(images, labels, user_name)

if len(user_name) == 1:
    print(' \nTraining set must have at least 2 users. Exitting application')
    exit()

# Converting lists to numpy.arrays
(images, labels) = [numpy.array(lis) for lis in [images, labels]]

# Training FisherFace model
print('\n Creating model to be trained...')
model = cv2.face.FisherFaceRecognizer_create()
print(' Training model with %s users...' % len(user_name))
model.train(images,labels)
print(' Successfully trained model')
model.setThreshold(1000)

# Open Haar cascade classifier for identifying face
cascade_face_file = os.path.join(manage_training_set.CASCADE_CLASSIFIER_DIR, 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cascade_face_file)

# Open camera
print('\n Trying to open camera')
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not camera.isOpened():
    print('\n Error: Could not open the camera')
    exit()
print(' Successfully opened the camera')

print('\n Detect faces and predict users (Ctrl+C to stop)')
while True:
    # Take camera frame
    _, frame = camera.read()

    # Convert RGB color channels to gray
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect face in the frame
    faces = face_cascade.detectMultiScale(gray_frame)
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), 2)
        face_image = gray_frame[y:y+h, x:x+w]
        face_image = cv2.resize(face_image, (manage_training_set.OUTPUT_WIDTH, manage_training_set.OUTPUT_HEIGHT))

        # Try recognizing the face
        prediction = model.predict(face_image)
        text_start_point = (x - 10, y -10)
        if(prediction[0] >= 0):
            cv2.putText(frame, 'User: ' + user_name[prediction[0]], text_start_point, cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0))
        else:
            cv2.putText(frame, 'User: Unknown', text_start_point, cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0))
    cv2.imshow('Face Recognition...', frame)
    cv2.waitKey(250)