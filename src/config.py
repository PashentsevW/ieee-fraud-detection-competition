import os

input_path = '../input/'
submissions_path = '../output/'
models_path = '../models/'
tmp_path = '../temp/'

task_type = 'classification'
target_col = 'isFraud'
target_col_vars = [0, 1]

# train_transactions_path = os.path.join(input_path, 'train_transaction.csv')
# train_identify_path = os.path.join(input_path, 'train_identity.csv')
#
# test_transactions_path = os.path.join(input_path, 'test_transaction.csv')
# test_identify_path = os.path.join(input_path, 'test_identity.csv')
