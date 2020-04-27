# -*- coding: utf-8 -*-
import tkinter
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
from dao_assisted import DAOAssisted
from dao_user import DAOUser

dao_assisted = DAOAssisted()
dao_user = DAOUser()

class Ui_FormBackup(object):
    password_visible = False

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
        
    def btn_execute_clicked(self):
        this_window = QtWidgets.QApplication.activeWindow()        
        user = self.txt_user.text().strip()
        password = self.txt_password.text().strip()        
        
        if dao_user.count_user(user) < 1:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', 'ERRO!!! O Usuário informado não existe.\nTente outro usuário')
            tkinter.Tk().destroy()
        else:       
            historic_message = ''     
            active_user = dao_user.select_active_user()
            
            if self.radio_export.isChecked():
                if password == dao_user.select_user(user)[1]:
                    if user == active_user[1]:
                        historic_message = 'EXPORTOU dados utilizando o próprio login'
                    else:
                        historic_message = f'EXPORTOU dados utilizando o login <{user}>'
                        
                    dao_assisted.export_data()
                    dao_user.register_changes(active_user[0], historic_message)
                    this_window.close()
                else:
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showerror('ERRO', 'ERRO!!! A senha para o usuário <{}> está incorreta'.format(user))
                    tkinter.Tk().destroy()                    
            else:                             
                if dao_user.select_user(user)[2] != 'ADMINISTRADOR':
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showerror('ERRO', 'ERRO!!! Apenas usuários com categoria ADMINISTRADOR podem IMPORTAR dados.\nInsira um usuário com a categoria de <ADMINISTRADOR> e tente novamente.')
                    tkinter.Tk().destroy()
                else:                    
                    if password == dao_user.select_user(user)[1]:
                        import platform
                        import os
                        path = ''
                                                
                        if platform.system() == 'Linux':
                            path = os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/BACKUPS/'
                        else:
                            path = os.path.expanduser("~") + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\BACKUPS\\'
                            
                        dialog = QtWidgets.QFileDialog()        
                        file = dialog.getOpenFileName(dialog, 'Selecionar arquivo de backup', path, 'Arquivo de Banco de Dados (*.db)')    
                                                
                        if file[0] != '':
                            root = tkinter.Tk()
                            root.withdraw()
                            choice = messagebox.askquestion('ATENÇÃO', 'Ao confirmar esta ação, TODOS os dados salvos anteriormente serão substituidos.\nDeseja continuar?')
                            tkinter.Tk().destroy()
                            
                            if choice == 'yes':                            
                                if user == active_user[1]:
                                    historic_message = 'IMPORTOU dados utilizando o próprio login'
                                else:
                                    historic_message = f'IMPORTOU dados utilizando o login de {active_user[0]}'                            

                                dao_user.register_changes(active_user[0], historic_message)
                                dao_user.gen_historic()
                                dao_assisted.import_data(file[0])
                                QtWidgets.QApplication.quit()
                    else:
                        root = tkinter.Tk()
                        root.withdraw()
                        messagebox.showerror('ERRO', 'ERRO!!! A senha para o usuário <{}> está incorreta'.format(user))
                        tkinter.Tk().destroy()                                                                                         
    
 
    
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
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(50)
        self.radio_export = QtWidgets.QRadioButton(self.groupBox)
        self.radio_export.setGeometry(QtCore.QRect(36, 60, 171, 22))
        self.radio_export.setObjectName("radio_export")
        self.radio_export.setEnabled(False)
        self.radio_export.setFont(font)
        self.radio_import = QtWidgets.QRadioButton(self.groupBox)
        self.radio_import.setGeometry(QtCore.QRect(280, 60, 161, 22))
        self.radio_import.setObjectName("radio_import")
        self.radio_import.setEnabled(False)
        self.radio_import.setFont(font)
        self.radio_import.toggle()
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 481, 211))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
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
        font.setPixelSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_user.setFont(font)
        self.txt_user.setObjectName("txt_user")
        self.txt_password = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_password.setGeometry(QtCore.QRect(15, 150, 410, 32))
        font = QtGui.QFont()
        font.setPixelSize(11)
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
        self.btn_show_password.clicked.connect(self.btn_show_password_clicked)
        self.btn_execute = QtWidgets.QPushButton(self.centralwidget)
        self.btn_execute.setGeometry(QtCore.QRect(10, 360, 481, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_execute.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/database_go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_execute.setIcon(icon2)
        self.btn_execute.setObjectName("btn_execute")
        self.btn_execute.clicked.connect(self.btn_execute_clicked)
        FormBackup.setCentralWidget(self.centralwidget)    
        
        if dao_assisted.id_gen_assisted() - 1 < 1:
            self.radio_export.setEnabled(False)
            self.radio_import.setEnabled(True)
        else:
            self.radio_export.setEnabled(True)
            self.radio_import.setEnabled(True)             
        
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
