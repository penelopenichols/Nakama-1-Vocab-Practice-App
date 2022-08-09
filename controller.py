from PyQt5.QtWidgets import *
from vocab_quiz_gui import Ui_MainWindow
from process_vocab import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.terms = []
        self.definitions = []
        self.language = ''
        self.pushButton_start.clicked.connect(lambda: self.start_quiz())

    def start_quiz(self):

        if self.buttonGroup_radio_language.checkedButton() is not None:
            if self.radioButton_english.isChecked():
                self.language = 'english'
            elif self.radioButton_japanese.isChecked():
                self.language = 'japanese'

            self.terms, self.definitions = process_vocab(language=self.language)
            print(self.terms)
            print(self.definitions)

            self.hide_start_menu()

    def hide_start_menu(self):
        self.label_text_asnwer_language.hide()
        self.radioButton_japanese.hide()
        self.radioButton_english.hide()
        self.pushButton_start.hide()
