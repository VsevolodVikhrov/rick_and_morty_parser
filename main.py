import parse_data
import file_processing
import os.path
import handlers
import dataclasses


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
        if i["species"] == "Human":
            special_character = Human(
                name=i["name"],
                status=i["status"],
                species=i["species"],
                gender=i["gender"],
                location=i["location"]
            )
        else:
            special_character = Alien(
                name=i["name"],
                status=i["status"],
                species=i["species"],
                gender=i["gender"],
                location=i["location"]
            )
        list_of_characters.append(special_character)
        print(special_character) # Почему в листе отображаются такие странные значения объектов класса?
    return list_of_characters


def input_command():
    while True:
        command = input("Input your command: ")
        handlers.handle_command(command)


@dataclasses.dataclass()
class Character:
    name: str
    status: str
    species: str
    gender: str
    location: str


species_registry = {}


class SpeciesMeta(type):
    def __new__(mcs, class_name, superclass, attrs):
        species_type = class_name
        species_class = type(class_name, superclass, attrs)
        if species_type not in species_registry.keys():
            species_registry.update({species_type: species_class})
        return species_class


class Human(Character, metaclass=SpeciesMeta):
    type = "Human"


class Alien(Character, metaclass=SpeciesMeta):
    type = "Alien"


class Aggregator:
    data = init_characters()
    alive = 0
    unknown = 0
    locations = 0
    human = 0
    alien = 0

    def show_alive(self):
        for i in self.data:
            if i.status == "Alive":
                self.alive += 1
        return self.alive

    def show_unknown(self):
        for i in self.data:
            if i.status == "unknown":
                self.unknown += 1
        return self.unknown

    def show_human_species(self):
        for i in self.data:
            if i.species == "Human":
                self.human += 1
        return self.human

    def show_alien_species(self):
        for i in self.data:
            if i.species == "Alien":
                self.alien += 1
        return self.alien

    def show_locations(self):
        location_count = {}
        for i in self.data:
            if i.location not in location_count:
                location_count[i.location] = 0
            location_count[i.location] += 1
        self.locations = location_count
        return self.locations


if __name__ == '__main__':
    input_command()

