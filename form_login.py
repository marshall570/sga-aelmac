# -*- coding: utf-8 -*-
import tkinter
from PyQt5 import QtCore, QtGui, QtWidgets
from dto_user import User
from tkinter import messagebox
from dao_user import DAOUser
from dao_assisted import DAOAssisted
from dao_interview import DAOInterview

dao_user = DAOUser()
dao_assisted = DAOAssisted()
dao_interview = DAOInterview()
u = User()

class Ui_FormLogin(object):
    password_visible = False

    def btn_show_password_clicked(self):
        if self.password_visible is True:
            self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/eye-off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_show_password.setIcon(icon)
            self.password_visible = False
        else:
            self.txt_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_show_password.setIcon(icon)
            self.password_visible = True

    def btn_signin_clicked(self):
        this_window = QtWidgets.QApplication.activeWindow()        
        u.user = self.txt_user.text().strip()

        if dao_user.register_count_user(u) < 1:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', 'O Usuário não existe no banco de dados.')
            tkinter.Tk().destroy()
        else:
            u.password = self.txt_password.text()
            if len(u.password) < 1:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror('ERRO', 'A senha não pode estar vazia.')
                tkinter.Tk().destroy()
            else:    
                if dao_user.check_password(u) != u.password:
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showerror('ERRO', 'Senha incorreta para o usuário <{}>'.format(u.user))
                    tkinter.Tk().destroy()
                else:
                    from form_assisted import Ui_FormFicha                    
                    dao_user.set_on(u)
                    this_window.close()
                    self.FormFicha = QtWidgets.QMainWindow()
                    self.ui = Ui_FormFicha()
                    self.ui.setupUi(self.FormFicha)
                    self.FormFicha.show()

    def btn_create_user_clicked(self):
        this_window = QtWidgets.QApplication.activeWindow()        
        from form_sign_up import UiFormSignUp
        this_window.close()     
        self.FormSignUp = QtWidgets.QMainWindow()
        self.ui = UiFormSignUp()
        self.ui.setupUi(self.FormSignUp)
        self.FormSignUp.show()


    def setupUi(self, FormLogin):
        FormLogin.setObjectName("FormLogin")
        FormLogin.resize(650, 250)
        FormLogin.setMaximumSize(QtCore.QSize(650, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/aelmac_white.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormLogin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 630, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 57, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_user = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_user.setGeometry(QtCore.QRect(10, 85, 631, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.txt_user.setFont(font)
        self.txt_user.setObjectName("txt_user")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 122, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_password = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_password.setGeometry(QtCore.QRect(10, 150, 601, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.txt_password.setFont(font)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.btn_create_user = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create_user.setGeometry(QtCore.QRect(10, 205, 151, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.btn_create_user.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/user-check.svg"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_create_user.setIcon(icon1)
        self.btn_create_user.setObjectName("btn_create_user")
        self.btn_create_user.clicked.connect(self.btn_create_user_clicked)
        self.btn_signin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signin.setGeometry(QtCore.QRect(510, 205, 131, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.btn_signin.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/arrow-right-circle.svg"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_signin.setIcon(icon2)
        self.btn_signin.setObjectName("btn_signin")
        self.btn_signin.clicked.connect(self.btn_signin_clicked)
        self.btn_show_password = QtWidgets.QPushButton(self.centralwidget)
        self.btn_show_password.setGeometry(QtCore.QRect(610, 150, 35, 32))
        self.btn_show_password.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/eye-off.svg"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_show_password.setIcon(icon3)
        self.btn_show_password.setIconSize(QtCore.QSize(24, 24))
        self.btn_show_password.setFlat(True)
        self.btn_show_password.setObjectName("btn_show_password")
        self.btn_show_password.clicked.connect(self.btn_show_password_clicked)
        FormLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(FormLogin)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)
        FormLogin.setTabOrder(self.txt_user, self.txt_password)
        FormLogin.setTabOrder(self.txt_password, self.btn_show_password)
        FormLogin.setTabOrder(self.btn_show_password, self.btn_signin)
        FormLogin.setTabOrder(self.btn_signin, self.btn_create_user)

    def retranslateUi(self, FormLogin):
        _translate = QtCore.QCoreApplication.translate
        FormLogin.setWindowTitle(_translate("FormLogin", "GERENCIAMENTO DE ASSISTIDOS - LOGIN"))
        self.label.setText(_translate("FormLogin", "SISTEMA DE GERENCIAMENTO DE ASSISTIDOS"))
        self.label_2.setText(_translate("FormLogin", "USUÁRIO"))
        self.label_3.setText(_translate("FormLogin", "SENHA"))
        self.btn_create_user.setText(_translate("FormLogin", "CRIAR USUÁRIO"))
        self.btn_signin.setText(_translate("FormLogin", "ENTRAR"))


if __name__ == "__main__":
    import sys
    dao_assisted.create_table_assisted()
    dao_assisted.create_files_directory()
    dao_interview.create_table_interview()
    dao_user.create_table_user()
    dao_user.create_table_changes()
    dao_user.set_off()
    app = QtWidgets.QApplication(sys.argv)
    FormLogin = QtWidgets.QMainWindow()
    ui = Ui_FormLogin()
    ui.setupUi(FormLogin)
    FormLogin.show()
    sys.exit(app.exec_())
