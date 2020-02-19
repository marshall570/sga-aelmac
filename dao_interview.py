# -*- coding: utf-8 -*-
import sqlite3 as sql
import tkinter
from tkinter import messagebox
from database import Data

db = Data()

class DataAcessInterview:
    def create_table_interview(self):
        try:
            table_sql = 'CREATE TABLE IF NOT EXISTS tb_entrevistas (id_entrevista INTEGER NOT NULL PRIMARY KEY, id_assistido INTEGER NOT NULL, Data_da_Entrevista TEXT, Entrevistador TEXT, Tratamento TEXT, Entrevista TEXT, FOREIGN KEY (id_assistido) REFERENCES tb_assistidos (id_assistido))'
            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(table_sql)
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)

    
    def id_gen_interview(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute('SELECT COUNT(*) FROM tb_entrevistas').fetchone()[0] + 1
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)
            
    
    def insert_interview(self, i, a):
        try:
            sql_string = "INSERT INTO tb_entrevistas VALUES ({}, {}, '{}', '{}', '{}', '{}')".format(i.code, a.code, i.date, i.interviewer, i.treatment, i.interview)
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql_string)
            conn.commit()

            sql_string = "UPDATE tb_assistidos SET Ultimo_tratamento = '{}' WHERE id_assistido = {}".format(i.treatment, a.code)
            cursor.execute(sql_string)
            conn.commit()

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('CADASTRADO', 'Entrevista registrada com sucesso!\nSaindo do modo de edição...')     
            tkinter.Tk().destroy()            
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)
            
            
    def select_interview(self, a):
        try:
            select_string = 'SELECT Data_da_Entrevista, Entrevistador, Tratamento, Entrevista FROM tb_entrevistas WHERE id_assistido = ' + str(a.code)
            
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(select_string).fetchall()
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)
        
