import os
import json


NON_DATA_VALUES = ['DESCRIPTION', 'CURRENT MARK', 'GOAL']


def _is_course(name: str) -> bool:
    return '.json' in name and (name[0:3].isupper() and name[3:6].isdigit())


def _get_dict_average(dictionary: dict):
    num = 0
    accumulator = 0
    for entry in dictionary:
        if dictionary[entry] != '':
            accumulator += float(dictionary[entry])
            num += 1
    if num != 0:
        return accumulator / num
    else:
        return 0.0


def main():
    # Create a dictionary of all the averages of the courses
    average_dict = {}

    directory = 'Datafiles\\Data'
    for filename in os.listdir(directory):
        if _is_course(filename):
            directory_file_name = f"{directory}\\{filename}"
            storage_file = open(directory_file_name)
            data = json.load(storage_file)

            average_dict[filename[0:-4]] = data['CURRENT MARK']

    total_average = _get_dict_average(average_dict)

    # Write the info to file
    output = open("Backend\\Overall Averages.txt", 'w')

    for average in average_dict:
        avg = average_dict[average]
        if avg == '':
            output.write(f'{average}: 0.00 \n')
        else:
            output.write(f'{average}: {round(float(avg), 2)} \n')

    output.write(f'OVERALL AVERAGE: {round(total_average, 2)}')

    if round(total_average, 2) < 85:
        output.write(f'\nDanger! Below Goal by {round(85 - total_average, 2)}%')
    else:
        output.write(f'\nGood. Above Goal by {round(total_average - 85, 2)}%')

    output.flush()
    output.close()


if __name__ == '__main__':
    main()
