# -*- coding: utf-8 -*-
import sqlite3 as sql
import tkinter
from tkinter import messagebox
from database import Data

db = Data()

class DataAcessUser:
    def create_table_user(self):
        try:
            table_sql = 'CREATE TABLE IF NOT EXISTS tb_usuarios (id_usuario INTEGER NOT NULL PRIMARY KEY, Nome TEXT, Usuario TEXT, Senha TEXT, Categoria TEXT)'
            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(table_sql)
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)


    def id_gen_user(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute('SELECT COUNT(*) FROM tb_usuarios').fetchone()[0] + 1
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)        
            

    def register_count_user(self, u):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute("SELECT COUNT(*) FROM tb_usuarios WHERE Usuario = '{}'".format(u.user)).fetchone()[0]
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)


    def check_password(self, u):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute("SELECT Senha FROM tb_usuarios WHERE Usuario = '{}'".format(u.user)).fetchone()[0]
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)


    def insert_user(self, u):
        try:
            sql_string = "INSERT INTO tb_usuarios VALUES ({}, '{}', '{}', '{}', '{}')".format(u.code, u.name, u.user, u.password, u.category)

            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql_string)
            conn.commit()
                        
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('CADASTRADO', 'Usuário cadastrado com sucesso!')        
            tkinter.Tk().destroy()
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)
            
            
    def select_user(self, user):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute("SELECT Usuario, Senha, Categoria FROM tb_usuarios WHERE Usuario = '{}'".format(user)).fetchone()
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)

    def count_user(self, user):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute("SELECT COUNT(*) FROM tb_usuarios WHERE Usuario = '{}'".format(user)).fetchone()[0]
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)
    
       
            
    # def set_off(self):
    #     try:
    #         sql_string = "UPDATE tb_usuarios SET Status = 'OFF' WHERE Status = 'ON'"

    #         conn = db.create_connection()
    #         cursor = conn.cursor()
    #         cursor.execute(sql_string)
    #         conn.commit()
    #     except sql.Error as e:
    #         print(e)
    #     finally:
    #         db.close_connection(conn, cursor) 
            
            
    # def set_on(self, u):
    #     try:
    #         sql_string = "UPDATE tb_usuarios SET Status = 'ON' WHERE Usuario = '{}'".format(u.user)

    #         conn = db.create_connection()
    #         cursor = conn.cursor()
    #         cursor.execute(sql_string)
    #         conn.commit()
    #     except sql.Error as e:
    #         print(e)
    #     finally:
    #         db.close_connection(conn, cursor) 
