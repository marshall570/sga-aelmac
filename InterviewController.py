# -*- coding: utf-8 -*-
import tkinter
import platform
import os
import fpdf
from tkinter import messagebox
from Connection import Database

db = Database()


class InterviewController:   
    def count_interviews(self, index):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(f'SELECT COUNT(*) FROM tb_entrevistas WHERE Posicao = {index}').fetchone()[0]
            return rs
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor)
            
    
    def insert_interview(self, i, a):
        try:
            sql_string = "INSERT INTO tb_entrevistas VALUES ({}, {}, '{}', '{}', '{}', '{}')".format(i.code, a.serial, i.date, i.interviewer, i.treatment, i.interview)
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql_string)
            conn.commit()

            sql_string = "UPDATE tb_assistidos SET Ultimo_tratamento = '{}' WHERE Serial = {}".format(i.treatment, a.serial)
            cursor.execute(sql_string)
            conn.commit()

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('CADASTRADO', 'Entrevista registrada com sucesso!')     
            tkinter.Tk().destroy()
                   
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor)
            
            
    def select_interview(self, index):
        try:            
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(f'SELECT Data_da_entrevista, Entrevistador, Tratamento, Entrevista FROM tb_entrevistas WHERE Posicao = {index}').fetchall()
            return rs
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor)
  
        
    def print_interviews(self, a):
        try:            
            sql_string = f"SELECT Data_da_entrevista, Entrevistador, Tratamento, Entrevista FROM tb_entrevistas WHERE id_assistido = {a.serial} ORDER BY id_entrevista DESC LIMIT 3"
            
            conn = db.create_connection()
            cursor = conn.cursor()
            query = cursor.execute(sql_string).fetchall()
                
            pdf = fpdf.FPDF(format='A4')
            pdf.add_page()
            pdf.set_font('helvetica', 'B',size = 20)
            pdf.set_fill_color(200,200,200)
            pdf.write(15,'ÚLTIMAS ENTREVISTAS de {}'.format(a.name))
            pdf.ln()             

            fields_interview = ['DATA', 'ENTREVISTADOR', 'TRATAMENTO', 'ENTREVISTA']
            
            j = 0
            while j < 3:
                i = 0
                while i < len(fields_interview):
                    if query[j][i] != 'Não' and query[j][i] != '':                    
                        pdf.set_font('helvetica', 'B',size = 11)
                        pdf.cell(55, 10, fields_interview[i].upper(), 1, 0, '', 1, '')
                        pdf.set_font('helvetica', size = 11)
                        pdf.multi_cell(0, 10, query[j][i], 1, 'J', 0)
                    i += 1
                pdf.ln()                                 
                j += 1
                
            if platform.system() == 'Linux':
                pdf.output(os.path.expanduser("~") + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/FICHAS_INDIVIDUAIS/Entrevistas_de_' + a.name + '.pdf')
            else:                    
                pdf.output(os.path.expanduser("~") + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\FICHAS_INDIVIDUAIS\\Entrevistas_de_' + a.name + '.pdf')

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('GERAR FICHA', 'Ficha para impressão gerada com sucesso para a pasta <FICHAS_INDIVIDUAIS>!')
            tkinter.Tk().destroy()
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn)
            