from PyQt5.QtWidgets import *
from quiz import Ui_MainWindow as Quiz
from process_vocab import *
import random


class quizWindow(QMainWindow, Quiz):
    """
    Class for the quiz window screen
    """
    def __init__(self, *args, **kwargs):
        """
        Defines the initialization of the quizWindow class object
        :param args: Takes arguments from quiz.py
        :param kwargs: Takes arguments from quiz.py
        """
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
        """
        Sets the elements for the quiz visible and the elements for the 'Finish' screen invisible.
        Runs self.new_term()
        """
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
        """
        Sets the elements for the quiz invisible and the elements for the 'Finish' screen visible.
        Runs self.display_score()
        :return:
        """
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
        """
        Sets up the UI to display the new question as well as sets the correct and incorrect answers
        """
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
        """
        Creates dummy answers to display in the non-correct answer pushButtons for each term
        :return: a random int in range of self.terms as long as it is not in self.exclude_search
        """
        incorrect_answer = random.choice([i for i in range(0, len(self.terms) - 1) if i not in self.exclude_search])
        self.exclude_search.append(incorrect_answer)
        return incorrect_answer

    def answered(self, letter):
        """
        Tallies correct answers, gives you visual feedback on whether the answer was correct or not
        :param letter: the letter of the button clicked. Checks if this letter matches self.answer
        """
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
        """
        When the 'Finish' button is clicked, displays score as a ratio and a percentage.
        Changes text color based on amount of correct answers over the total questions asked.
        """
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
