# -*- coding: utf-8 -*-
import tkinter
from PyQt5 import QtCore, QtGui, QtWidgets
from dto_user import User
from dao_user import DAOUser
from tkinter import messagebox

u = User()
dao = DAOUser()

class Ui_FormSignUp(object):
    password_visible = False
    confirm_visible = False
    password_matches = False
    strength = 0
    
    def btn_show_password_clicked(self):
        if self.password_visible is True:
            self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/EnablePassword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_show_password.setIcon(icon)
            self.password_visible = False
        else:
            self.txt_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/DisablePassword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_show_password.setIcon(icon)
            self.password_visible = True 

    def btn_show_confirm_clicked(self):
        if self.confirm_visible is True:
            self.txt_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/EnablePassword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_show_confirm.setIcon(icon)
            self.confirm_visible = False
        else:
            self.txt_confirm.setEchoMode(QtWidgets.QLineEdit.Normal)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/DisablePassword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_show_confirm.setIcon(icon)
            self.confirm_visible = True 
    
    def check_password_strength(self):
        import re
        
        if len(self.txt_password.text().strip()) < 8 or self.txt_password.text().strip() == self.txt_name.text().strip() or self.txt_password.text().strip() == self.txt_user.text().strip():
            self.strength = 0
        elif len(self.txt_password.text().strip()) >= 8:
            self.strength = 1
        elif len(self.txt_password.text().strip()) >= 10:
            self.strength = 2
            
        if re.search(r"\d", self.txt_password.text().strip()):
            self.strength += 2
            
        if re.search(r"[a-z]", self.txt_password.text().strip()):
            self.strength += 2
            
        if re.search(r"[A-Z]", self.txt_password.text().strip()):
            self.strength += 2
        
        if re.search(r"\W", self.txt_password.text().strip()):
            self.strength += 2
            
        if self.strength < 2:
            self.lbl_strength.setText('FORÇA DA SENHA: MUITO FRACA')
        elif self.strength <= 4:
            self.lbl_strength.setText('FORÇA DA SENHA: FRACA')
        elif self.strength <= 5:
            self.lbl_strength.setText('FORÇA DA SENHA: ACEITÁVEL')
        elif self.strength <= 8:
            self.lbl_strength.setText('FORÇA DA SENHA: FORTE')
        else:
            self.lbl_strength.setText('FORÇA DA SENHA: MUITO FORTE')            
        self.check_password_matches()  
    
    def check_password_matches(self):
        if self.txt_confirm.text() != self.txt_password.text():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            icon.addPixmap(QtGui.QPixmap("images/cancel.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
            icon.addPixmap(QtGui.QPixmap("images/cancel.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
            self.btn_check.setIcon(icon)
            return False
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/accept.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            icon.addPixmap(QtGui.QPixmap("images/accept.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
            icon.addPixmap(QtGui.QPixmap("images/accept.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
            self.btn_check.setIcon(icon)
            return True          
        
    def btn_signup_clicked(self):
        this_window = QtWidgets.QApplication.activeWindow()
        if len(self.txt_password.text()) < 1:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('AÇÃO NÃO PERMITIDA', 'A senha está não pode estar vazia.')
            tkinter.Tk().destroy()
        else:
            if not self.check_password_matches():
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror('AÇÃO NÃO PERMITIDA', 'As senhas não estão iguais.')
                tkinter.Tk().destroy()
            else:
                u.name = self.txt_name.text().strip().title()
                u.user = self.txt_user.text().strip()
                u.password = self.txt_password.text().strip()
                u.category = self.cmb_category.currentText()
                if dao.register_count_user(u) > 0:
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showerror('AÇÃO NÃO PERMITIDA', 'O usuário já está cadastrado no banco de dados. Tente outro nome de usuário.')
                    tkinter.Tk().destroy()
                else:
                    if self.lbl_strength.text().endswith('MUITO FRACA'):
                        root = tkinter.Tk()
                        root.withdraw()
                        messagebox.showerror('AÇÃO NÃO PERMITIDA', 'A senha inserida é MUITO FRACA, insira uma senha mais forte para efetuar o cadastro.')
                        tkinter.Tk().destroy()
                    else:
                        if self.lbl_strength.text().endswith('FRACA') and self.cmb_category.currentText() == 'ADMINISTRADOR':            
                            root = tkinter.Tk()
                            root.withdraw()
                            messagebox.showerror('AÇÃO NÃO PERMITIDA', 'Usuário com categoria ADMINISTRADOR necessita senha com força ACEITÁVEL ou maior')
                            tkinter.Tk().destroy()
                        elif self.lbl_strength.text().endswith('FRACA') and self.cmb_category.currentText() != 'ADMINISTRADOR':
                            root = tkinter.Tk()
                            root.withdraw()
                            choice = messagebox.askquestion('ATENÇÃO', 'Deseja criar usuário com uma senha FRACA?')
                            tkinter.Tk().destroy()
                            
                            if choice == 'yes':
                                u.code = dao.id_gen_user()
                                dao.insert_user(u)
                                root = tkinter.Tk()
                                root.withdraw()
                                
                                choice = messagebox.askquestion('ATENÇÃO', 'Deseja voltar para a TELA DE LOGIN?')
                                tkinter.Tk().destroy()
                                
                                if choice == 'yes':
                                    from form_login import Ui_FormLogin                                    
                                    this_window.close()
                                    self.FormLogin = QtWidgets.QMainWindow()
                                    self.ui = Ui_FormLogin()
                                    self.ui.setupUi(self.FormLogin)
                                    self.FormLogin.show()
                        else:
                            u.code = dao.id_gen_user()
                            dao.insert_user(u)    
                            choice = messagebox.askquestion('ATENÇÃO', 'Deseja voltar para a TELA DE LOGIN?')
                            tkinter.Tk().destroy()
                                
                            if choice == 'yes':
                                from form_login import Ui_FormLogin
                                this_window.close()
                                self.FormLogin = QtWidgets.QMainWindow()
                                self.ui = Ui_FormLogin()
                                self.ui.setupUi(self.FormLogin)
                                self.FormLogin.show()
    
    
    def setupUi(self, FormSignUp):
        FormSignUp.setObjectName("FormSignUp")
        FormSignUp.resize(500, 545)
        FormSignUp.setMaximumSize(QtCore.QSize(500, 545))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/aelmac_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormSignUp.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormSignUp)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(10, 85, 480, 32))
        self.txt_name.setObjectName("txt_name")
        self.txt_user = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_user.setGeometry(QtCore.QRect(10, 165, 480, 32))
        self.txt_user.setObjectName("txt_user")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_password = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setGeometry(QtCore.QRect(10, 245, 451, 32))
        self.txt_password.setObjectName("txt_password")
        self.txt_password.textChanged.connect(self.check_password_strength)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btn_show_password = QtWidgets.QPushButton(self.centralwidget)
        self.btn_show_password.setGeometry(QtCore.QRect(460, 245, 32, 32))
        self.btn_show_password.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/EnablePassword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_show_password.setIcon(icon1)
        self.btn_show_password.setFlat(True)
        self.btn_show_password.setObjectName("btn_show_password")
        self.btn_show_password.clicked.connect(self.btn_show_password_clicked)
        self.lbl_strength = QtWidgets.QLabel(self.centralwidget)
        self.lbl_strength.setGeometry(QtCore.QRect(10, 280, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        self.lbl_strength.setFont(font)
        self.lbl_strength.setObjectName("lbl_strength")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 250, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btn_show_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_show_confirm.setGeometry(QtCore.QRect(460, 345, 32, 32))
        self.btn_show_confirm.setText("")
        self.btn_show_confirm.setIcon(icon1)
        self.btn_show_confirm.setFlat(True)
        self.btn_show_confirm.setObjectName("btn_show_confirm")
        self.btn_show_confirm.clicked.connect(self.btn_show_confirm_clicked)
        self.txt_confirm = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_confirm.setGeometry(QtCore.QRect(10, 345, 451, 32))
        self.txt_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_confirm.setObjectName("txt_confirm")
        self.txt_confirm.textEdited.connect(self.check_password_matches)
        self.btn_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check.setGeometry(QtCore.QRect(130, 320, 21, 21))
        self.btn_check.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("images/cancel.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("images/cancel.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.btn_check.setIcon(icon2)
        self.btn_check.setEnabled(False)
        self.btn_check.setFlat(True)
        self.btn_check.setObjectName("btn_check")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 400, 135, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cmb_category = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_category.setGeometry(QtCore.QRect(10, 425, 481, 32))
        self.cmb_category.setObjectName("cmb_category")
        self.cmb_category.addItem("")
        self.cmb_category.addItem("")
        self.btn_signup = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signup.setGeometry(QtCore.QRect(270, 490, 220, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_signup.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/vcard_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_signup.setIcon(icon3)
        self.btn_signup.setObjectName("btn_signup")
        self.btn_signup.clicked.connect(self.btn_signup_clicked)
        FormSignUp.setCentralWidget(self.centralwidget)

        self.retranslateUi(FormSignUp)
        QtCore.QMetaObject.connectSlotsByName(FormSignUp)
        FormSignUp.setTabOrder(self.txt_name, self.txt_user)
        FormSignUp.setTabOrder(self.txt_user, self.txt_password)
        FormSignUp.setTabOrder(self.txt_password, self.btn_show_password)
        FormSignUp.setTabOrder(self.btn_show_password, self.txt_confirm)
        FormSignUp.setTabOrder(self.txt_confirm, self.btn_show_confirm)
        FormSignUp.setTabOrder(self.btn_show_confirm, self.cmb_category)
        FormSignUp.setTabOrder(self.cmb_category, self.btn_signup)
        FormSignUp.setTabOrder(self.btn_signup, self.btn_check)

    def retranslateUi(self, FormSignUp):
        _translate = QtCore.QCoreApplication.translate
        FormSignUp.setWindowTitle(_translate("FormSignUp", "CADASTRO DE USUÁRIO"))
        self.label.setText(_translate("FormSignUp", "CADASTRO DE USUÁRIO"))
        self.label_2.setText(_translate("FormSignUp", "NOME"))
        self.label_3.setText(_translate("FormSignUp", "USUÁRIO"))
        self.label_4.setText(_translate("FormSignUp", "SENHA"))
        self.lbl_strength.setText(_translate("FormSignUp", "FORÇA DA SENHA: MUITO FRACA"))
        self.label_6.setText(_translate("FormSignUp", "CONFIRMAR SENHA"))
        self.label_7.setText(_translate("FormSignUp", "CATEGORIA"))
        self.cmb_category.setItemText(0, _translate("FormSignUp", "COMUM"))
        self.cmb_category.setItemText(1, _translate("FormSignUp", "ADMINISTRADOR"))
        self.btn_signup.setText(_translate("FormSignUp", "CADASTRAR USUÁRIO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSignUp = QtWidgets.QMainWindow()
    ui = Ui_FormSignUp()
    ui.setupUi(FormSignUp)
    FormSignUp.show()
    sys.exit(app.exec_())
