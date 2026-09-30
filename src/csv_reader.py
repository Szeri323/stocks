import csv

def read_from_csv(file_destination):
    with open(file_destination, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        array = []
        for row in reader:
            print(', '.join(row))
            array.append(row)
        return array

def write_to_csv(file_destination, data_rows):
    with open(file_destination, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in data_rows:
            print(row)
            writer.writerow(row)

def append_to_csv(file_destination, data_rows):
    with open(file_destination, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in data_rows:
            print(row)
            writer.writerow(row)