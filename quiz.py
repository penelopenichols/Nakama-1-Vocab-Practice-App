# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quiz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(304, 276)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_answer_C = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_answer_C.setObjectName("pushButton_answer_C")
        self.gridLayout_2.addWidget(self.pushButton_answer_C, 4, 0, 1, 1)
        self.pushButton_answer_B = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_answer_B.setObjectName("pushButton_answer_B")
        self.gridLayout_2.addWidget(self.pushButton_answer_B, 3, 0, 1, 1)
        self.label_text_question = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_text_question.setFont(font)
        self.label_text_question.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_question.setObjectName("label_text_question")
        self.gridLayout_2.addWidget(self.label_text_question, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 7, 0, 1, 1)
        self.pushButton_answer_D = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_answer_D.setObjectName("pushButton_answer_D")
        self.gridLayout_2.addWidget(self.pushButton_answer_D, 5, 0, 1, 1)
        self.label_var_term = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_var_term.setFont(font)
        self.label_var_term.setAlignment(QtCore.Qt.AlignCenter)
        self.label_var_term.setObjectName("label_var_term")
        self.gridLayout_2.addWidget(self.label_var_term, 1, 0, 1, 1)
        self.pushButton_answer_A = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_answer_A.setObjectName("pushButton_answer_A")
        self.gridLayout_2.addWidget(self.pushButton_answer_A, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 304, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_answer_C.setText(_translate("MainWindow", "C"))
        self.pushButton_answer_B.setText(_translate("MainWindow", "B"))
        self.label_text_question.setText(_translate("MainWindow", "What is this word in [Language]?"))
        self.pushButton.setText(_translate("MainWindow", "Finish"))
        self.pushButton_answer_D.setText(_translate("MainWindow", "D"))
        self.label_var_term.setText(_translate("MainWindow", "Term"))
        self.pushButton_answer_A.setText(_translate("MainWindow", "A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
