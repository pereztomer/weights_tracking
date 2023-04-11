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
    d = datetime.date(2022, 12, 25)
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
