from src import *


def main():
    try:
        run_app()
    except ModuleNotFoundError:
        run_cmd_line()
        input('Press Enter to Exit: ')
    # run_cmd_line()
    # Calculate_Overall.main()


if __name__ == "__main__":
    main()
