from main import Aggregator


def handle_command(command):
    if "show status" in command:
        if "alive" in command:
            show_status(alive=True)
        elif "unknown" in command:
            show_status(unknown=True)
        else:
            show_status(alive=True, unknown=True)
    elif command == "show species human":
        show_human_count()
    elif command == "show location":
        show_locations()
    else:
        print("Incorrect input! Please try again")


def show_status(alive=False, unknown=False):
    alive_count = Aggregator()
    alive_count.show_alive()
    unknown_count = Aggregator()
    unknown_count.show_unknown()
    alive_count = alive_count.alive
    unknown_count = unknown_count.unknown
    asked_alive_value = f"Alive {alive_count}"
    asked_unknown_value = f"Unknown {unknown_count}"
    if alive and not unknown:
        printer(asked_alive_value)
    elif unknown and not alive:
        printer(asked_unknown_value)
    else:
        printer(asked_alive_value + "\n" + asked_unknown_value)


def show_human_count():
    human_count = Aggregator()
    human_count.show_human_species()
    printer(human_count.human)


def show_locations():
    locations = Aggregator()
    locations.show_locations()
    locations = locations.locations
    printer(locations)


def printer(print_data):
    if type(print_data) is dict:
        for key, value in print_data.items():
            print(f"{key} : {value}")
    else:
        print(print_data)