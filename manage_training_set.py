import os
import cv2
import csv

TRAINING_SET_DIR = './Training Set'
USER_CSV_DIR = './User CSV'
SEPARATOR = ';'
CASCADE_CLASSIFIER_DIR = './Haar Cascade Classifier'
OUTPUT_WIDTH = 100
OUTPUT_HEIGHT = 100

def checkTrainingSetDir():
    print('\n Checking Training Set folder existence...')
    if os.path.isdir(TRAINING_SET_DIR):
        print(' Found Training Set folder')
        list = os.listdir(TRAINING_SET_DIR)
        if list:
            if len(list) == 1:
                print(' There is already 1 person in the training set')
                print(' User in the training set:', list[0], end='')
            else:
                print(' There are already', len(list), 'people in the training set')
                print(' Users in the training set:', list[0], end='')
                for user in list[1:]:
                    print(',', user, end='')
        else:
            print(' There is no users in the training set')
    else:
        print(' Folder not found. Making directory...')
        os.mkdir(TRAINING_SET_DIR)
        print(' Created Training Set folder')

def takeUserPhotos(user_path):
    # Try opening camera
    print('\n Checking camera existence...')
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not camera.isOpened():
        print('\n Error: Could not open the camera')
        exit()
    print(' Successfully opened the camera')

    # Prepare pretrained classifier
    cascade_face_file = os.path.join(CASCADE_CLASSIFIER_DIR, 'haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(cascade_face_file)

    # Count before the photos caption
    print('\n A ammount of 100 photos will be taken in x seconds. Stay steady')
    count = 5
    while count != 0:
        print(' Prepare to take photos in %d...' % count)
        cv2.waitKey(1000)
        count -= 1

    # Photo caption
    while count < 30:
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
            cv2.imwrite('%s/%s.jpg' % (user_path, count), face_image)
        cv2.imshow('Taking photos...', frame)
        cv2.waitKey(250)
        count += 1
    print(' All photos taken. Destroying window')
    camera.release()
    cv2.destroyAllWindows()

def generateCSVFile(username, user_path):
    print('\n Creating .csv file for the new user added')
    
    print(' Checking User CSV folder existence...')
    if not os.path.isdir(USER_CSV_DIR):
        print(' Folder not found. Creating the directory')
        os.mkdir(USER_CSV_DIR)
    else:
        print(' Found User CSV folder')

    user_file = username + '.csv'
    user_csv_path = os.path.join(USER_CSV_DIR, user_file)

    f = open(user_csv_path, 'w')

    for filename in os.listdir(user_path):
        row = user_path + filename + SEPARATOR + username
        f.write(row + '\n')

def manageTrainingSet():
    print('\n ### Managing the training set ### ')

    checkTrainingSetDir()

    name = input('\n\n Type the name of the person that you want to add to the training set of the classifier (0 to skip): ')
    while name != '0':
        user_path = os.path.join(TRAINING_SET_DIR, name)
        if os.path.isdir(user_path):
            print('\n Person already in the training set')
            decision = input(' Do you want to retake the photos (y/n): ')
            while decision != 'y' and decision != 'n':  
                decision = input(' Type a valid option. Do you want to retake the photos (y/n): ')
            if decision == 'y':
                takeUserPhotos(user_path)
                generateCSVFile(name, user_path)
        else:
            print('\n User does not exist in the database. Making directory...')
            os.mkdir(user_path)
            print(' Created ', name, ' folder in the training set\n')
            takeUserPhotos(user_path)
            generateCSVFile(name, user_path)
            
        name = input('\n Type the name of the person that you want to add to the training set of the classifier (0 to finish): ')