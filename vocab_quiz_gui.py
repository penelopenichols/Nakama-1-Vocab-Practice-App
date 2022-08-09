# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vocab_quiz_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_var_term = QtWidgets.QLabel(self.centralwidget)
        self.label_var_term.setGeometry(QtCore.QRect(130, 170, 47, 14))
        self.label_var_term.setObjectName("label_var_term")
        self.label_var_definition = QtWidgets.QLabel(self.centralwidget)
        self.label_var_definition.setGeometry(QtCore.QRect(200, 170, 47, 14))
        self.label_var_definition.setObjectName("label_var_definition")
        self.label_text_term = QtWidgets.QLabel(self.centralwidget)
        self.label_text_term.setGeometry(QtCore.QRect(130, 150, 47, 14))
        self.label_text_term.setObjectName("label_text_term")
        self.label_text_definition = QtWidgets.QLabel(self.centralwidget)
        self.label_text_definition.setGeometry(QtCore.QRect(200, 150, 47, 14))
        self.label_text_definition.setObjectName("label_text_definition")
        self.radioButton_english = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_english.setGeometry(QtCore.QRect(150, 30, 80, 18))
        self.radioButton_english.setObjectName("radioButton_english")
        self.radioButton_japanese = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_japanese.setGeometry(QtCore.QRect(150, 60, 80, 18))
        self.radioButton_japanese.setObjectName("radioButton_japanese")
        self.label_text_asnwer_language = QtWidgets.QLabel(self.centralwidget)
        self.label_text_asnwer_language.setGeometry(QtCore.QRect(10, 10, 191, 21))
        self.label_text_asnwer_language.setObjectName("label_text_asnwer_language")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
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
        self.label_var_term.setText(_translate("MainWindow", "TextLabel"))
        self.label_var_definition.setText(_translate("MainWindow", "TextLabel"))
        self.label_text_term.setText(_translate("MainWindow", "Term:"))
        self.label_text_definition.setText(_translate("MainWindow", "Definition:"))
        self.radioButton_english.setText(_translate("MainWindow", "English"))
        self.radioButton_japanese.setText(_translate("MainWindow", "Japanese"))
        self.label_text_asnwer_language.setText(_translate("MainWindow", "Choose what language to answer in:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())