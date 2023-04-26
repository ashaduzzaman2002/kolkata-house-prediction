import csv
import os


current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir, '../'))
# parent_dir = os.path.abspath(os.path.join(current_dir))
file_path = os.path.join(parent_dir, "Kolkata.csv")

location_list = []
yesNoParameter_list =[]


def getLocationList():
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            location_list.append(row['Location'])

    return sorted(list(set(location_list)))

def yesNoParameters():
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        header_row = next(csv_reader)
        for column_name in header_row.keys():
            if(column_name!='Price' and column_name != 'Area' and column_name != 'No. of Bedrooms' and column_name != 'Location'):
                yesNoParameter_list.append(column_name)
    return sorted(list(set(yesNoParameter_list)))



