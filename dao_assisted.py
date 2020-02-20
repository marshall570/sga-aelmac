# -*- coding: utf-8 -*-
import sqlite3 as sql
import pandas as pd
import tkinter
import os
import platform
import datetime
import fpdf
from tkinter import messagebox
from database import Data

db = Data()

class DataAcessAssisted:
    def create_table_assisted(self):
        try:
            table_sql = 'CREATE TABLE IF NOT EXISTS tb_assistidos (id_assistido INTEGER NOT NULL PRIMARY KEY, Nome TEXT, Data_de_nascimento TEXT, Telefone_1 TEXT, Telefone_2 TEXT, Genero TEXT, Estado_civil TEXT, Ocupacao TEXT, Reside_com TEXT, Endereco TEXT, Bairro TEXT, Numero TEXT, Cidade TEXT, Estado TEXT, Toma_sedativos TEXT, Tratamento_medico TEXT, Dorme_bem TEXT, Vicios TEXT, Sonhos TEXT, Trabalho TEXT, Familia TEXT, Alimentacao TEXT, Info_para_DEPOE TEXT, Ultimo_tratamento TEXT, Cursos TEXT, Encaminhamento TEXT, Tratamentos TEXT, Orientacao_espiritual TEXT)'
            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(table_sql)
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)


    def id_gen_assisted(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute('SELECT COUNT(*) FROM tb_assistidos').fetchone()[0] + 1
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)                


    def insert_assisted(self, a):
        try:
            sql_string = "INSERT INTO tb_assistidos VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(a.code, a.name, a.date_of_birth, a.phone1, a.phone2, a.gender, a.civil_state, a.ocupation, a.lives_with, a.address, a.neighbourhood, a.number, a.city, a.state, a.sedatives, a.medical_treatment, a.sleep_well, a.addictions, a.dreams, a.work, a.family, a.feeding, a.traits, a.latest_treatment,a.courses, a.fowarding, a.treatment, a.guidance)

            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql_string)
            conn.commit()
                        
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('CADASTRADO', 'Assistido CADASTRADO com sucesso!')        
            tkinter.Tk().destroy()
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)    


    def edit_assisted(self, a):
        try:
            sql_string = "INSERT INTO tb_assistidos VALUES ({}, '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(a.code - 1, a.name, a.date_of_birth, a.phone1, a.phone2, a.gender, a.civil_state, a.ocupation, a.lives_with, a.address, a.neighbourhood, a.number, a.city, a.state, a.sedatives, a.medical_treatment, a.sleep_well, a.addictions, a.dreams, a.work, a.family, a.feeding, a.traits, a.latest_treatment,a.courses, a.fowarding, a.treatment, a.guidance)

            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tb_assistidos WHERE id_assistido = {}'.format(a.code - 1))
            conn.commit()

            cursor.execute(sql_string)
            conn.commit()
                        
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('CADASTRADO', 'Registro EDITADO com sucesso!')        
            tkinter.Tk().destroy()
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)    


    def select_assisted(self, a, i):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute('SELECT * FROM tb_assistidos WHERE id_assistido = {}'.format(i)).fetchone()                                        

            new_values = []            
            for value in rs:
                if value == None:
                    item = ''
                else:
                    item = value
                new_values.append(item)
            
                                                                     
            a.code = new_values[0]
            a.name = new_values[1]
            a.date_of_birth = new_values[2]
            a.phone1 = new_values[3]
            a.phone2 = new_values[4]
            a.gender = new_values[5]
            a.civil_state = new_values[6]
            a.ocupation = new_values[7]
            a.lives_with = new_values[8]
            a.address = new_values[9]
            a.neighbourhood = new_values[10]
            a.number = new_values[11]
            a.city = new_values[12]
            a.state = new_values[13]
            a.sedatives = new_values[14]
            a.medical_treatment = new_values[15]
            a.sleep_well = new_values[16]
            a.addictions = new_values[17]
            a.dreams = new_values[18]
            a.work = new_values[19]
            a.family = new_values[20]
            a.feeding = new_values[21]
            a.traits = new_values[22]
            a.latest_treatment = new_values[23]
            a.courses = new_values[24]
            a.fowarding = new_values[25]
            a.treatment = new_values[26]
            a.guidance = new_values[27]
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)
   
   
    def delete_assisted(self, i):
        try:
            sql_string = 'DELETE FROM tb_assistidos WHERE id_assistido = ' + str(i)
            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql_string)
            conn.commit()
            
            sql_string = 'DELETE FROM tb_entrevistas WHERE id_assistido = ' + str(i)
            cursor.execute(sql_string)
            conn.commit()                        
            
            sql_string = 'UPDATE tb_assistidos SET id_assistido = id_assistido - 1 WHERE id_assistido > ' + str(i)
            cursor.execute(sql_string)
            conn.commit()

            sql_string = 'UPDATE tb_entrevistas SET id_assistido = id_assistido - 1 WHERE id_assistido > ' + str(i)
            cursor.execute(sql_string)
            conn.commit()
            
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('DELETADO', 'Registro DELETADO com sucesso!')        
            tkinter.Tk().destroy()        
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)   
   
   
 
    def print_register(self, a):
        try:
            conn = db.create_connection()
            
            sql_string = "SELECT * FROM tb_assistidos WHERE id_assistido = {}".format(a.code)
            
            query = list(conn.execute(sql_string).fetchone())
            
            results = []
            
            for item in query:
                results.append(str(item))
                    
            fields = ['ID', 'Nome do Assistido', 'Data de Nascimento', 'Telefone (Celular)', 'Telefone (Residencial)', 'Gênero', 'Estado Civil', 'Ocupação', 'Reside Com', 'Endereço', 'Bairro', 'Número', 'Cidade', 'Estado', 'Toma sedativos', 'Tratamento médico', 'Dorme bem', 'Vícios', 'Sonhos', 'Trabalho', 'Família', 'Alimentação', 'Info para DEPOE', 'Último Tratamento','Frequência - Cursos', 'Encaminhamento', 'Tratamentos', 'Orientação']
            
            pdf = fpdf.FPDF(format='A4')
            pdf.add_page()
            pdf.set_font('helvetica', 'B',size = 20)
            pdf.set_fill_color(200,200,200)
            pdf.write(15,'FICHA DO ASSISTIDO - {}'.format(results[1]))
            pdf.ln()  
            
            i = 1
            while i < len(fields):
                if results[i] != 'Não' and results[i] != '':
                    pdf.set_font('helvetica', 'B',size = 11)
                    pdf.cell(55, 10, fields[i].upper(), 1, 0, '', 1, '')
                    pdf.set_font('helvetica', size = 11)
                    pdf.multi_cell(0, 10, results[i].replace(' --- ', ', '), 1, 'J', 0)
                i += 1
                
            if platform.system() == 'Linux':
                path = os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/FICHAS_INDIVIDUAIS/'
                if not os.path.exists(path):
                    os.mkdir(path)
                    
                pdf.output(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/FICHAS_INDIVIDUAIS/Ficha_de_assistido-' + results[1] + '.pdf')
            else:
                if os.path.isdir(os.path.expanduser("~") + '/Documents/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/FICHAS_INDIVIDUAIS/'.replace('/','\\')) is False:
                    os.mkdir(os.path.expanduser("~") + '/Documents/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/FICHAS_INDIVIDUAIS/'.replace('/','\\'))
                    
                pdf.output(os.path.expanduser("~") + '/Documents/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/FICHAS_INDIVIDUAIS/Ficha_de_assistido-' + results[1] + '.pdf'.replace('/','\\'))


            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('GERAR FICHA', 'Ficha para impressão gerada com sucesso para a pasta <FICHAS_INDIVIDUAIS>!')
            tkinter.Tk().destroy()
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn)
               
   
    def count_custom_search(self, custom_string):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(custom_string).fetchone()[0]                                            
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)        


    def custom_search(self, custom_string):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(custom_string).fetchall()                                                
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)        
   
   
    def gen_custom_csv(self, custom_string, selected_filter):
        try:            
            today = datetime.datetime.now().strftime("%d-%m-%y")            
            
            
            if platform.system() == 'Linux':
                if not os.path.exists(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/RELATORIOS/'):
                    os.mkdir(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/RELATORIOS/')
            else:
                if not os.path.isdir(os.path.expanduser("~") + '\\Documents\\Pedidos_AELMAC\\EXCEL'):
                    os.mkdir(os.path.expanduser("~") + '\\Documents\\Pedidos_AELMAC\\EXCEL')

            conn = db.create_connection()
            db_df = pd.read_sql_query(custom_string, conn)

            if platform.system() == 'Linux':
                db_df.to_excel(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/RELATORIOS/FILTRAGEM_POR_' + selected_filter.upper() + '_' + today + '.xlsx', index=False)
            else:
                db_df.to_excel(os.path.expanduser("~") + '\\Documents\\Pedidos_AELMAC\\EXCEL\\Pedidos_EXCEL_' + selected_filter.upper() + '_' + today + '.xlsx', index=False)

            
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Relatório para EXCEL gerado com sucesso!')        
            tkinter.Tk().destroy()
            
            db.close_connection(conn)
        except sql.Error as e:
            print(e)
            
            
    def export_data(self):
        try:            
            today = datetime.datetime.now().strftime("%d-%m-%y")            
            
            
            if platform.system() == 'Linux':
                if not os.path.exists(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/BACKUPS/'):
                    os.mkdir(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/BACKUPS/')
            else:
                if not os.path.isdir(os.path.expanduser("~") + '\\Documents\\Pedidos_AELMAC\\EXCEL'):
                    os.mkdir(os.path.expanduser("~") + '\\Documents\\Pedidos_AELMAC\\EXCEL')

            conn = db.create_connection()
            db_df_assisted = pd.read_sql_query('SELECT * FROM tb_assistidos', conn)
            db_df_interview = pd.read_sql_query('SELECT * FROM tb_entrevistas', conn)

            if platform.system() == 'Linux':
                writer = pd.ExcelWriter(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/BACKUPS/BACKUP' + '_' + today + '.xlsx', engine='xlsxwriter')                
                db_df_assisted.to_excel(writer, sheet_name = 'tb_assistidos', index = None, header = True)
                db_df_interview.to_excel(writer, sheet_name = 'tb_entrevistas', index = None, header = True)
                
                workbook = writer.book
                worksheet = writer.sheets['tb_assistidos']
                
                format_text = workbook.add_format()
                format_text.set_num_format('@')
                worksheet.set_column('B:AB', None, format_text)
                
                writer.save()
            else:
                db_df_assisted.to_excel(os.path.expanduser("~") + '\\Documents\\Pedidos_AELMAC\\EXCEL\\BACKUPS' + '_' + today + '.xlsx', index=False)

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'BACKUP do banco de dados gerado com sucesso!\nSaindo do gerenciador de backups...')        
            tkinter.Tk().destroy()
            
            db.close_connection(conn)
        except sql.Error as e:
            print(e)
        
   
    def import_data(self, file):
        try:            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute('DROP TABLE tb_assistidos')
            conn.commit()
            cursor.execute('DROP TABLE tb_entrevistas')
            conn.commit()
            
            wb = pd.ExcelFile(file + '.xlsx')            

            for sheet in wb.sheet_names:
                if sheet == 'tb_assistidos':               
                    df = pd.read_excel(file + '.xlsx', sheet_name=sheet, converters={'id_assistido': int, 'Nome':str, 'Data_de_nascimento': str, 'Telefone_1': str, 'Telefone_2': str, 'Genero': str, 'Estado_civil': str, 'Ocupacao': str, 'Reside_com': str, 'Endereco': str, 'Bairro': str, 'Numero': str, 'Cidade': str, 'Estado': str, 'Toma_sedativos': str, 'Tratamento_medico': str, 'Dorme_bem': str, 'Vicios': str, 'Sonhos': str, 'Trabalho': str, 'Familia': str, 'Alimentacao': str, 'Info_para_DEPOE': str, 'Ultimo_tratamento': str, 'Cursos': str, 'Encaminhamento': str, 'Tratamentos': str, 'Orientacao_espiritual': str})
                    df.to_sql(sheet, conn, index=False)
                else:
                    df = pd.read_excel(file + '.xlsx', sheet_name=sheet, converters={'id_entrevista': int, 'id_assistido': int, 'Entrevistador': str, 'Tratamento': str, 'Entrevista': str})                    
                    df.to_sql(sheet, conn, index=False)              
            conn.commit()
            
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Dados importados e substituidos com sucesso!\nSaindo do gerenciador de backups...')        
            tkinter.Tk().destroy()
            
            db.close_connection(conn)
        except sql.Error as e:
            print(e)   
   
   
   
   
   
   
   
   
   
               
    def gen_csv(self):
        try:
            data = datetime.datetime.now().strftime("%d-%m-%y")
            
            if platform.system() == 'Linux':
                if not os.path.exists(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC/EXCEL'):
                    os.mkdir(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC/EXCEL')
            else:
                if not os.path.isdir(os.path.expanduser("~") + '\\Documents\\Pedidos_AELMAC\\EXCEL'):
                    os.mkdir(os.path.expanduser("~") + '\\Documents\\Pedidos_AELMAC\\EXCEL')

            conn = db.create_connection()
            db_df = pd.read_sql_query("SELECT * FROM tb_pedidos", conn)

            if platform.system() == 'Linux':
                db_df.to_csv(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC/EXCEL/Pedidos_EXCEL_' + data +'.csv', index=False)
            else:
                db_df.to_csv(os.path.expanduser("~") + '\\Documents\\Pedidos_AELMAC\\EXCEL\\Pedidos_EXCEL_' + data +'.csv', index=False)

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Relatório para EXCEL gerado com sucesso!')        
            tkinter.Tk().destroy()
            
            db.close_connection(conn)
        except sql.Error as e:
            print(e)
        
   