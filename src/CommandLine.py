from src.Backend import Markbook
from src.Backend import Calculate_Overall
from src.Backend.DataInput import DataInput


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
    data = Markbook.read(filename)

    data_input = DataInput(data)
    data_input.input_data()

    Markbook.write_data(data, filename)
    Markbook.analyze_data(data)


if __name__ == "__main__":
    main()
    Calculate_Overall.main()
    input('Press Enter to Exit: ')
