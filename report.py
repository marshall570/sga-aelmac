# -*- coding: utf-8 -*-
import tkinter
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
from AssistedController import AssistedController

controller = AssistedController()


class Ui_FormReports(object):
    selected_filter = 'Nome'
    custom_sql = ''

    def cmb_filter_changed(self):
        self.model.removeRows(0, self.model.rowCount())
        self.txt_filter.setText('')
        self.btn_search.setEnabled(True)
        self.btn_export.setEnabled(False)

        if self.cmb_filter.currentText() == 'Nome':
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Nome'
        elif self.cmb_filter.currentText() == 'Data de Nascimento':
            self.txt_filter.setInputMask('##/##/####')
            self.selected_filter = 'Data_de_nascimento'
        elif self.cmb_filter.currentText() == 'Telefone':
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Telefone'
        elif self.cmb_filter.currentText() == 'Gênero':
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Genero'
        elif self.cmb_filter.currentText() == 'Endereço':
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Endereco'
        elif self.cmb_filter.currentText() == 'Bairro':
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Bairro'
        elif self.cmb_filter.currentText() == 'Cidade':
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Cidade'
        else:
            self.txt_filter.setInputMask('')
            self.selected_filter = 'Ultimo_tratamento'

    def btn_search_clicked(self):
        if len(self.txt_filter.text().strip()) < 1:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror(
                'ERRO', 'Preencha os campos corretamente para pesquisar')
            tkinter.Tk().destroy()
        else:
            value = self.txt_filter.text().strip().upper()
            
            count_sql = f'SELECT COUNT(*) FROM tb_assistidos WHERE {self.selected_filter} LIKE \'%{value}%\''
            self.custom_sql = f'SELECT * FROM tb_assistidos WHERE {self.selected_filter} LIKE \'%{value}%\''

            if controller.count_custom_search(count_sql) < 1:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showinfo(
                    'RESULTADO NÃO ENCONTRADO', 'Não foram encontrados resultados com os filtros especificados.\nTente novamente com outros filtros.')
                tkinter.Tk().destroy()
            else:
                self.model.removeRows(0, self.model.rowCount())
                query_result = controller.custom_search(self.custom_sql)

                for value in query_result:
                    row = []
                    for item in value:
                        cell = QtGui.QStandardItem(str(item))
                        row.append(cell)
                    self.model.appendRow(row)

                self.btn_export.setEnabled(True)

    def btn_export_clicked(self):
        controller.gen_custom_csv(self.custom_sql, self.selected_filter)

    def setupUi(self, FormReports):
        FormReports.setObjectName("FormReports")
        FormReports.resize(650, 450)
        FormReports.setMaximumSize(QtCore.QSize(650, 450))
        FormReports.setWindowTitle("GERENCIADOR DE RELATÓRIOS")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/aelmac_white_16.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormReports.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FormReports)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("FILTRO")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txt_filter = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txt_filter.setFont(font)
        self.txt_filter.setInputMask("")
        self.txt_filter.setText("")
        self.txt_filter.setObjectName("txt_filter")
        self.gridLayout_2.addWidget(self.txt_filter, 0, 0, 1, 1)
        self.cmb_filter = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cmb_filter.setFont(font)
        self.cmb_filter.setCurrentText("Nome")
        self.cmb_filter.setObjectName("cmb_filter")
        self.cmb_filter.addItem("")
        self.cmb_filter.setItemText(0, "Nome")
        self.cmb_filter.addItem("")
        self.cmb_filter.setItemText(1, "Data de Nascimento")
        self.cmb_filter.addItem("")
        self.cmb_filter.setItemText(2, "Telefone")
        self.cmb_filter.addItem("")
        self.cmb_filter.setItemText(3, "Gênero")
        self.cmb_filter.addItem("")
        self.cmb_filter.setItemText(4, "Endereço")
        self.cmb_filter.addItem("")
        self.cmb_filter.setItemText(5, "Bairro")
        self.cmb_filter.addItem("")
        self.cmb_filter.setItemText(6, "Cidade")
        self.cmb_filter.addItem("")
        self.cmb_filter.setItemText(7, "Último Tratamento")     
        self.cmb_filter.currentIndexChanged.connect(self.cmb_filter_changed)
        self.gridLayout_2.addWidget(self.cmb_filter, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle("RESULTADOS")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tb_results = QtWidgets.QTableView(self.groupBox_2)
        self.model = QtGui.QStandardItemModel(self.groupBox_2)
        self.model.setHorizontalHeaderLabels(['SERIAL', 'POSICAO', 'DATA DE REGISTRO', 'NOME', 'DATA DE NASCIMENTO', 'TELEFONE', 'GÊNERO', 'ESTADO CIVIL', 'OCUPAÇÃO', 'RESIDE COM', 'CEP','ENDEREÇO', 'BAIRRO', 'NÚMERO', 'CIDADE', 'ESTADO', 'TOMA SEDATIVOS?', 'TRATAMENTO MÉDICO?', 'DROME BEM?', 'VÍCIOS', 'SONHOS', 'TRABALHO', 'FAMÍLIA', 'ALIMENTAÇÃO', 'INFO PARA O DEPOE', 'ÚLTIMO TRATAMENTO', 'CURSOS E FREQUÊNCIA', 'ENCAMINHAMENTO', 'TRATAMENTOS', 'ORIENTAÇÃO ESPIRITUAL'])
        self.tb_results.setModel(self.model)        
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tb_results.setFont(font)
        self.tb_results.setObjectName("tb_results")
        self.gridLayout_3.addWidget(self.tb_results, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setText("PESQUISAR")
        icon = QtGui.QIcon.fromTheme("zoom")
        self.btn_search.setIcon(icon)
        self.btn_search.setObjectName("btn_search")
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.gridLayout.addWidget(self.btn_search, 2, 0, 1, 1)
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.btn_export.setFont(font)
        self.btn_export.setText("EXPORTAR RESULTADOS PARA EXCEL")
        icon = QtGui.QIcon.fromTheme("x-office-spreadsheet")
        self.btn_export.setIcon(icon)
        self.btn_export.setObjectName("btn_export")
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.gridLayout.addWidget(self.btn_export, 2, 1, 1, 1)
        FormReports.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(FormReports)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormReports = QtWidgets.QMainWindow()
    ui = Ui_FormReports()
    ui.setupUi(FormReports)
    FormReports.show()
    sys.exit(app.exec_())
