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
            table_sql = 'CREATE TABLE IF NOT EXISTS tb_assistidos (id_assistido INTEGER NOT NULL PRIMARY KEY, Nome TEXT, Data_de_nascimento TEXT, Telefone_1 TEXT, Telefone_2 TEXT, Genero TEXT, Estado_civil TEXT, Ocupacao TEXT, Reside_com TEXT, Endereco TEXT, Bairro TEXT, Numero TEXT, Cidade TEXT, Estado TEXT, Toma_sedativos TEXT, Tratamento_medico TEXT, Dorme_bem TEXT, Vicios TEXT, Sonhos TEXT, Trabalho TEXT, Familia TEXT, Alimentacao TEXT, Info_para_DEPOE TEXT, Cursos TEXT, Encaminhamento TEXT, Tratamentos TEXT, Orientacao_espiritual TEXT)'
            
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
            sql_string = "INSERT INTO tb_assistidos VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(a.code, a.name, a.date_of_birth, a.phone1, a.phone2, a.gender, a.civil_state, a.ocupation, a.lives_with, a.address, a.neighbourhood, a.number, a.city, a.state, a.sedatives, a.medical_treatment, a.sleep_well, a.addictions, a.dreams, a.work, a.family, a.feeding, a.traits, a.courses, a.fowarding, a.treatment, a.guidance)

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
            sql_string = "INSERT INTO tb_assistidos VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(a.code - 1, a.name, a.date_of_birth, a.phone1, a.phone2, a.gender, a.civil_state, a.ocupation, a.lives_with, a.address, a.neighbourhood, a.number, a.city, a.state, a.sedatives, a.medical_treatment, a.sleep_well, a.addictions, a.dreams, a.work, a.family, a.feeding, a.traits, a.courses, a.fowarding, a.treatment, a.guidance)

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
                                                            
            a.code = rs[0]
            a.name = rs[1]
            a.date_of_birth = rs[2]
            a.phone1 = rs[3]
            a.phone2 = rs[4]
            a.gender = rs[5]
            a.civil_state = rs[6]
            a.ocupation = rs[7]
            a.lives_with = rs[8]
            a.address = rs[9]
            a.neighbourhood = rs[10]
            a.number = rs[11]
            a.city = rs[12]
            a.state = rs[13]
            a.sedatives = rs[14]
            a.medical_treatment = rs[15]
            a.sleep_well = rs[16]
            a.addictions = rs[17]
            a.dreams = rs[18]
            a.work = rs[19]
            a.family = rs[20]
            a.feeding = rs[21]
            a.traits = rs[22]
            a.courses = rs[23]
            a.fowarding = rs[24]
            a.treatment = rs[25]
            a.guidance = rs[26]
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)
   
   
    def delete_assisted(self, i):
        try:
            temp_id = i
            sql_string = 'DELETE FROM tb_assistidos WHERE id_assistido = ' + str(temp_id)
            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql_string)
            conn.commit()
            
            sql_string = 'UPDATE tb_assistidos SET id_assistido = id_assistido - 1 WHERE id_assistido > ' + str(temp_id)
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
                    
            fields = ['ID', 'Nome do Assistido', 'Data de Nascimento', 'Telefone (Celular)', 'Telefone (Residencial)', 'Gênero', 'Estado Civil', 'Ocupação', 'Reside Com', 'Endereço', 'Bairro', 'Número', 'Cidade', 'Estado', 'Toma sedativos', 'Tratamento médico', 'Dorme bem', 'Vícios', 'Sonhos', 'Trabalho', 'Família', 'Alimentação', 'Info para DEPOE', 'Frequência - Cursos', 'Encaminhamento', 'Tratamentos', 'Orientação']
            
            pdf = fpdf.FPDF(format='A4')
            pdf.add_page()
            pdf.set_font('times', 'B',size = 20)
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
        
   