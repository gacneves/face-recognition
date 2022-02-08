import manage_training_set

print('\n### Face recognition: detecting known users ###')

# Managing training set
decision = input('\n Do you want to modify the training set? (y/n): ')
while decision != 'y' and decision != 'n':  
    decision = input(' Type a valid option. Do you want to modify the training set? (y/n): ')
if decision == 'y':
    manage_training_set.manageTrainingSet()