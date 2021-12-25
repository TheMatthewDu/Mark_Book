import os
from typing import List, TextIO


NON_DATA_VALUES = ['DESCRIPTION', 'CURRENT MARK', 'GOAL']


def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on data to be input.
    """

    # Read and discard header.
    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data


def get_storage_dict(file: TextIO) -> dict:
    """ Get the storage dict
    """
    # Clean the data
    contents = csv_to_list(file)

    # Empty dicts
    storage = {}

    for item in contents:
        # Getting the goal
        if item[0] == 'GOAL':
            storage['GOAL'] = item[1]

        # Getting the current mark
        if item[0] == 'CURRENT MARK':
            storage['CURRENT MARK'] = item[1]

    # Get a sublist of all the data in contents
    s2 = []
    for it in contents:
        s2.append([it[0], it[1]])

    # Filter the empty sublists
    for entry in s2:
        if entry == ['','']:
            s2.remove(entry)

    # Get the individual entries and the mark
    name = ''
    for enter in s2:

        # If the enter is a divider
        if enter[0].isupper() and enter[0] not in NON_DATA_VALUES:
            storage[enter[0]] = []
            name = enter[0]

        # Append all the individual entries
        if not(enter[0].isupper()) and enter[1] != '':
            storage[name].append(enter)

    return storage


def _is_course(name: str) -> bool:
    return '.csv' in name and (name[0:3].isupper() and name[3:6].isdigit())


def _get_dict_average(dictionary: dict):
    num = 0
    accumulator = 0
    for entry in dictionary:
        if dictionary[entry] != '':
            accumulator += float(dictionary[entry])
            num += 1

    return accumulator / num


def main():
    # Create a dictionary of all the averages of the courses
    average_dict = {}

    directory = 'Datafiles'
    for filename in os.listdir(directory):
        if _is_course(filename):
            file = open(f"{directory}\\{filename}")
            data = get_storage_dict(file)
            average_dict[filename[0:-4]] = data['CURRENT MARK']

    total_average = _get_dict_average(average_dict)

    # Write the info to file
    output_filename = 'Overall Averages.txt'
    output = open(f"Backend\\{output_filename}", 'w')

    for average in average_dict:
        avg = average_dict[average]
        if avg == '':
            output.write(f'{average}: 0.00 \n')
        else:
            output.write(f'{average}: {round(float(avg), 2)} \n')

    output.write(f'OVERALL AVERAGE: {round(total_average, 2)}')

    if round(total_average, 2) < 80:
        output.write(f'\nDanger! Below Goal by {round(80 - total_average, 2)}%')
    else:
        output.write(f'\nGood. Above Goal by {round(total_average - 80, 2)}%')

    output.close()


if __name__ == '__main__':
    main()
