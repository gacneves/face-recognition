import os

TRAINING_SET_DIR = './Training Set'

print('Checking Training Set folder existence...')
if os.path.isdir(TRAINING_SET_DIR):
    print('Found Training Set folder\n')
else:
    print('Folder not found. Making directory...')
    os.mkdir(TRAINING_SET_DIR)
    print('Created Training Set folder\n')

name = input('Type the name of the person to be used for training the classifier (0 to skip): ')
while name != '0':
    user_path = TRAINING_SET_DIR + '/' + name
    if os.path.isdir(user_path):
        print('\nPerson already in the training set')
    else:
        print('\nUser does not exist in the database. Making directory...')
        os.mkdir(user_path)
        print('Created ' + name + ' folder in the training set\n')
    name = input('Type the name of the person to be used for training the classifier (0 to finish): ')