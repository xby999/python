# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clock_Vote_0.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import Btn_func
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(773, 892)
        self.MsgStatus = QtWidgets.QTextBrowser(Form)
        self.MsgStatus.setGeometry(QtCore.QRect(0, 510, 771, 381))
        self.MsgStatus.setStyleSheet("gh")
        self.MsgStatus.setObjectName("MsgStatus")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 480, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(620, 450, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda :self.Run_btn_clicked(Btn_func.text))

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 450, 81, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.Clear_btn_clicked())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MsgStatus.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("Form", "Msg Status:"))
        self.pushButton.setText(_translate("Form", "Run"))
        self.pushButton_2.setText(_translate("Form", "Clean"))

    def Run_btn_clicked(self,text):
        result = os.popen(text)
        info = result.readlines()
        print(info)
        for line in info:
            self.MsgStatus.append(line.strip('\r\n'))
            print(line.strip('\r\n'))

    def Clear_btn_clicked(self):
        self.MsgStatus.setText("")