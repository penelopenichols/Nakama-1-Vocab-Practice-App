from controller import *


def main():
    app = QApplication([])
    window = quizWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
