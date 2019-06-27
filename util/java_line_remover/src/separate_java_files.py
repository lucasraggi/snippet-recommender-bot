import os
import os.path
from shutil import copyfile


def fast_method():
    size = len([name for name in os.listdir('../java_files')])
    test_size = 0.80 * size
    validation_size = 0.10 * size
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


fast_method()
