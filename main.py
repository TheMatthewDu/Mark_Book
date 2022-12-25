from src.Controllers import Controller
from src.GUI.MainScreen import MainScreen


def run_cmd_line() -> None:
    """ The main body of the function. Runs all the components """
    entry_message = "MarkBook Application\n" \
                    "Created By Matthew Du\n" \
                    "Enter `help` for full instructions\n"

    print(entry_message)

    running = True
    factory = Controller()
    while running:
        cmd = input("MarkBook > ").strip().split(sep=" ")
        response = factory.process_command(cmd[0], cmd[1:])
        if response is not None:
            print(response)


def run_app():
    app = MainScreen()
    app.display()


def main():
    try:
        run_app()
    except ModuleNotFoundError:
        run_cmd_line()
        input('Press Enter to Exit: ')


if __name__ == "__main__":
    # main()
    run_cmd_line()
    input('Press Enter to Exit: ')
