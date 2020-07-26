# -*- coding: utf-8 -*-
import pandas
import tkinter
import os
import shutil
import platform
import datetime
import fpdf
from tkinter import messagebox
from Connection import Database

db = Database()


class AssistedController:
    def count_assisted(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute('SELECT COUNT(*) FROM tb_assistidos').fetchone()[0]
            return rs
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor)


    def insert_assisted(self, a):
        try:
            sql_string = f'''
            INSERT INTO tb_assistidos VALUES (
                '{a.serial}',
                {a.position},
                '{a.name}',
                '{a.date_of_birth}',
                '{a.phone1}',
                '{a.phone2}',
                '{a.gender}',
                '{a.civil_state}',
                '{a.ocupation}',
                '{a.lives_with}',
                '{a.address}',
                '{a.neighbourhood}',
                '{a.number}',
                '{a.city}',
                '{a.state}',
                '{a.sedatives}',
                '{a.medical_treatment}',
                '{a.sleep_well}',
                '{a.addictions}',
                '{a.dreams}',
                '{a.work}',
                '{a.family}',
                '{a.feeding}',
                '{a.traits}',
                '{a.latest_treatment}',
                '{a.courses}',
                '{a.fowarding}',
                '{a.treatment}',
                '{a.guidance}'
            )
            '''

            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql_string)
            conn.commit()
                        
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('CADASTRADO', 'Assistido CADASTRADO com sucesso!')        
            tkinter.Tk().destroy()
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
            
        finally:
            db.close_connection(conn, cursor)    


    def update_assisted(self, a, index):
        try:
            sql_string = f'''
            UPDATE tb_assistidos SET 
            Nome = '{a.name}',
            Data_de_nascimento = '{a.date_of_birth}',
            Telefone_1 = '{a.phone1}',
            Telefone_2 = '{a.phone2}',
            Genero = '{a.gender}',
            Estado_civil = '{a.civil_state}',
            Ocupacao = '{a.ocupation}',
            Reside_com = '{a.lives_with}',
            Endereco = '{a.address}',
            Bairro = '{a.neighbourhood}',
            Numero = '{a.number}',
            Cidade = '{a.city}',
            Estado = '{a.state}',
            Toma_sedativos = '{a.sedatives}',
            Tratamento_medico = '{a.medical_treatment}',
            Dorme_bem = '{a.sleep_well}',
            Vicios = '{a.addictions}',
            Sonhos = '{a.dreams}',
            Trabalho = '{a.work}',
            Familia = '{a.family}',
            Alimentacao = '{a.feeding}',
            Info_para_DEPOE = '{a.traits}',
            Ultimo_tratamento = '{a.latest_treatment}',
            Cursos = '{a.courses}',
            Encaminhamento = '{a.fowarding}',
            Tratamentos = '{a.treatment}',
            Orientacao_espiritual = '{a.guidance}'
            WHERE Posicao = {index}
            '''
            
            conn = db.create_connection()
            cursor = conn.cursor()            
            cursor.execute(sql_string)
            conn.commit()
                        
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('CADASTRADO', 'Registro EDITADO com sucesso!')        
            tkinter.Tk().destroy()
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor)    


    def select_assisted(self, i):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(f'SELECT * FROM tb_assistidos WHERE Posicao = {i}').fetchone()                                        
            return rs
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
            
        finally:
            db.close_connection(conn, cursor)
   
   
    def delete_assisted(self, i):
        try:            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(f'DELETE FROM tb_assistidos WHERE Posicao = {i}')
            conn.commit()
            
            cursor.execute(f'UPDATE tb_assistidos SET Posicao = Posicao - 1 WHERE Posicao > {i}')
            conn.commit()
            
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('DELETADO', 'Registro DELETADO com sucesso!')        
            tkinter.Tk().destroy()
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
            
        finally:
            db.close_connection(conn, cursor)   
   
   
 
    def print_register(self, a, index):
        try:            
            conn = db.create_connection()
            cursor = conn.cursor()
            query = cursor.execute(f'SELECT * FROM tb_assistidos WHERE Posicao = {index}').fetchone()                              
            
            # results = []
            
            # for item in query:
            #     if item == None:
            #         item = ''
            #     results.append(str(item))
                    
            fields = ['SERIAL', 'ID', 'Nome do Assistido', 'Data de Nascimento', 'Telefone (Celular)', 'Telefone (Residencial)', 'Gênero', 'Estado Civil', 'Ocupação', 'Reside Com', 'Endereço', 'Bairro', 'Número', 'Cidade', 'Estado', 'Toma sedativos', 'Tratamento médico', 'Dorme bem', 'Vícios', 'Sonhos', 'Trabalho', 'Família', 'Alimentação', 'Info para DEPOE', 'Último Tratamento','Frequência - Cursos', 'Encaminhamento', 'Tratamentos', 'Orientação']
            
            pdf = fpdf.FPDF(format='A4')
            pdf.add_page()
            pdf.set_font('helvetica', 'B',size = 20)
            pdf.set_fill_color(200,200,200)
            pdf.write(15,f'FICHA DE ASSISTIDO - {query[2]}')
            pdf.ln() 
            
            i = 2
            while i < len(fields):
                if query[i] != 'Não' and query[i] != '':
                    pdf.set_font('helvetica', 'B',size = 11)
                    pdf.cell(55, 10, fields[i].upper(), 1, 0, '', 1, '')
                    pdf.set_font('helvetica', size = 11)
                    pdf.multi_cell(0, 10, query[i].replace(' --- ', ', '), 1, 'J', 0)
                i += 1                        
                
            
            if self.count_interviews(a) > 0:
                pdf.add_page()
                pdf.set_font('helvetica', 'B',size = 20)
                pdf.set_fill_color(200,200,200)
                pdf.write(15,'ÚLTIMA ENTREVISTA de {}'.format(query[2]))
                pdf.ln() 
                query_interviews = self.select_interview(a)
                latest_interview = query_interviews[len(query_interviews) - 1]
                fields_interview = ['DATA', 'ENTREVISTADOR', 'TRATAMENTO', 'ENTREVISTA']
                
                i = 0
                while i < len(fields_interview):
                    if latest_interview[i] != 'Não' and latest_interview[i] != '':
                        pdf.set_font('helvetica', 'B',size = 11)
                        pdf.cell(55, 10, fields_interview[i].upper(), 1, 0, '', 1, '')
                        pdf.set_font('helvetica', size = 11)
                        pdf.multi_cell(0, 10, latest_interview[i].replace(' --- ', ', '), 1, 'J', 0)
                    i += 1                                    
            
            if platform.system() == 'Linux':
                pdf.output(os.path.expanduser('~') + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/FICHAS_INDIVIDUAIS/Ficha_de_assistido-' + query[2] + '.pdf')
            else:                    
                pdf.output(os.path.expanduser('~') + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\FICHAS_INDIVIDUAIS\\Ficha_de_assistido-' + query[2] + '.pdf')


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
               
   
    def count_custom_search(self, custom_string):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(custom_string).fetchone()[0]                                            
            return rs
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
            
        finally:
            db.close_connection(conn, cursor)        


    def custom_search(self, custom_string):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(custom_string).fetchall()                                                
            return rs
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn, cursor)        
   
   
    def gen_custom_csv(self, custom_string, selected_filter):
        try:            
            today = datetime.datetime.now().strftime('%d-%m-%y')            
            
            conn = db.create_connection()
            db_df = pandas.read_sql_query(custom_string, conn)

            if platform.system() == 'Linux':
                db_df.to_excel(os.path.expanduser('~') + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/RELATORIOS_EXCEL/FILTRAGEM_POR_' + selected_filter.upper() + '_' + today + '.xlsx', index=False)
            else:
                db_df.to_excel(os.path.expanduser('~') + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\RELATORIOS_EXCEL\\FILTRAGEM_POR_' + selected_filter.upper() + '_' + today + '.xlsx', index=False)
            
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Relatório para EXCEL gerado com sucesso!')        
            tkinter.Tk().destroy()
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn)
            
            
    def export_data(self):
        today = datetime.datetime.now().strftime('%d-%m-%y')            
        
        if platform.system() == 'Linux':
            shutil.copyfile('sga_database.db', os.path.expanduser('~') + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/BACKUPS/BACKUP' + '_' + today + '.db')
        else:
            shutil.copyfile('sga_database.db', os.path.expanduser('~') + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\BACKUPS\\BACKUP' + '_' + today + '.db')


        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo('SUCESSO', 'BACKUP do banco de dados gerado com sucesso!\nSaindo do gerenciador de backups...')        
        tkinter.Tk().destroy()
    
                              
    def import_data(self, file):        
        # os.remove('sga_database.db')            
        shutil.copyfile(file, 'sga_database.db')
                    
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo('SUCESSO', 'Dados importados e substituidos com sucesso!\nSaindo sistema para aplicar atualizações...')        
        tkinter.Tk().destroy()            
    
    def select_active_user(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute('SELECT Nome, Usuario, Categoria FROM tb_usuarios WHERE Status = \'ON\'').fetchone()
            return rs
        
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
            cursor.execute('UPDATE tb_usuarios SET Status = \'OFF\' WHERE Status = \'ON\'')
            conn.commit()
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
            
        finally:
            db.close_connection(conn, cursor) 
    
    def register_changes(self, name, message):
        try:
            now = datetime.datetime.now().strftime('%d-%m-%y - %H:%M:%S')            

            conn = db.create_connection()
            cursor = conn.cursor()
            index = cursor.execute('SELECT COUNT(*) FROM tb_historico').fetchone()[0] + 1
                        
            sql_string = f'INSERT INTO tb_historico VALUES ({index}, \'{now}\', \'{name}\', \'{message}\')'
            cursor.execute(sql_string)
            conn.commit()
                        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection(conn, cursor)        
    
    def gen_historic(self):
        try:
            conn = db.create_connection()
            df = pandas.read_sql_query('SELECT * FROM tb_historico', conn)
            df.to_excel('Registro_de_alteracoes.xlsx', index=None)
            
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection(conn)
                        
    def count_interviews(self, a):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()            
            rs = cursor.execute(f'SELECT COUNT(*) FROM tb_entrevistas WHERE id_assistido = \'{a.serial}\'').fetchone()[0]
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
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(f'INSERT INTO tb_entrevistas VALUES (\'{i.code}\', \'{a.serial}\', \'{i.date}\', \'{i.interviewer}\', \'{i.treatment}\', \'{i.interview}\')')
            conn.commit()

            cursor.execute(f'UPDATE tb_assistidos SET Ultimo_tratamento = \'{i.treatment}\' WHERE Serial = \'{a.serial}\'')
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
            
            
    def select_interview(self, a):
        try:            
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(f'SELECT Data_da_entrevista, Entrevistador, Tratamento, Entrevista FROM tb_entrevistas WHERE id_assistido = \'{a.serial}\'').fetchall()
            
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
            sql_string = f'SELECT Data_da_entrevista, Entrevistador, Tratamento, Entrevista FROM tb_entrevistas WHERE id_assistido = \'{a.serial}\' ORDER BY id_entrevista DESC LIMIT 3'
            
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
                pdf.output(os.path.expanduser('~') + '/Documentos/GERENCIAMENTO_DE_ASSISTIDOS_AELMAC/FICHAS_INDIVIDUAIS/Entrevistas_de_' + a.name + '.pdf')
            else:                    
                pdf.output(os.path.expanduser('~') + '\\Documents\\GERENCIAMENTO_DE_ASSISTIDOS_AELMAC\\FICHAS_INDIVIDUAIS\\Entrevistas_de_' + a.name + '.pdf')

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
            