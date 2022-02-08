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
                    images.append(cv2.imread(list[0]))
                    labels.append(list[1])
    print('\n Successfully read training set...')

# Initialize application
print('\n### Face recognition: detecting known users ###')

# Managing training set
decision = input('\n Do you want to modify the training set? (y/n): ')
while decision != 'y' and decision != 'n':  
    decision = input(' Type a valid option. Do you want to modify the training set? (y/n): ')
if decision == 'y':
    manage_training_set.manageTrainingSet()

manage_training_set.generateCSVFile()

images, labels = [], []
readCSVFiles(images, labels)

(images, labels) = [numpy.array(lis, dtype="object") for lis in [images, labels]]

# Training EigenFaces model
# model = cv2.face.LBPHFaceRecognizer_create()
# model.train(images,labels)