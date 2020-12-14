# -*- coding: utf-8 -*-
import tkinter
import platform
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
from LoginController import LoginController

controller = LoginController()


class Ui_FrameLogin(object):
    password_visible = False

    def btn_show_password_clicked(self):
        if self.password_visible:
            self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
            new_icon = QtGui.QIcon.fromTheme("hint")
            self.btn_show_password.setIcon(new_icon)
            self.password_visible = False

        else:
            self.txt_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            new_icon = QtGui.QIcon.fromTheme("view-hidden")
            self.btn_show_password.setIcon(new_icon)
            self.password_visible = True

    def btn_signin_clicked(self):
        this_window = QtWidgets.QApplication.activeWindow()

        if controller.count_user(self.txt_user.text().strip()) < 1:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror(
                'ERRO', 'O Usuário não existe no banco de dados.')
            tkinter.Tk().destroy()

        else:
            if len(self.txt_password.text()) < 1:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror('ERRO', 'A senha não pode estar vazia.')
                tkinter.Tk().destroy()

            else:
                if not controller.check_password(self.txt_user.text(), self.txt_password.text()):
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showerror(
                        'ERRO', f'Senha incorreta para o usuário <{self.txt_user.text()}>')
                    tkinter.Tk().destroy()

                else:
                    from assisted import Ui_FormFicha
                    controller.set_on(self.txt_user.text())
                    this_window.close()
                    self.FormFicha = QtWidgets.QMainWindow()
                    self.ui = Ui_FormFicha()
                    self.ui.setupUi(self.FormFicha)
                    self.FormFicha.showFullScreen()

    def btn_create_user_clicked(self):
        this_window = QtWidgets.QApplication.activeWindow()
        from signup import Ui_FormSignUp
        this_window.close()
        self.FormSignUp = QtWidgets.QMainWindow()
        self.ui = Ui_FormSignUp()
        self.ui.setupUi(self.FormSignUp)
        self.FormSignUp.show()

    def setupUi(self, FrameLogin):
        FrameLogin.setObjectName("FrameLogin")
        FrameLogin.resize(650, 250)
        FrameLogin.setMaximumSize(QtCore.QSize(650, 250))
        FrameLogin.setWindowTitle("GERENCIAMENTO DE ASSISTIDOS - LOGIN")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/aelmac_white_16.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameLogin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FrameLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 630, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("SISTEMA DE GERENCIAMENTO DE ASSISTIDOS")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 57, 631, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("USUÁRIO")
        self.label_2.setObjectName("label_2")
        self.txt_user = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_user.setGeometry(QtCore.QRect(10, 85, 631, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_user.setFont(font)
        self.txt_user.setInputMask("")
        self.txt_user.setText("")
        self.txt_user.setObjectName("txt_user")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 122, 631, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("SENHA")
        self.label_3.setObjectName("label_3")
        self.txt_password = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_password.setGeometry(QtCore.QRect(10, 150, 601, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
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
        self.btn_create_user.setText("CRIAR USUÁRIO")
        icon = QtGui.QIcon.fromTheme("list-add-user")
        self.btn_create_user.setIcon(icon)
        self.btn_create_user.setObjectName("btn_create_user")
        self.btn_create_user.clicked.connect(self.btn_create_user_clicked)
        self.btn_signin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signin.setGeometry(QtCore.QRect(510, 205, 131, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.btn_signin.setFont(font)
        self.btn_signin.setText("ENTRAR")
        icon = QtGui.QIcon.fromTheme("mail-forwarded")
        self.btn_signin.setIcon(icon)
        self.btn_signin.setObjectName("btn_signin")
        self.btn_signin.clicked.connect(self.btn_signin_clicked)
        self.btn_show_password = QtWidgets.QPushButton(self.centralwidget)
        self.btn_show_password.setGeometry(QtCore.QRect(610, 150, 35, 32))
        self.btn_show_password.setText("")
        icon = QtGui.QIcon.fromTheme("hint")
        self.btn_show_password.setIcon(icon)
        self.btn_show_password.setIconSize(QtCore.QSize(24, 24))
        self.btn_show_password.setFlat(True)
        self.btn_show_password.setObjectName("btn_show_password")
        self.btn_show_password.clicked.connect(self.btn_show_password_clicked)
        FrameLogin.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(FrameLogin)
        FrameLogin.setTabOrder(self.txt_user, self.txt_password)
        FrameLogin.setTabOrder(self.txt_password, self.btn_show_password)
        FrameLogin.setTabOrder(self.btn_show_password, self.btn_signin)
        FrameLogin.setTabOrder(self.btn_signin, self.btn_create_user)

        if platform.system() == 'Linux':
            if not os.path.exists(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC'):
                os.mkdir(os.path.expanduser("~") +
                         '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC')

            if not os.path.exists(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/RELATORIOS_EXCEL'):
                os.mkdir(os.path.expanduser(
                    "~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/RELATORIOS_EXCEL')

            if not os.path.exists(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/FICHAS_INDIVIDUAIS'):
                os.mkdir(os.path.expanduser(
                    "~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/FICHAS_INDIVIDUAIS')

            if not os.path.exists(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/BACKUPS'):
                os.mkdir(os.path.expanduser(
                    "~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/BACKUPS')

        else:
            if not os.path.exists(os.path.expanduser("~") + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC'):
                os.mkdir(os.path.expanduser("~") +
                         '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC')

            if not os.path.exists(os.path.expanduser("~") + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\RELATORIOS_EXCEL'):
                os.mkdir(os.path.expanduser(
                    "~") + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\RELATORIOS_EXCEL')

            if not os.path.exists(os.path.expanduser("~") + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\FICHAS_INDIVIDUAIS'):
                os.mkdir(os.path.expanduser(
                    "~") + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\FICHAS_INDIVIDUAIS')

            if not os.path.exists(os.path.expanduser("~") + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\BACKUPS'):
                os.mkdir(os.path.expanduser(
                    "~") + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\BACKUPS')


if __name__ == "__main__":
    import sys
    controller.create_tables()
    controller.set_off()
    app = QtWidgets.QApplication(sys.argv)
    FrameLogin = QtWidgets.QMainWindow()
    ui = Ui_FrameLogin()
    ui.setupUi(FrameLogin)
    FrameLogin.show()
    sys.exit(app.exec_())
