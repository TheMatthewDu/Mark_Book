from src.Backend import Calculate_Overall
from Backend.Controller import Controller


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


def run_cmd_line() -> None:
    """ The main body of the function. Runs all the components """
    entry_message = "MarkBook Application\n" \
                    "Created By Matthew Du\n" \
                    "Enter `mb-help` for full instructions\n"

    print(entry_message)

    running = True
    factory = Controller()
    while running:
        cmd = input("MarkBook > ").strip().split(sep=" ")
        response = factory.process_command(cmd[0], cmd[1:])
        if response is not None:
            print(response)


if __name__ == "__main__":
    run_cmd_line()
    Calculate_Overall.main()
    input('Press Enter to Exit: ')
