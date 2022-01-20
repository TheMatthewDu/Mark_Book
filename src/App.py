from GUI.MainScreen import MainScreen
import Backend.Calculate_Overall as Overall
import CommandLine


if __name__ == "__main__":
    try:
        app = MainScreen()
        app.display()
        Overall.main()
    except ModuleNotFoundError:
        CommandLine.main()
        Overall.main()
        input('Press Enter to Exit: ')
