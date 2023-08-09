import json
import csv
import pickle


def load_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def save_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def load_csv(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


def save_csv(data, file_path):
    with open(file_path, 'w', newline='') as csv_file:
        fieldnames = data[0].keys()
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def load_pickle(file_path):
    with open(file_path, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
    return data


def save_pickle(data, file_path):
    with open(file_path, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
