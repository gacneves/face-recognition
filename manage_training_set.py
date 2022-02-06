import os, cv2

TRAINING_SET_DIR = './Training Set'

def manageTrainingSet():
    print('\n ### Managing the training set ### ')

    print('\n Checking Training Set folder existence...')
    if os.path.isdir(TRAINING_SET_DIR):
        print(' Found Training Set folder')
        list = os.listdir(TRAINING_SET_DIR)
        if len(list) == 1:
            print(' There is already 1 person in the training set')
            print(' User in the training set:', list[0])
        else:
            print(' There are already', len(list), 'people in the training set')
            print(' Users in the training set:', list[0], end='')
            for user in list[1:]:
                print(',', user)
    else:
        print(' Folder not found. Making directory...')
        os.mkdir(TRAINING_SET_DIR)
        print(' Created Training Set folder')

    name = input('\n Type the name of the person that you want to add to the training set of the classifier (0 to skip): ')
    while name != '0':
        user_path = TRAINING_SET_DIR + '/' + name
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
            print(' Take 100 photos')

        name = input('\n Type the name of the person that you want to add to the training set of the classifier (0 to finish): ')