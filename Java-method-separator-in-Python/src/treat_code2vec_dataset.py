import csv
import sys

csv.field_size_limit(sys.maxsize)

def treat_code2vec_database():
    with open('/home/arthur/Documents/result.csv') as file:
        reader = csv.reader(file)
        final_list = list()

        for row in reader:
            if row[1] not in final_list:
                final_list.append(row[1])
    return final_list