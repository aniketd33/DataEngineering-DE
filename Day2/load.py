import json


def load_data(data):

    with open("output.json", "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )