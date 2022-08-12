from PyQt5.QtWidgets import *
from vocab_quiz_gui import Ui_MainWindow as Start
from quiz import Ui_MainWindow as Quiz
from process_vocab import *
import random


class startWindow(QMainWindow, Start):
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


class quizWindow(QMainWindow, Quiz):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.exclude_search = []
        self.current_term = None
        self.terms, self.definitions = process_vocab()

        self.new_term()

    def new_term(self):
        self.current_term = random.randint(0, len(self.terms) - 1)
        self.label_var_term.setText(self.terms[self.current_term])
        self.exclude_search.append(self.current_term)

        correct_answer = random.randint(0, 3)
        answer = ''

        if correct_answer == 0:
            self.pushButton_answer_A.setText(self.definitions[self.current_term])
            answer = 'a'
            self.pushButton_answer_B.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_C.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_D.setText(self.definitions[self.incorrect_answers()])

        elif correct_answer == 1:
            self.pushButton_answer_B.setText(self.definitions[self.current_term])
            answer = 'b'
            self.pushButton_answer_A.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_C.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_D.setText(self.definitions[self.incorrect_answers()])
        elif correct_answer == 2:
            self.pushButton_answer_C.setText(self.definitions[self.current_term])
            answer = 'c'
            self.pushButton_answer_B.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_A.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_D.setText(self.definitions[self.incorrect_answers()])
        elif correct_answer == 3:
            self.pushButton_answer_D.setText(self.definitions[self.current_term])
            answer = 'd'
            self.pushButton_answer_B.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_A.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_A.setText(self.definitions[self.incorrect_answers()])

    def incorrect_answers(self):
        incorrect_answer = random.choice([i for i in range(0, len(self.terms) - 1) if i not in self.exclude_search])
        self.exclude_search.append(incorrect_answer)
        return incorrect_answer



