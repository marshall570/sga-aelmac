# -*- coding: utf-8 -*-
import sqlite3 as sql
import tkinter
from tkinter import messagebox
from database import Data

db = Data()

class DataAcessInterview:
    def create_table_interview(self):
        try:
            table_sql = 'CREATE TABLE IF NOT EXISTS tb_entrevistas (id_entrevista INTEGER NOT NULL PRIMARY KEY, id_assistido TEXT NOT NULL, Entrevistador TEXT, Tratamento TEXT, Entrevista TEXT, FOREIGN KEY (id_assistido) REFERENCES tb_assistidos (id_assistido))'
            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(table_sql)
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)
            