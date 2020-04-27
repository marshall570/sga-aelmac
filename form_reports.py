# -*- coding: utf-8 -*-
import tkinter
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
from dao_assisted import DAOAssisted

dao_assisted = DAOAssisted()

class Ui_FormReports(object):
    selected_filter = 'Nome'
    custom_sql = ''   
   
    def cmb_filter_changed(self):
        self.model.removeRows(0, self.model.rowCount())                               
        self.txt_filter.setText('')
        self.btn_search.setEnabled(True)        
        self.btn_export.setEnabled(False)
        
        if self.cmb_filter.currentText() == 'Nome':
            self.txt_filter.setEnabled(True)
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Nome'
        elif self.cmb_filter.currentText() == 'Data de Nascimento':
            self.txt_filter.setEnabled(True)
            self.txt_filter.setInputMask('##/##/####')
            self.selected_filter = 'Data_de_nascimento'
        elif self.cmb_filter.currentText() == 'Telefone (Celular)':
            self.txt_filter.setEnabled(True)
            self.txt_filter.setInputMask('(##) #####-####')
            self.selected_filter = 'Telefone_1'
        elif self.cmb_filter.currentText() == 'Telefone (Residencial)':
            self.txt_filter.setEnabled(True)
            self.txt_filter.setInputMask('(##) ####-####')
            self.selected_filter = 'Telefone_2'
        elif self.cmb_filter.currentText() == 'Gênero':
            self.txt_filter.setEnabled(True)
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Genero'
        elif self.cmb_filter.currentText() == 'Endereço':
            self.txt_filter.setEnabled(True)
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Endereco'
        elif self.cmb_filter.currentText() == 'Bairro':
            self.txt_filter.setEnabled(True)
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Bairro'
        elif self.cmb_filter.currentText() == 'Cidade':
            self.txt_filter.setEnabled(True)
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Cidade'
        else:
            self.txt_filter.setEnabled(False)            
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Ultimo_tratamento'

    def btn_search_clicked(self):
        if self.selected_filter != 'Ultimo_tratamento' and len(self.txt_filter.text().strip()) < 1:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', 'Preencha os campos corretamente para pesquisar')
            tkinter.Tk().destroy()
        else:
            value = ''            
            
            if self.selected_filter != 'Ultimo_tratamento':
                value = self.txt_filter.text().strip().upper()
            else:
                if self.cmb_filter.currentText() == 'Tratamento: HL':
                    value = 'HL'
                elif self.cmb_filter.currentText() == 'Tratamento: P1/2':
                    value = 'P1/2'
                elif self.cmb_filter.currentText() == 'Tratamento: P3E':
                    value = 'P3E'
                else:
                    value = 'P3F'
            
            count_sql = "SELECT COUNT(*) FROM tb_assistidos WHERE {} LIKE '%{}%'".format(self.selected_filter, value)
            self.custom_sql = "SELECT * FROM tb_assistidos WHERE {} LIKE '%{}%'".format(self.selected_filter, value)
            
            if dao_assisted.count_custom_search(count_sql) < 1:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showinfo('RESULTADO NÃO ENCONTRADO', 'Não foram encontrados resultados com os filtros especificados.\nTente novamente com outros filtros.')
                tkinter.Tk().destroy()
            else:
                self.model.removeRows(0, self.model.rowCount())                
                query_result = dao_assisted.custom_search(self.custom_sql)
                
                for value in query_result:
                    row = []
                    for item in value:
                        cell = QtGui.QStandardItem(str(item))
                        row.append(cell)
                    self.model.appendRow(row)
                    
                self.btn_export.setEnabled(True)
                
    def btn_export_clicked(self):
        dao_assisted.gen_custom_csv(self.custom_sql, self.selected_filter)
            
    
    def setupUi(self, FormReports):
        FormReports.setObjectName("FormReports")
        FormReports.resize(650, 450)
        FormReports.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/aelmac_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormReports.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormReports)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 631, 101))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.txt_filter = QtWidgets.QLineEdit(self.groupBox)
        self.txt_filter.setGeometry(QtCore.QRect(20, 45, 361, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setWeight(50)
        self.txt_filter.setFont(font)
        self.txt_filter.setObjectName("txt_filter")
        self.cmb_filter = QtWidgets.QComboBox(self.groupBox)
        self.cmb_filter.setGeometry(QtCore.QRect(406, 45, 201, 32))        
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setWeight(50)
        self.cmb_filter.setFont(font)
        self.cmb_filter.setObjectName("cmb_filter")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.addItem("")
        self.cmb_filter.currentIndexChanged.connect(self.cmb_filter_changed)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 631, 281))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tb_results = QtWidgets.QTableView(self.groupBox_2)
        self.tb_results.setGeometry(QtCore.QRect(10, 30, 611, 241))
        self.model = QtGui.QStandardItemModel(self.groupBox_2)
        self.model.setHorizontalHeaderLabels(['ID', 'NOME', 'DATA DE NASCIMENTO', 'TELEFONE (CELULAR)', 'TELEFONE (RESIDENCIAL)', 'GÊNERO', 'ESTADO CIVIL', 'OCUPAÇÃO', 'RESIDE COM', 'ENDEREÇO', 'BAIRRO', 'NÚMERO', 'CIDADE', 'ESTADO', 'TOMA SEDATIVOS?', 'TRATAMENTO MÉDICO?', 'DROME BEM?', 'VÍCIOS', 'SONHOS', 'TRABALHO', 'FAMÍLIA', 'ALIMENTAÇÃO', 'INFO PARA O DEPOE', 'ÚLTIMO TRATAMENTO', 'CURSOS E FREQUÊNCIA', 'ENCAMINHAMENTO', 'TRATAMENTOS', 'ORIENTAÇÃO ESPIRITUAL'])
        self.tb_results.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_results.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_results.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tb_results.setModel(self.model)        
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tb_results.setFont(font)
        self.tb_results.setObjectName("tb_results")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(10, 410, 300, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setObjectName("btn_search")
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export.setGeometry(QtCore.QRect(340, 410, 300, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.btn_export.setFont(font)
        self.btn_export.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/page_excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_export.setIcon(icon1)
        self.btn_export.setObjectName("btn_export")
        self.btn_export.clicked.connect(self.btn_export_clicked)
        FormReports.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(FormReports)
        QtCore.QMetaObject.connectSlotsByName(FormReports)

    def retranslateUi(self, FormReports):
        _translate = QtCore.QCoreApplication.translate
        FormReports.setWindowTitle(_translate("FormReports", "GERENCIADOR DE RELATÓRIOS"))
        self.groupBox.setTitle(_translate("FormReports", "FILTRO"))
        self.cmb_filter.setItemText(0, _translate("FormReports", "Nome"))
        self.cmb_filter.setItemText(1, _translate("FormReports", "Data de Nascimento"))
        self.cmb_filter.setItemText(2, _translate("FormReports", "Telefone (Celular)"))
        self.cmb_filter.setItemText(3, _translate("FormReports", "Telefone (Residencial)"))
        self.cmb_filter.setItemText(4, _translate("FormReports", "Gênero"))
        self.cmb_filter.setItemText(5, _translate("FormReports", "Endereço"))
        self.cmb_filter.setItemText(6, _translate("FormReports", "Bairro"))
        self.cmb_filter.setItemText(7, _translate("FormReports", "Cidade"))
        self.cmb_filter.setItemText(8, _translate("FormReports", "Tratamento: HL"))
        self.cmb_filter.setItemText(9, _translate("FormReports", "Tratamento: P1/2"))
        self.cmb_filter.setItemText(10, _translate("FormReports", "Tratamento: P3E"))
        self.cmb_filter.setItemText(11, _translate("FormReports", "Tratamento: P3F"))
        self.groupBox_2.setTitle(_translate("FormReports", "RESULTADOS"))
        self.btn_search.setText(_translate("FormReports", "PESQUISAR"))
        self.btn_export.setText(_translate("FormReports", "EXPORTAR RESULTADOS PARA EXCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormReports = QtWidgets.QMainWindow()
    ui = Ui_FormReports()
    ui.setupUi(FormReports)
    FormReports.show()
    sys.exit(app.exec_())
