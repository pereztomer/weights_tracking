import json
import datetime


def add_weight(new_weight, date):
    f = open('tomer_weights.json')
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    data.append((new_weight, date))

    # Serializing json
    json_object = json.dumps(data, indent=4)

    with open("tomer_weights.json", "w") as outfile:
        outfile.write(json_object)


def main(name):
    d = datetime.date(2022, 3, 26)
    weight = 61.4
    add_weight(weight, d)


if __name__ == '__main__':
    json_object = json.dumps([], indent=4)

    with open("tomer_weights.json", "w") as outfile:
        outfile.write(json_object)
    main('PyCharm')

