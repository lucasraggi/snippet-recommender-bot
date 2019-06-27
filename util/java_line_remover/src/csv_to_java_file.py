import pandas as pd
import os


# transform csv methods into java files for each method
def main():
    methods_df = pd.read_csv('../result.csv')
    directory_path = '../java_files'
    os.makedirs(directory_path, exist_ok=True)
    os.chdir(directory_path)  # setting working directory to path
    start = 0
    file_count = start
    for i, row in methods_df.iterrows():
        file_name = str(file_count) + '.java'
        f = open(file_name, 'w+')
        method_name = row['name']
        file_start_string = 'public class ' + method_name + ' {\n\n'
        method = row['codes']
        file_end_string = '\n}'
        string_to_file = file_start_string + str(method) + file_end_string
        f.write(string_to_file)
        f.close()
        file_count += 1


main()