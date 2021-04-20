import json


def load_data():
    with open("backuped_data.json", "r") as read_file:
        data = json.load(read_file)
        return data


def save_data(data):
    with open("backuped_data.json", "w") as write_file:
        json.dump(data, write_file)
