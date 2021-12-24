import csv
from src.Backend.DataReader import DataReader
from src.Backend.DataInput import DataInput
from src.Backend.DataObject import DataObject
from typing import Tuple, Any

DESCRIPTION = 'DESCRIPTION'
CURRENT_MARK = "CURRENT MARK"
GOAL = 'GOAL'
NON_DATA_VALUES = [DESCRIPTION, CURRENT_MARK, GOAL]


def _create_backup(name: str) -> None:
    """ Create a backup of the previous state of the files

    :param: name: the name of the course for the backup
    """
    # Quick Backup
    filename = f"DataFiles\\{name}.csv"
    backup = open(f'BACKUPS\\{name}_BACKUP.csv', 'w')
    file = open(filename, 'r')

    backup_read = file.read()
    backup.write(backup_read)

    file.close()
    backup.close()


def read(name_file: str) -> DataObject:
    """ Reads the data with the course name name_file

    :param: name_file: the name of the course
    :return: A DataObject of the data
    """
    # Quick Backup
    filename = f"DataFiles\\{name_file}.csv"
    reader = DataReader(filename)

    _create_backup(name_file)

    return reader.get_data()


def write_data(data: DataObject, filename: str) -> None:
    """ Writes the data into the specified file

    :param: data: the data object where the data is stored
    :param: filename: the name of the file to be written
    """
    # Get a list of items to be written
    writing_list = data.sort_for_writing(filename)

    # opening the csv file in 'w+' mode
    file = open(f"DataFiles\\{filename}.csv", 'w+', newline='')

    # writing the data into the file
    with file:
        write = csv.writer(file)
        write.writerows(writing_list)

    file.close()


def analyze_data(storage: DataObject) -> None:
    """ Print the analysis of the grade on the storage object

    :param: storage: the DataObject storing the information
    """
    print(storage.generate_analysis())


def check_course_code(code: str) -> str:
    """ Check if the code is valid. Fix if not

    :param: code: the code entered by the user

    :return: a correctly formatted course code
    """
    if not (len(code) == 6 or len(code) == 8) or not code[:3].isalpha() \
            or not code[3:6].isdigit():
        raise FileNotFoundError

    copy_of_code = code
    if code[:3].islower():
        copy_of_code = code[:3].upper() + code[3:]
    if len(code) == 6:
        copy_of_code = code + 'H1'
    if code[:-2] == 'h1':
        copy_of_code = code[:-2] + 'H1'
    return copy_of_code


def main() -> None:
    """ The main body of the function. Runs all the components """
    entry_message = '*** THIS IS THE MARK BOOK *** \n CREATED BY MATTHEW DU \n' \
                    'ALL FILES ARE OPEN AND WRITTEN AS CSV FILES. \n PLEASE ' \
                    'USE THE PROPER TEMPLATE FOR THE DATA'

    print(entry_message)

    file = input("Enter Course Name: ")
    filename = check_course_code(file)
    data = read(filename)

    data_input = DataInput(data)
    data_input.input_data()

    write_data(data, filename)
    analyze_data(data)


def gui_read(file: str) -> DataObject:
    """ The main body of the function. Runs all the components """
    filename = check_course_code(file)
    return read(filename)


def gui_input(data: Tuple[Any, Any, Any], data_obj: DataObject):
    data_input = DataInput(data_obj)
    return data_input.gui_input_data(data)


def gui_write(data, filename):
    write_data(data, filename)


if __name__ == '__main__':
    main()
    input('Press Enter to Exit: ')
