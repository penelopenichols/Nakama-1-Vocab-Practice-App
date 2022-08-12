from PyQt5.QtWidgets import *
from quiz import Ui_MainWindow as Quiz
from process_vocab import *
import random


class quizWindow(QMainWindow, Quiz):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.exclude_search = []
        self.current_term = None
        self.answer = None
        self.total_questions = 0
        self.total_correct_answers = 0
        self.terms, self.definitions = process_vocab()

        self.view_quiz_mode()

        self.pushButton_answer_A.clicked.connect(lambda: self.answered(letter='a'))
        self.pushButton_answer_B.clicked.connect(lambda: self.answered(letter='b'))
        self.pushButton_answer_C.clicked.connect(lambda: self.answered(letter='c'))
        self.pushButton_answer_D.clicked.connect(lambda: self.answered(letter='d'))

        self.pushButton_finish.clicked.connect(lambda: self.view_finish_mode())
        self.pushButton_restart.clicked.connect(lambda: self.view_quiz_mode())

    def view_quiz_mode(self):
        self.total_questions = 0
        self.total_correct_answers = 0
        self.label_text_feedback.setVisible(False)
        self.label_text_yourscoreis.setVisible(False)
        self.label_score.setVisible(False)
        self.label_percentage.setVisible(False)
        self.pushButton_restart.setVisible(False)
        self.pushButton_finish.setEnabled(False)

        self.label_text_question.setVisible(True)
        self.label_var_term.setVisible(True)
        self.pushButton_answer_A.setVisible(True)
        self.pushButton_answer_B.setVisible(True)
        self.pushButton_answer_C.setVisible(True)
        self.pushButton_answer_D.setVisible(True)
        self.pushButton_finish.setVisible(True)

        self.new_term()

    def view_finish_mode(self):
        self.label_text_question.setVisible(False)
        self.label_var_term.setVisible(False)
        self.pushButton_answer_A.setVisible(False)
        self.pushButton_answer_B.setVisible(False)
        self.pushButton_answer_C.setVisible(False)
        self.pushButton_answer_D.setVisible(False)
        self.pushButton_finish.setVisible(False)

        self.label_text_feedback.setVisible(False)

        self.label_text_yourscoreis.setVisible(True)
        self.label_score.setVisible(True)
        self.label_percentage.setVisible(True)
        self.pushButton_restart.setVisible(True)

        self.display_score()

    def new_term(self):
        self.exclude_search = []
        self.current_term = random.randint(0, len(self.terms) - 1)
        self.label_var_term.setText(self.terms[self.current_term])
        self.exclude_search.append(self.current_term)

        correct_answer = random.randint(0, 3)

        if correct_answer == 0:
            self.pushButton_answer_A.setText(self.definitions[self.current_term])
            self.answer = 'a'
            self.pushButton_answer_B.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_C.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_D.setText(self.definitions[self.incorrect_answers()])

        elif correct_answer == 1:
            self.pushButton_answer_B.setText(self.definitions[self.current_term])
            self.answer = 'b'
            self.pushButton_answer_A.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_C.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_D.setText(self.definitions[self.incorrect_answers()])

        elif correct_answer == 2:
            self.pushButton_answer_C.setText(self.definitions[self.current_term])
            self.answer = 'c'
            self.pushButton_answer_B.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_A.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_D.setText(self.definitions[self.incorrect_answers()])

        elif correct_answer == 3:
            self.pushButton_answer_D.setText(self.definitions[self.current_term])
            self.answer = 'd'
            self.pushButton_answer_B.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_A.setText(self.definitions[self.incorrect_answers()])
            self.pushButton_answer_C.setText(self.definitions[self.incorrect_answers()])

    def incorrect_answers(self):
        incorrect_answer = random.choice([i for i in range(0, len(self.terms) - 1) if i not in self.exclude_search])
        self.exclude_search.append(incorrect_answer)
        return incorrect_answer

    def answered(self, letter):
        self.total_questions += 1
        self.label_text_feedback.setVisible(True)
        if letter == self.answer:
            self.label_text_feedback.setText("Correct!")
            self.label_text_feedback.setStyleSheet("color: green")
            self.total_correct_answers += 1
        else:
            self.label_text_feedback.setText(f"Incorrect! {self.terms[self.current_term]} in Japanese is {self.definitions[self.current_term]}")
            self.label_text_feedback.setStyleSheet("color: red")

        self.pushButton_finish.setEnabled(True)
        self.new_term()

    def display_score(self):
        percentage = (self.total_correct_answers/self.total_questions) * 100
        self.label_score.setText(f"{self.total_correct_answers}/{self.total_questions}")
        self.label_percentage.setText(f"Or: {percentage:.1f}%")

        if percentage >= 90:
            color = "color: green"
        elif percentage >= 70:
            color = "color: orange"
        else:
            color = "color: red"

        self.label_score.setStyleSheet(color)
        self.label_percentage.setStyleSheet(color)
        self.label_text_yourscoreis.setStyleSheet(color)
