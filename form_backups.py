# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormBackup(object):        
    def setupUi(self, FormBackup):
        FormBackup.setObjectName("FormBackup")
        FormBackup.resize(500, 405)
        FormBackup.setMaximumSize(QtCore.QSize(500, 405))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/aelmac_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormBackup.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormBackup)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 481, 121))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.radio_export = QtWidgets.QRadioButton(self.groupBox)
        self.radio_export.setGeometry(QtCore.QRect(36, 60, 171, 22))
        self.radio_export.setObjectName("radio_export")
        self.radio_import = QtWidgets.QRadioButton(self.groupBox)
        self.radio_import.setGeometry(QtCore.QRect(280, 60, 161, 22))
        self.radio_import.setObjectName("radio_import")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 481, 211))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(15, 47, 445, 21))
        self.label.setObjectName("label")
        self.txt_user = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_user.setGeometry(QtCore.QRect(15, 70, 450, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_user.setFont(font)
        self.txt_user.setObjectName("txt_user")
        self.txt_password = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_password.setGeometry(QtCore.QRect(15, 150, 410, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_password.setFont(font)
        self.txt_password.setText("")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(15, 127, 445, 21))
        self.label_2.setObjectName("label_2")
        self.btn_show_password = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_show_password.setGeometry(QtCore.QRect(430, 150, 32, 32))
        self.btn_show_password.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/EnablePassword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_show_password.setIcon(icon1)
        self.btn_show_password.setFlat(True)
        self.btn_show_password.setObjectName("btn_show_password")
        self.btn_execute = QtWidgets.QPushButton(self.centralwidget)
        self.btn_execute.setGeometry(QtCore.QRect(10, 360, 481, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_execute.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/database_go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_execute.setIcon(icon2)
        self.btn_execute.setObjectName("btn_execute")
        FormBackup.setCentralWidget(self.centralwidget)

        self.retranslateUi(FormBackup)
        QtCore.QMetaObject.connectSlotsByName(FormBackup)

    def retranslateUi(self, FormBackup):
        _translate = QtCore.QCoreApplication.translate
        FormBackup.setWindowTitle(_translate("FormBackup", "GERENCIADOR DE BACKUPS"))
        self.groupBox.setTitle(_translate("FormBackup", "OPERAÇÃO"))
        self.radio_export.setText(_translate("FormBackup", "EXPORTAR Dados"))
        self.radio_import.setText(_translate("FormBackup", "IMPORTAR Dados"))
        self.groupBox_2.setTitle(_translate("FormBackup", "AUTENTICAÇÃO"))
        self.label.setText(_translate("FormBackup", "USUÁRIO"))
        self.label_2.setText(_translate("FormBackup", "SENHA"))
        self.btn_execute.setText(_translate("FormBackup", "EXECUTAR TRANSAÇÃO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormBackup = QtWidgets.QMainWindow()
    ui = Ui_FormBackup()
    ui.setupUi(FormBackup)
    FormBackup.show()
    sys.exit(app.exec_())
