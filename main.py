import get_data
import parse_data
import file_processing
import os.path
import handlers


def check_file_existing():
    file_path = "backuped_data.json"
    is_file_exists = os.path.isfile(file_path)
    return is_file_exists


def load_backuped_or_get_data():
    if check_file_existing():
        data = file_processing.load_data()
    else:
        data = parse_data.parse_get_request()
        file_processing.save_data(data)
    return data


def init_characters():
    data = load_backuped_or_get_data()
    list_of_characters = []
    for i in data:
        character = Character(
            name=i["name"],
            status=i["status"],
            species=i["species"],
            gender=i["gender"],
            location=i["location"]
        )
        list_of_characters.append(character)
    return list_of_characters


def input_command():
    while True:
        command = input("Input your command: ")
        handlers.handle_command(command)


class Character:
    def __init__(self, name, status, species, gender, location):
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.location = location


class Aggregator:
    data = init_characters()
    alive = 0
    unknown = 0
    locations = 0
    human = 0

    def show_alive(self):
        for i in self.data:
            if i.status == "Alive":
                self.alive += 1

    def show_unknown(self):
        for i in self.data:
            if i.status == "unknown":
                self.unknown += 1

    def show_human_species(self):
        for i in self.data:
            if i.species == "Human":
                self.human += 1

    def show_locations(self):
        locations = {}
        list_of_locations = []
        for i in self.data:
            list_of_locations.append(i.location)
        for i in list_of_locations:
            if i not in locations:
                locations.update({i: 1})
            else:
                locations[i] = locations[i] + 1
        self.locations = locations


if __name__ == '__main__':
    input_command()

