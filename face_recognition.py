import manage_training_set

print('\n### Face recognition: detecting known users ###')

manage_training_set.manageTrainingSet()

manage_training_set.generateCSVFile('Gabriel', 'Training Set/Gabriel/')

# Fazer detecção com comparação

