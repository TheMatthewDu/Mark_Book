from GUI.MainScreen import MainScreen
import Backend.Calculate_Overall as Overall


if __name__ == "__main__":
    app = MainScreen()
    app.display()
    Overall.main()
