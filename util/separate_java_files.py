import os
import os.path
from shutil import copyfile


# re-organizes java files in 3 directories: train, validation, test
def fast_method(test_size, validation_size):
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

