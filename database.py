# -*- coding: utf-8 -*-
import sqlite3 as sql


class Data:
    def __init__(self, conn=None, cursor=None, rs=None):
        self.conn = conn
        self.cursor = cursor
        self.rs = rs

    def create_connection(self):
        conn = None
        db_file = 'sga_database.db'
        try:
            conn = sql.connect(db_file)
            return conn
        except sql.Error as e:
            print(e)
        return conn

    def close_connection(self, conn=None, cursor=None):
        try:
            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()
        except sql.Error as e:
            print(e)
