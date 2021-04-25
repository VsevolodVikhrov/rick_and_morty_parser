import get_data


def parse_get_request():
    data = get_data.get_characters()
    list_of_characters = []
    for i in data:
        list_of_characters.append({
            "name": i["name"],
            "status": i["status"],
            "species": i["species"],
            "gender": i["gender"],
            "location": i["location"]["name"]
        })
    return list_of_characters

