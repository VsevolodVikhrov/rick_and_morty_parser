from main import Aggregator


def handle_command(command):
    if "show status" in command:
        if "alive" in command:
            show_status(alive=True)
        elif "unknown" in command:
            show_status(unknown=True)
        else:
            show_status(alive=True, unknown=True)
    elif "show species" in command:
        if "human" in command:
            show_species(human=True)
        elif "alien" in command:
            show_species(alien=True)
        else:
            show_species(human=True, alien=True)
    elif command == "show location":
        show_locations()
    else:
        print("Incorrect input! Please try again")


def show_species(human=False, alien=False):
    human_count = Aggregator()
    human_count = human_count.show_human_species()
    alien_count = Aggregator()
    alien_count = alien_count.show_alien_species()
    asked_human_value = f"Human {human_count}"
    asked_alien_value = f"Alien {alien_count}"
    if human and alien:
        printer(f"{asked_human_value}\n{asked_alien_value}")
    elif human:
        printer(asked_human_value)
    else:
        printer(asked_alien_value)


def show_status(alive=False, unknown=False):
    alive_count = Aggregator()
    alive_count = alive_count.show_alive()
    unknown_count = Aggregator()
    unknown_count = unknown_count.show_unknown()
    asked_alive_value = f"Alive {alive_count}"
    asked_unknown_value = f"Unknown {unknown_count}"
    if alive and unknown:
        printer(asked_alive_value + "\n" + asked_unknown_value)
    elif alive:
        printer(asked_alive_value)
    else:
        printer(asked_unknown_value)


def show_locations():
    locations = Aggregator()
    locations = locations.show_locations()
    printer(locations)


def printer(print_data):
    if isinstance(print_data, dict):
        for key, value in print_data.items():
            print(f"{key} : {value}")
    else:
        print(print_data)
