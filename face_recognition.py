import csv
import os
import cv2, numpy

import manage_training_set

def readCSVFiles(images, labels):
    print('\n Reading training set...')
    for (_, _, files) in os.walk(manage_training_set.USER_CSV_DIR):
        for file in files:
            print(' Reading %s...' % file)
            with open(os.path.join(manage_training_set.USER_CSV_DIR, file), newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    list = row[0].split(sep=';')
                    images.append(cv2.imread(list[0], 0))
                    labels.append(int(list[1]))
    print('\n Successfully read training set...')

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

images, labels = [], []
readCSVFiles(images, labels)

# Converting lists to numpy.arrays
(images, labels) = [numpy.array(lis) for lis in [images, labels]]

# Training FisherFace model
model = cv2.face.FisherFaceRecognizer_create()
model.train(images,labels)
model.setThreshold(1000)

# Open Haar cascade classifier for identifying face
cascade_face_file = os.path.join(manage_training_set.CASCADE_CLASSIFIER_DIR, 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cascade_face_file)

# Open camera
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not camera.isOpened():
    print('\n Error: Could not open the camera')
    exit()
print(' Successfully opened the camera')

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
        
