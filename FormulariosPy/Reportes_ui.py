# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Formularios/Reportes.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(535, 239)
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(-1, -1, 541, 101))
        self.widget_4.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        self.label_16.setGeometry(QtCore.QRect(140, 20, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setGeometry(QtCore.QRect(0, 100, 541, 31))
        self.widget_5.setStyleSheet("\n"
"background-color: rgb(49, 0, 74);")
        self.widget_5.setObjectName("widget_5")
        self.label_17 = QtWidgets.QLabel(self.widget_5)
        self.label_17.setGeometry(QtCore.QRect(140, 0, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"")
        self.label_17.setObjectName("label_17")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 160, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 160, 161, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "REPORTES"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Ice Cream &quot;Faván”</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Manta - Manabí - Ecuador</span></p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">EXPORTAR REPORTES</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "CLIENTES"))
        self.pushButton_2.setText(_translate("Form", "PERSONAL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
