import os
import os.path
from shutil import copyfile
import shutil


# re-organizes java files in 3 directories: train, validation, test
def separate_train_val_test(test_size, validation_size):
    size = len([name for name in os.listdir('../java_files')])
    test_size = test_size * size
    validation_size = validation_size * size
    src_path = '../dataset/'
    os.makedirs('../dataset/test', exist_ok=True)
    os.makedirs('../dataset/validation', exist_ok=True)
    os.makedirs('../dataset/train', exist_ok=True)
    for i in range(size):
        fname = str(i) + '.java'
        fname_src = '../java_files/' + str(fname)
        print(i)
        if os.path.isfile(fname_src):
            if i < test_size:
                copyfile('../java_files/' + str(fname), src_path + 'test/' + str(fname))
            elif i < test_size + validation_size:
                copyfile('../java_files/' + str(fname), src_path + 'validation/' + str(fname))
            else:
                copyfile('../java_files/' + str(fname), src_path + 'train/' + str(fname))


# re-organizes java files in n directories to be processed separately
def separate_to_parallelism(n_division):
    src_path = 'java-large'
    size = len([name for name in os.listdir(src_path)])
    out_path = 'dataset/'
    for i in range(n_division):
        os.makedirs(out_path + str(i), exist_ok=True)
    for root, subdirs, files in os.walk(src_path):
        n_files_each_directory = len(files)/n_division
        # count = 0
        # curr_out_folder = 0
        for file in files:
            if file.endswith('.java'):
                print(file)
                path = os.path.join(root, file)
                shutil.copy(path, out_path)
            # count += 1
            # if count >= n_files_each_directory:
            #     curr_out_folder += 1
            #     count = 0




separate_to_parallelism(8)
