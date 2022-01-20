import csv
import json
from src.Backend.DataReader import DataReader
from src.Backend.DataObject import DataObject


DESCRIPTION = 'DESCRIPTION'
CURRENT_MARK = "CURRENT MARK"
GOAL = 'GOAL'
NON_DATA_VALUES = [DESCRIPTION, CURRENT_MARK, GOAL]


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


def _create_backup(name: str) -> None:
    """ Create a backup of the previous state of the files

    :param name: the name of the course for the backup
    :return: None
    """
    # Quick Backup
    filename = f"DataFiles\\Data\\{name}.json"
    backup = open(f'BACKUPS\\{name}_BACKUP.json', 'w')
    file = open(filename, 'r')

    backup_read = json.load(file)
    json.dump(backup_read, backup)

    file.close()
    backup.close()


def read(name_file: str) -> DataObject:
    """ Reads the data with the course name name_file

    :param name_file: the name of the course
    :return: A DataObject of the data
    """
    # Quick Backup
    reader = DataReader(name_file)

    _create_backup(name_file)

    return reader.get_data()


def write_data(data: DataObject, filename: str) -> None:
    """ Writes the data into the specified file

    :param data: the data object where the data is stored
    :param filename: the name of the file to be written
    :return: None
    """
    storage_file = open(f"DataFiles\\Data\\{filename}.json", 'w')
    json.dump(data.get_storage(), storage_file)
    storage_file.close()

    weights_file = open(f"DataFiles\\Weights\\{filename}_weights.json", 'w')
    json.dump(data.get_weights(), weights_file)
    weights_file.close()


def analyze_data(storage: DataObject) -> None:
    """ Print the analysis of the grade on the storage object

    :param storage: the DataObject storing the information
    :return: None
    """
    print(storage.generate_analysis())


def load_json(data: dict, course_name: str):
    file = open(f"{course_name}.json", "w")
    json.dump(data, file)
