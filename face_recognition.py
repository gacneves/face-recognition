import os

TRAINING_SET_DIR = './Training Set'

print('Checking Training Set folder existence...')
if(os.path.isdir(TRAINING_SET_DIR)):
    print('Found Training Set folder\n')
else:
    print('Folder not found. Creating directory...')
    os.mkdir(TRAINING_SET_DIR)
    print('Created Training Set folder')

name = input('Type the name of the person to be used for training the classifier (0 to finish): ')
while name != '0':
    print(name)
    name = input('Type the name of the person to be used for training the classifier (0 to finish): ')