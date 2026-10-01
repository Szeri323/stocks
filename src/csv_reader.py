import csv

def read_from_csv(file_destination):
    with open(file_destination, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        array = []
        for row in reader:
            array.append(row)
        return array

def write_to_csv(file_destination, data_rows):
    with open(file_destination, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if type(data_rows) == list:
            for row in data_rows:
                writer.writerow(row)
        if type(data_rows) == dict:
            for key, value in data_rows.items():
                values = []
                for value2 in value.values():
                        values.append(value2)
                new_arr = [key] +values
                writer.writerow(new_arr)

def append_to_csv(file_destination, data_rows):
    with open(file_destination, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if type(data_rows) == list:
            for row in data_rows:
                writer.writerow(row)
        if type(data_rows) == dict:
            for key, value in data_rows.items():
                values = []
                for value2 in value.values():
                        values.append(value2)
                new_arr = [key] +values
                writer.writerow(new_arr)
        