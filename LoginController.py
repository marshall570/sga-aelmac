# -*- coding: utf-8 -*-
import pandas
import datetime
import tkinter
import random
import string
from tkinter import messagebox
from Connection import Database

db = Database()


class LoginController:
    def create_tables(self):
        try:
            table_users = '''
            CREATE TABLE IF NOT EXISTS tb_usuarios (
                id_usuario TEXT NOT NULL PRIMARY KEY,
                Nome TEXT,
                Usuario TEXT,
                Senha TEXT,
                Categoria TEXT,
                Status TEXT
            )
            '''
            
            table_assisted = '''
            CREATE TABLE IF NOT EXISTS tb_assistidos (
                Serial TEXT NOT NULL PRIMARY KEY,
                Posicao INTEGER NOT NULL,
                Nome TEXT,
                Data_de_nascimento TEXT,
                Telefone_1 TEXT,
                Telefone_2 TEXT,
                Genero TEXT,
                Estado_civil TEXT,
                Ocupacao TEXT,
                Reside_com TEXT,
                Endereco TEXT,
                Bairro TEXT,
                Numero TEXT,
                Cidade TEXT,
                Estado TEXT,
                Toma_sedativos TEXT,
                Tratamento_medico TEXT,
                Dorme_bem TEXT,
                Vicios TEXT,
                Sonhos TEXT,
                Trabalho TEXT,
                Familia TEXT,
                Alimentacao TEXT,
                Info_para_DEPOE TEXT,
                Ultimo_tratamento TEXT,
                Cursos TEXT,
                Encaminhamento TEXT,
                Tratamentos TEXT,
                Orientacao_espiritual TEXT
            )
            '''
            
            table_interview = '''
            CREATE TABLE IF NOT EXISTS tb_entrevistas (
                id_entrevista TEXT NOT NULL PRIMARY KEY,
                id_assistido TEXT NOT NULL,
                Data_da_Entrevista TEXT,
                Entrevistador TEXT,
                Tratamento TEXT,
                Entrevista TEXT,
                FOREIGN KEY (id_assistido) REFERENCES tb_assistidos (Serial)
            )
            '''
            
            table_changes = '''
            CREATE TABLE IF NOT EXISTS tb_historico (
                id_alteracao INTEGER NOT NULL PRIMARY KEY,
                Data_da_alteracao TEXT,
                Usuario TEXT,
                Alteracao TEXT
            )
            '''
            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(table_users)
            cursor.execute(table_assisted)
            cursor.execute(table_interview)
            cursor.execute(table_changes)
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
            
        finally:
            db.close_connection(conn, cursor)    
    
    def id_gen_historic(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute('SELECT COUNT(*) FROM tb_historico').fetchone()[0] + 1
            return rs
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor)        
            

    def count_user(self, user):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(f'SELECT COUNT(*) FROM tb_usuarios WHERE Usuario = \'{user}\'').fetchone()[0]
            return rs
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor)


    def check_password(self, user, password):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            verification = cursor.execute(f'SELECT Senha FROM tb_usuarios WHERE Usuario = \'{user}\'').fetchone()[0]
            
            if password == verification:
                return True
            
            else:
                return False
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor)


    def insert_user(self, name, user, password, category):
        try:            
            unique_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            
            sql_string = f'INSERT INTO tb_usuarios VALUES (\'{unique_id}\', \'{name}\', \'{user}\', \'{password}\', \'{category}\', \'OFF\')'

            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql_string)
            conn.commit()
                        
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('CADASTRADO', 'Usuário cadastrado com sucesso!')        
            tkinter.Tk().destroy()
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
            
        finally:
            db.close_connection(conn, cursor)            

    def select_user(self, user):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute("SELECT Usuario, Senha, Categoria FROM tb_usuarios WHERE Usuario = '{}'".format(user)).fetchone()
            return rs
       
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor)

    def select_active_user(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute("SELECT Nome, Usuario, Categoria FROM tb_usuarios WHERE Status = 'ON'").fetchone()
            return rs
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
            
        finally:
            db.close_connection(conn, cursor)            
            
    def set_on(self, user):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(f'UPDATE tb_usuarios SET Status = \'ON\' WHERE Usuario = \'{user}\'')
            conn.commit()
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor) 

    def set_off(self):
        try:            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tb_usuarios SET Status = 'OFF' WHERE Status = 'ON'")
            conn.commit()
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
            
        finally:
            db.close_connection(conn, cursor) 