# -*- coding: utf-8 -*-
import sqlite3 as sql
import tkinter
from tkinter import messagebox
from database import Data

db = Data()

class DataAcessInterview:
    def create_table_interview(self):
        try:
            table_sql = 'CREATE TABLE IF NOT EXISTS tb_entrevistas (id_entrevista INTEGER NOT NULL PRIMARY KEY, Entrevistador TEXT, Tratamento TEXT, Entrevista TEXT)'
            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(table_sql)
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)


    def create_table_assisted_interview(self):
        try:
            table_sql = 'CREATE TABLE IF NOT EXISTS tb_entrevistados (id_entrevistado INTEGER NOT NULL PRIMARY KEY, id_entrevista INTEGER, id_assistido INTEGER, FOREIGN KEY (id_entrevista) REFERENCES tb_entrevista (id_entrevista), FOREIGN KEY (id_assistido) REFERENCES tb_assistido (id_assistidos))'
            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(table_sql)
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)
            