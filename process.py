import csv

def process_file(file):
    reader = csv.DictReader(file)
    list = []

    for line in reader:
        list.append(line)

    for entry in list:
        print(f'name: {entry["name"]}, type: {entry["type"]}, max_rabi: {entry["maximum_rabi_rate"]}, polar_angle: {entry["polar_angle"]}')


file = open("controls.csv")
process_file(file)
