import os
from typing import List, TextIO


NON_DATA_VALUES = ['DESCRIPTION', 'CURRENT MARK', 'GOAL']


def is_number(value: str) -> bool:
    """Return True if and only if value represents a decimal number.

    >>> is_number('csc108')
    False
    >>> is_number('  108 ')
    True
    >>> is_number('+3.14159')
    True
    """

    return value.strip().lstrip('-+').replace('.', '', 1).isnumeric()


def clean_data(data: List[list]) -> None:
    """Convert each string in data to an int if and only if it represents a
    whole number, and a float if and only if it represents a number that is not
    a whole number.

    >>> d = [['abc', '123', '45.6', 'car', 'Bike']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, 'car', 'Bike']]
    >>> d = [['ab2'], ['-123'], ['BIKES', '3.2'], ['3.0', '+4', '-5.0']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], ['BIKES', 3.2], [3, 4, -5]]
    """

    new_data = []
    for item in data:
        sub_new_data = []
        for it in item:
            sign_log = False
            sign = ''
            if is_number(it):
                if it[0] == '+' or it[0] == '-':
                    sign_log = True
                    sign += it[0]
                    a = it[1:]
                else:
                    a = it

                if float(a) % 1 == 0:
                    if sign_log:
                        sub_new_data.append(int(float(sign + a)))
                    else:
                        sub_new_data.append(int(float(a)))
                else:
                    if sign_log:
                        sub_new_data.append(float(sign + a))
                    else:
                        sub_new_data.append(float(a))

            else:
                sub_new_data.append(it)

        new_data.append(sub_new_data)

    data.clear()

    data += new_data


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
    clean_data(contents)

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
            accumulator += dictionary[entry]
            num += 1

    return accumulator / num


def main():
    # Create a dictionary of all the averages of the courses
    average_dict = {}

    directory = 'src\\Datafiles'
    for filename in os.listdir(directory):
        if _is_course(filename):
            file = open(f"{directory}\\{filename}")
            data = get_storage_dict(file)
            average_dict[filename[0:-4]] = data['CURRENT MARK']

    total_average = _get_dict_average(average_dict)

    # Write the info to file
    output_filename = 'Overall Averages.txt'
    output = open(output_filename, 'w')

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
