import os

try:
    import csv
except ImportError:
    print("Trying to Install required module: csv\n")
    os.system('pip3 install csv')

import csv

# -- input items from csv
def csv_in(file):
    items = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for item in csv_reader:
            if item:
                items.append(item[0])
    return items

# -- output items to csv
def csv_out(file, items):
    with open(file, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in items:
            csv_writer.writerow(item)