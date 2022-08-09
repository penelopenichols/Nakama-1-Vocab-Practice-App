from PyQt5.QtWidgets import *
from vocab_quiz_gui import Ui_MainWindow
from process_vocab import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
