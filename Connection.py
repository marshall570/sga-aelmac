# -*- coding: utf-8 -*-
import sqlite3 as sql
import tkinter
from tkinter import messagebox

class Database:
    def __init__(self, conn=None, cursor=None, rs=None):
        self.conn = conn
        self.cursor = cursor
        self.rs = rs

    def create_connection(self):
        conn = None
        
        try:
            conn = sql.connect('sga_database.db')
            return conn
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
    def close_connection(self, conn=None, cursor=None):
        try:
            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()
                
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
