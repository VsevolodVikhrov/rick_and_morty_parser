import json

file_name = "backuped_data.json"


def load_data():
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
        return data


def save_data(data):
    with open(file_name, "w") as write_file:
        json.dump(data, write_file)
