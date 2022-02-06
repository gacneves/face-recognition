import os
import cv2

TRAINING_SET_DIR = './Training Set'

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

def manageTrainingSet():
    print('\n ### Managing the training set ### ')

    checkTrainingSetDir()

    name = input('\n\n Type the name of the person that you want to add to the training set of the classifier (0 to skip): ')
    while name != '0':
        user_path = os.path.join(TRAINING_SET_DIR, name)
        if os.path.isdir(user_path):
            print('\n Person already in the training set')
            decision = input(' Do you want to retake frames (y/n): ')
            while decision != 'y' and decision != 'n':  
                decision = input(' Type a valid option. Do you want to retake frames (y/n): ')
            take_photos = True if decision == 'y' else False if decision == 'n' else 0
        else:
            print('\n User does not exist in the database. Making directory...')
            os.mkdir(user_path)
            print(' Created ', name, ' folder in the training set\n')
            take_photos = True

        if take_photos:
            camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            cv2.waitKey(500)
            if not camera.isOpened():
                print(' \nError: Could not open the camera')
                exit()
            count = 0
            while count < 30:
                # Take camera frame
                _, frame = camera.read()

                # Convert RGB color channels to gray
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                cv2.imwrite('%s/%s.bmp' % (user_path, count), gray_frame)
                cv2.imshow('Taking photos...', frame)
                cv2.waitKey(250)
                count += 1
            camera.release()
            cv2.destroyAllWindows()

        name = input('\n Type the name of the person that you want to add to the training set of the classifier (0 to finish): ')