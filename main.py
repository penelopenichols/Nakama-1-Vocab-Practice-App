from controller import *


def main():
    """
    runs the application. Displays the GUI
    """
    app = QApplication([])
    window = quizWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
