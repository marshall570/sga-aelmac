# -*- coding: utf-8 -*-
import tkinter
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
from dto_user import User
from dto_assisted import Assisted
from dto_interview import Interview
from dao_assisted import DAOAssisted
from dao_interview import DAOInterview
from dao_user import DAOUser

# GLOBAL OBJECTS
dao_assisted = DAOAssisted()
dao_interview = DAOInterview()
dao_user = DAOUser()

a = Assisted()
i = Interview()
u = User()
class Ui_FormFicha(object):
    ####################################################    
    # FORM VARIABLES    
    ####################################################    
    index = 0
    error_message = ''
    adding = False
    editing = False
    writing_interview = False
    old_values = []
    
    
    ####################################################    
    # PASSIVE METHODS
    ####################################################
    def get_user(self):
        result = dao_user.select_active_user()

        u.name = result[0]
        u.user = result[1]
        u.category = result[2]
    
    def empty_form(self):
        self.txt_name.setText('')
        self.txt_date.setText('')
        self.txt_phone1.setText('')
        self.txt_phone2.setText('')
        self.txt_ocupation.setText('')
        self.txt_lives_with.setText('')
        self.txt_address.setText('')
        self.txt_neighbourhood.setText('')
        self.txt_number.setText('')
        self.txt_city.setText('')
        
        if self.radio_sedative_yes.isChecked():
            self.radio_sedative_no.toggle()         
        if self.radio_medical_treatment_yes.isChecked():
            self.radio_medical_treatment_no.toggle()
        if self.radio_sleep_well_yes.isChecked():
            self.radio_sleep_well_no.toggle()        
        self.radio_addiction_no.click()
        if self.check_alcohol.isChecked():
            self.check_alcohol.toggle()
        if self.check_tobacco.isChecked():
            self.check_tobacco.toggle()
        if self.check_cigarette.isChecked():
            self.check_cigarette.toggle()
        if self.check_drugs.isChecked():
            self.check_drugs.toggle()
        if self.check_sex.isChecked():
            self.check_sex.toggle()
        self.check_alcohol.setEnabled(False)
        self.check_tobacco.setEnabled(False)
        self.check_cigarette.setEnabled(False)
        self.check_drugs.setEnabled(False)
        self.check_sex.setEnabled(False)
        if self.radio_dreams_no.isChecked():
            self.radio_dreams_yes.toggle()
        self.txt_dreams.setText('')
        self.txt_work.setText('')
        self.txt_family.setText('')
        if self.check_depression.isChecked():
            self.check_depression.toggle()
        if self.check_mental_disorder.isChecked():
            self.check_mental_disorder.toggle()
        if self.check_pre_surgery.isChecked():
            self.check_pre_surgery.toggle()
        if self.check_post_surgery.isChecked():
            self.check_post_surgery.toggle()
        if self.check_victim_of_violence.isChecked():
            self.check_victim_of_violence.toggle()
        if self.check_acute_physical_illness.isChecked():
            self.check_acute_physical_illness.toggle()
        if self.check_unknow_disease.isChecked():
            self.check_unknow_disease.toggle()
        if self.check_idea_of_eliminate.isChecked():
            self.check_idea_of_eliminate.toggle()
        if self.check_umbanda.isChecked():
            self.check_umbanda.toggle()
        if self.check_disappearence.isChecked():
            self.check_disappearence.toggle()
        if self.check_homicidal.isChecked():
            self.check_homicidal.toggle()
        if self.check_problem_continues.isChecked():
            self.check_problem_continues.toggle()
        if self.check_violence_practice.isChecked():
            self.check_violence_practice.toggle()
        if self.check_serious_physical_illness.isChecked():
            self.check_serious_physical_illness.toggle()
        if self.check_aggresive_mental_illness.isChecked():
            self.check_aggresive_mental_illness.toggle()
        if self.check_possession.isChecked():
            self.check_possession.toggle()
        if self.check_problems_at_home.isChecked():
            self.check_problems_at_home.toggle()
        if self.check_panic_sindrome.isChecked():
            self.check_panic_sindrome.toggle()
        self.txt_traits.setText('')
        
        self.txt_interviewer.setText('')
        self.cmb_treatment.setCurrentText('NENHUM')
        self.txt_interview.setPlainText('SALVE O REGISTRO PARA DEPOIS ESCREVER AS ENTREVISTAS')
        self.btn_save_interview.setEnabled(False)
        self.btn_new_interview.setEnabled(False)
        if self.check_preparatory.isChecked():
            self.check_preparatory.toggle()
        if self.check_basic1.isChecked():
            self.check_basic1.toggle()
        if self.check_basic2.isChecked():
            self.check_basic2.toggle()
        if self.check_apprentice1.isChecked():
            self.check_apprentice1.toggle()
        if self.check_apprentice2.isChecked():
            self.check_apprentice2.toggle()
        if self.check_education1.isChecked():
            self.check_education1.toggle()
        if self.check_education2.isChecked():
            self.check_education2.toggle()
        if self.check_exposer.isChecked():
            self.check_exposer.toggle()
        if self.check_philosophy.isChecked():
            self.check_philosophy.toggle()
        if self.check_directors.isChecked():
            self.check_directors.toggle()
        if self.check_depass.isChecked():
            self.check_depass.toggle()
        if self.check_social_assistant.isChecked():
            self.check_social_assistant.toggle()
        if self.check_teaching.isChecked():
            self.check_teaching.toggle()
        self.txt_fowarding.setText('')
        
        if self.radio_pasteur_a2.isChecked():
            self.radio_pasteur_a2.toggle()
        if self.radio_pasteur_a4.isChecked():
            self.radio_pasteur_a4.toggle()
        if self.radio_pasteur_12.isChecked():
            self.radio_pasteur_12.toggle()
        if self.radio_pasteur_a3.isChecked():
            self.radio_pasteur_a3.toggle()
        if self.radio_pasteur_3e3m.isChecked():
            self.radio_pasteur_3e3m.toggle()
        if self.radio_pasteur_p3f.isChecked():
            self.radio_pasteur_p3f.toggle()
        if self.check_good_thoughts.isChecked():
            self.check_good_thoughts.toggle()
        if self.check_home_gospel.isChecked():
            self.check_home_gospel.toggle()
        if self.check_readings.isChecked():
            self.check_readings.toggle()
        if self.check_doctor.isChecked():
            self.check_doctor.toggle()
        if self.check_care_package.isChecked():
            self.check_care_package.toggle()
        if self.check_no_treatment.isChecked():
            self.check_no_treatment.toggle()
        if self.check_home_sanitation.isChecked():
            self.check_home_sanitation.toggle()
        if self.check_intimate_makeover.isChecked():
            self.check_intimate_makeover.toggle()
        if self.check_study.isChecked():
            self.check_study.toggle()
        if self.check_frequency.isChecked():
            self.check_frequency.toggle()
        if self.check_no_pass.isChecked():
            self.check_no_pass.toggle()
        self.txt_info.setText('')                   
    
    def fill_form(self):
        self.empty_form()
        rs = dao_assisted.select_assisted(a, self.index)
        new_values = []            
        for value in rs:
            if value == None:
                item = ''
            else:
                item = value
            new_values.append(item)
                                                                            
        a.code = new_values[0]
        a.name = new_values[1]
        a.date_of_birth = new_values[2]
        a.phone1 = new_values[3]
        a.phone2 = new_values[4]
        a.gender = new_values[5]
        a.civil_state = new_values[6]
        a.ocupation = new_values[7]
        a.lives_with = new_values[8]
        a.address = new_values[9]
        a.neighbourhood = new_values[10]
        a.number = new_values[11]
        a.city = new_values[12]
        a.state = new_values[13]
        a.sedatives = new_values[14]
        a.medical_treatment = new_values[15]
        a.sleep_well = new_values[16]
        a.addictions = new_values[17]
        a.dreams = new_values[18]
        a.work = new_values[19]
        a.family = new_values[20]
        a.feeding = new_values[21]
        a.traits = new_values[22]
        a.latest_treatment = new_values[23]
        a.courses = new_values[24]
        a.fowarding = new_values[25]
        a.treatment = new_values[26]
        a.guidance = new_values[27]                
        
        self.clear_table_view()
        self.fill_table_view()
        
        self.txt_name.setText(a.name)
        self.txt_date.setText(a.date_of_birth)
        self.txt_phone1.setText(a.phone1)
        self.txt_phone2.setText(a.phone2)
        self.cmb_gender.setCurrentText(a.gender)                        
        self.cmb_civil_state.setCurrentText(a.civil_state)                        
        self.txt_ocupation.setText(a.ocupation)
        self.txt_lives_with.setText(a.lives_with)
        self.txt_address.setText(a.address)
        self.txt_neighbourhood.setText(a.neighbourhood)
        self.txt_number.setText(a.number)
        self.txt_city.setText(a.city)
        self.cmb_state.setCurrentText(a.state)                        
                        
        if a.sedatives == 'Não':
            self.radio_sedative_no.toggle()
        else:
            self.radio_sedative_yes.toggle()
        if a.medical_treatment == 'Não':
            self.radio_medical_treatment_no.toggle()
        else:
            self.radio_medical_treatment_yes.toggle()
        if a.sleep_well == 'Não':
            self.radio_sleep_well_no.toggle()
        else:
            self.radio_sleep_well_yes.toggle()
       
            
        if a.addictions.startswith('Não'):
            self.radio_addiction_no.toggle()
        else:
            self.radio_addiction_yes.toggle()
            if a.addictions.find('Álcool') != -1:
                self.check_alcohol.toggle()
            if a.addictions.find('Tabaco') != -1:
                self.check_tobacco.toggle()
            if a.addictions.find('Fumo') != -1:
                self.check_cigarette.toggle()
            if a.addictions.find('Drogas') != -1:
                self.check_drugs.toggle()
            if a.addictions.find('Sexo') != -1:
                self.check_sex.toggle()
                
                                   
        if a.dreams.startswith('SONHO'):
            self.radio_dreams_yes.toggle()            
            self.txt_dreams.setText(a.dreams[7:])
        else:
            self.radio_dreams_no.toggle()        
            self.txt_dreams.setText(a.dreams[9:])
       
       
        self.txt_work.setText(a.work)
        self.txt_family.setText(a.family)
        self.cmb_feeding.setCurrentText(a.feeding)                        
        
        
        if a.traits.find('Depressão aguda') != -1:
            self.check_depression.toggle()
        if a.traits.find('Distúrbios mentais') != -1:
            self.check_mental_disorder.toggle()
        if a.traits.find('Pré-cirurgia') != -1:
            self.check_pre_surgery.toggle()
        if a.traits.find('Pós-cirurgia') != -1:
            self.check_post_surgery.toggle()
        if a.traits.find('Vítima de violência') != -1:
            self.check_victim_of_violence.toggle()
        if a.traits.find('Doença física em fase aguda') != -1:
            self.check_acute_physical_illness.toggle()
        if a.traits.find('Doença grave desconhecida') != -1:
            self.check_unknow_disease.toggle()
        if a.traits.find('Ideia de eliminar alguém') != -1:
            self.check_idea_of_eliminate.toggle()
        if a.traits.find('Veio da Umbanda') != -1:
            self.check_umbanda.toggle()
        if a.traits.find('Desaparecimento') != -1:
            self.check_disappearence.toggle()
        if a.traits.find('Homicida') != -1:
            self.check_homicidal.toggle()
        if a.traits.find('Problema continua') != -1:
            self.check_problem_continues.toggle()
        if a.traits.find('Prática de violência') != -1:
            self.check_violence_practice.toggle()
        if a.traits.find('Doença física grave') != -1:
            self.check_serious_physical_illness.toggle()
        if a.traits.find('Doença mental agressiva') != -1:
            self.check_aggresive_mental_illness.toggle()
        if a.traits.find('Possessão') != -1:
            self.check_possession.toggle()
        if a.traits.find('Problemas graves no lar') != -1:
            self.check_problems_at_home.toggle()
        if a.traits.find('Síndrome do Pânico') != -1:
            self.check_panic_sindrome.toggle()
        if a.traits.find(' --- ') != -1:
            text = a.traits.split(' --- ')
            self.txt_traits.setText(text[1])
        else:
            self.txt_traits.setText(a.traits)
        
        
        self.txt_interviewer.setText('')
        self.cmb_treatment.setCurrentText('NENHUM')        
        self.txt_interview.setText('Clique em <EDITAR> para poder escrever uma entrevista')
        self.btn_save_interview.setEnabled(False)
        
        
        if a.courses.find('Preparatório') != -1:
            self.check_preparatory.toggle()
        if a.courses.find('Básico 1') != -1:
            self.check_basic1.toggle()
        if a.courses.find('Básico 2') != -1:
            self.check_basic2.toggle()
        if a.courses.find('Aprendiz do Evangelho 1') != -1:
            self.check_apprentice1.toggle()
        if a.courses.find('Aprendiz do Evangelho 2') != -1:
            self.check_apprentice2.toggle()
        if a.courses.find('Educação Mediúnica 1') != -1:
            self.check_education1.toggle()
        if a.courses.find('Educação Mediúnica 2') != -1:
            self.check_education2.toggle()
        if a.courses.find('Expositor') != -1:
            self.check_exposer.toggle()
        if a.courses.find('Filosofia') != -1:
            self.check_philosophy.toggle()
            
            
        if a.fowarding.find('Diretoria') != -1:
            self.check_directors.toggle()
        if a.fowarding.find('Depasse') != -1:
            self.check_depass.toggle()
        if a.fowarding.find('Assistente Social') != -1:
            self.check_social_assistant.toggle()
        if a.fowarding.find('Ensino') != -1:
            self.check_teaching.toggle()
        if a.fowarding.find(' --- ') != -1:
            text = a.fowarding.split(' --- ')            
            self.txt_fowarding.setText(text[1])
        else:
            self.txt_fowarding.setText(a.fowarding)
        
        
        if a.treatment.find('Pasteur A2') != -1:
            self.radio_pasteur_a2.toggle()
        if a.treatment.find('Pasteur A4') != -1:
            self.radio_pasteur_a4.toggle()
        if a.treatment.find('Pasteur 1/2') != -1:
            self.radio_pasteur_12.toggle()
        if a.treatment.find('Pasteur A3') != -1:
            self.radio_pasteur_a3.toggle()
        if a.treatment.find('Pasteur 3E3M') != -1:
            self.radio_pasteur_3e3m.toggle()
        if a.treatment.find('Pasteur P3F-Cura') != -1:
            self.radio_pasteur_p3f.toggle()
            
            
        if a.guidance.find('Bons pensamentos') != -1:
            self.check_good_thoughts.toggle()
        if a.guidance.find('Evangelho no lar') != -1:
            self.check_home_gospel.toggle()
        if a.guidance.find('Leituras edificantes') != -1:
            self.check_readings.toggle()
        if a.guidance.find('Médico de confiança') != -1:
            self.check_doctor.toggle()
        if a.guidance.find('Cesta básica') != -1:
            self.check_care_package.toggle()
        if a.guidance.find('Não fazer tratamento') != -1:
            self.check_no_treatment.toggle()
        if a.guidance.find('Higienização do lar') != -1:
            self.check_home_sanitation.toggle()
        if a.guidance.find('Reforma íntima') != -1:
            self.check_intimate_makeover.toggle()
        if a.guidance.find('Estudo da doutrina') != -1:
            self.check_study.toggle()
        if a.guidance.find('Frequência na assistência') != -1:
            self.check_frequency.toggle()
        if a.guidance.find('Não aplicar passe') != -1:
            self.check_no_pass.toggle()
        if a.guidance.find(' --- ') != -1:
            text = a.guidance.split(' --- ')
            self.txt_info.setText(text[1])
        else:
            self.txt_info.setText(a.guidance)
              
    def enable_navigation(self):
        self.txt_index.setEnabled(True)
        

    def disable_navigation(self):
        self.txt_index.setEnabled(False)
        

    def enable_read_only(self):
        self.txt_name.setReadOnly(True)
        self.txt_date.setReadOnly(True)
        self.txt_phone1.setReadOnly(True)
        self.txt_phone2.setReadOnly(True)
        self.cmb_gender.setEnabled(False)
        self.cmb_civil_state.setEnabled(False)
        self.txt_ocupation.setReadOnly(True)
        self.txt_lives_with.setReadOnly(True)
        self.txt_address.setReadOnly(True)
        self.txt_neighbourhood.setReadOnly(True)
        self.txt_number.setReadOnly(True)
        self.txt_city.setReadOnly(True)
        self.cmb_state.setEnabled(False)
        
        self.radio_sedative_yes.setEnabled(False)
        self.radio_sedative_no.setEnabled(False)
        self.radio_medical_treatment_yes.setEnabled(False)
        self.radio_medical_treatment_no.setEnabled(False)
        self.radio_sleep_well_yes.setEnabled(False)
        self.radio_sleep_well_no.setEnabled(False)
        self.radio_addiction_yes.setEnabled(False)
        self.radio_addiction_no.setEnabled(False)        
        self.check_alcohol.setEnabled(False)
        self.check_tobacco.setEnabled(False)
        self.check_cigarette.setEnabled(False)
        self.check_drugs.setEnabled(False)
        self.check_sex.setEnabled(False)
        self.radio_dreams_yes.setEnabled(False)
        self.radio_dreams_no.setEnabled(False)
        self.txt_dreams.setReadOnly(True)
        self.txt_work.setReadOnly(True)
        self.txt_family.setReadOnly(True)
        self.cmb_feeding.setEnabled(False)
        self.check_depression.setEnabled(False)
        self.check_mental_disorder.setEnabled(False)
        self.check_pre_surgery.setEnabled(False)
        self.check_post_surgery.setEnabled(False)
        self.check_victim_of_violence.setEnabled(False)
        self.check_acute_physical_illness.setEnabled(False)
        self.check_unknow_disease.setEnabled(False)
        self.check_idea_of_eliminate.setEnabled(False)
        self.check_umbanda.setEnabled(False)
        self.check_disappearence.setEnabled(False)
        self.check_homicidal.setEnabled(False)
        self.check_problem_continues.setEnabled(False)
        self.check_violence_practice.setEnabled(False)
        self.check_serious_physical_illness.setEnabled(False)
        self.check_aggresive_mental_illness.setEnabled(False)
        self.check_possession.setEnabled(False)
        self.check_problems_at_home.setEnabled(False)
        self.check_panic_sindrome.setEnabled(False)
        self.txt_traits.setReadOnly(True)
        
        self.txt_interviewer.setReadOnly(True)
        self.cmb_treatment.setEnabled(False)
        self.tb_interviews.setEnabled(True)
        self.txt_interview.setReadOnly(True)
        self.btn_save_interview.setEnabled(False)
        self.btn_new_interview.setEnabled(False)
        
        self.check_preparatory.setEnabled(False)
        self.check_basic1.setEnabled(False)
        self.check_basic2.setEnabled(False)
        self.check_apprentice1.setEnabled(False)
        self.check_apprentice2.setEnabled(False)
        self.check_education1.setEnabled(False)
        self.check_education2.setEnabled(False)
        self.check_exposer.setEnabled(False)
        self.check_philosophy.setEnabled(False)
        self.check_directors.setEnabled(False)
        self.check_depass.setEnabled(False)
        self.check_social_assistant.setEnabled(False)
        self.check_teaching.setEnabled(False)
        self.txt_fowarding.setReadOnly(True)
        
        self.radio_pasteur_a2.setEnabled(False)
        self.radio_pasteur_a4.setEnabled(False)  
        self.radio_pasteur_12.setEnabled(False)        
        self.radio_pasteur_a3.setEnabled(False)
        self.radio_pasteur_3e3m.setEnabled(False)
        self.radio_pasteur_p3f.setEnabled(False)
        self.check_good_thoughts.setEnabled(False)
        self.check_home_gospel.setEnabled(False)
        self.check_readings.setEnabled(False)
        self.check_doctor.setEnabled(False)
        self.check_care_package.setEnabled(False)
        self.check_no_treatment.setEnabled(False)
        self.check_home_sanitation.setEnabled(False)
        self.check_intimate_makeover.setEnabled(False)
        self.check_study.setEnabled(False)
        self.check_frequency.setEnabled(False)
        self.check_no_pass.setEnabled(False)
        self.txt_info.setReadOnly(True)
    
    def disable_read_only(self):
        self.txt_name.setReadOnly(False)
        self.txt_date.setReadOnly(False)
        self.txt_phone1.setReadOnly(False)
        self.txt_phone2.setReadOnly(False)
        self.cmb_gender.setEnabled(True)
        self.cmb_civil_state.setEnabled(True)
        self.txt_ocupation.setReadOnly(False)
        self.txt_lives_with.setReadOnly(False)
        self.txt_address.setReadOnly(False)
        self.txt_neighbourhood.setReadOnly(False)
        self.txt_number.setReadOnly(False)
        self.txt_city.setReadOnly(False)
        self.cmb_state.setEnabled(True)
        
        self.radio_sedative_yes.setEnabled(True)
        self.radio_sedative_no.setEnabled(True)
        self.radio_medical_treatment_yes.setEnabled(True)
        self.radio_medical_treatment_no.setEnabled(True)
        self.radio_sleep_well_yes.setEnabled(True)
        self.radio_sleep_well_no.setEnabled(True)
        self.radio_addiction_yes.setEnabled(True)
        self.radio_addiction_no.setEnabled(True)        
        self.check_alcohol.setEnabled(True)
        self.check_tobacco.setEnabled(True)
        self.check_cigarette.setEnabled(True)
        self.check_drugs.setEnabled(True)
        self.check_sex.setEnabled(True)
        self.radio_dreams_yes.setEnabled(True)
        self.radio_dreams_no.setEnabled(True)
        self.txt_dreams.setReadOnly(False)
        self.txt_work.setReadOnly(False)
        self.txt_family.setReadOnly(False)
        self.cmb_feeding.setEnabled(True)
        self.check_depression.setEnabled(True)
        self.check_mental_disorder.setEnabled(True)
        self.check_pre_surgery.setEnabled(True)
        self.check_post_surgery.setEnabled(True)
        self.check_victim_of_violence.setEnabled(True)
        self.check_acute_physical_illness.setEnabled(True)
        self.check_unknow_disease.setEnabled(True)
        self.check_idea_of_eliminate.setEnabled(True)
        self.check_umbanda.setEnabled(True)
        self.check_disappearence.setEnabled(True)
        self.check_homicidal.setEnabled(True)
        self.check_problem_continues.setEnabled(True)
        self.check_violence_practice.setEnabled(True)
        self.check_serious_physical_illness.setEnabled(True)
        self.check_aggresive_mental_illness.setEnabled(True)
        self.check_possession.setEnabled(True)
        self.check_problems_at_home.setEnabled(True)
        self.check_panic_sindrome.setEnabled(True)
        self.txt_traits.setReadOnly(False)
        
        self.txt_interviewer.setReadOnly(True)
        self.cmb_treatment.setEnabled(False)
        self.tb_interviews.setEnabled(True)
        self.txt_interview.setReadOnly(True)
        self.tb_interviews.setEnabled(True)
        self.btn_save_interview.setEnabled(False)
                
        self.check_preparatory.setEnabled(True)
        self.check_basic1.setEnabled(True)
        self.check_basic2.setEnabled(True)
        self.check_apprentice1.setEnabled(True)
        self.check_apprentice2.setEnabled(True)
        self.check_education1.setEnabled(True)
        self.check_education2.setEnabled(True)
        self.check_exposer.setEnabled(True)
        self.check_philosophy.setEnabled(True)
        self.check_directors.setEnabled(True)
        self.check_depass.setEnabled(True)
        self.check_social_assistant.setEnabled(True)
        self.check_teaching.setEnabled(True)
        self.txt_fowarding.setReadOnly(False)
        
        self.radio_pasteur_a2.setEnabled(True)
        self.radio_pasteur_a4.setEnabled(True)  
        self.radio_pasteur_12.setEnabled(True)        
        self.radio_pasteur_a3.setEnabled(True)
        self.radio_pasteur_3e3m.setEnabled(True)
        self.radio_pasteur_p3f.setEnabled(True)
        self.check_good_thoughts.setEnabled(True)
        self.check_home_gospel.setEnabled(True)
        self.check_readings.setEnabled(True)
        self.check_doctor.setEnabled(True)
        self.check_care_package.setEnabled(True)
        self.check_no_treatment.setEnabled(True)
        self.check_home_sanitation.setEnabled(True)
        self.check_intimate_makeover.setEnabled(True)
        self.check_study.setEnabled(True)
        self.check_frequency.setEnabled(True)
        self.check_no_pass.setEnabled(True)
        self.txt_info.setReadOnly(False)    
      
    def action_buttons(self):
        if dao_assisted.id_gen_assisted() - 1 == 0:
            self.btn_add.setEnabled(True)
            self.btn_backups.setEnabled(True)
            self.btn_log_out.setEnabled(True)
            self.btn_cancel.setEnabled(False)
            self.btn_print.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.btn_edit.setEnabled(False)
            self.btn_report.setEnabled(False)
            self.btn_delete.setEnabled(False)
        else:
            self.btn_add.setEnabled(True)
            self.btn_backups.setEnabled(True)
            self.btn_log_out.setEnabled(True)
            self.btn_cancel.setEnabled(False)
            self.btn_print.setEnabled(True)
            self.btn_save.setEnabled(False)
            self.btn_edit.setEnabled(True)
            self.btn_report.setEnabled(True)
            self.btn_delete.setEnabled(True)
        

    def get_values(self, a):
        addictions = ''
        dreams = ''
        traits = ''
        courses = ''
        fowarding = ''
        treatments = ''
        guidance = ''
        
        a.code = dao_assisted.id_gen_assisted()
        
        a.name = self.txt_name.text().strip().upper()
        a.date_of_birth = self.txt_date.text().strip()
        a.phone1 = self.txt_phone1.text().strip() if len(self.txt_phone1.text().strip()) >= 15 else ''
        a.phone2 = self.txt_phone2.text().strip() if len(self.txt_phone2.text().strip()) >= 14 else ''
        a.gender = self.cmb_gender.currentText()
        a.civil_state = self.cmb_civil_state.currentText()
        a.ocupation = self.txt_ocupation.text().strip().upper()
        a.lives_with = self.txt_lives_with.text().strip().upper()
        a.address = self.shorten_places(self.txt_address.text().strip().upper())
        a.neighbourhood = self.shorten_places(self.txt_neighbourhood.text().strip().upper())
        a.number = self.txt_number.text().strip().upper()
        a.city = self.txt_city.text().strip().upper()
        a.state = self.cmb_state.currentText()
        a.sedatives = 'Sim' if self.radio_sedative_yes.isChecked() else 'Não'
        a.medical_treatment = 'Sim' if self.radio_medical_treatment_yes.isChecked() else 'Não'
        a.sleep_well = 'Sim' if self.radio_sleep_well_yes.isChecked() else 'Não'
        
        
        if self.radio_addiction_yes.isChecked():
            addictions = 'Sim'
            if self.check_alcohol.isChecked():
                addictions += ', Álcool'
            if self.check_tobacco.isChecked():
                addictions += ', Tabaco'
            if self.check_cigarette.isChecked():
                addictions += ', Fumo'
            if self.check_drugs.isChecked():
                addictions += ', Drogas'
            if self.check_sex.isChecked():
                addictions += ', Sexo'
        else:
            addictions = 'Não'        
        a.addictions = addictions
        
        
        if self.radio_dreams_yes.isChecked():
            dreams = 'SONHO, '
        else:
            dreams = 'PESADELO, '
        dreams += self.txt_dreams.toPlainText().strip()
        if dreams.endswith(', '):
            dreams = dreams[:-2]
        a.dreams = dreams
        
        
        a.work = self.txt_work.toPlainText().strip()
        a.family = self.txt_family.toPlainText().strip()
        a.feeding = self.cmb_feeding.currentText()
        
        
        if self.check_depression.isChecked():
            traits += 'Depressão aguda, '
        if self.check_mental_disorder.isChecked():
            traits += 'Distúrbios mentais, '
        if self.check_pre_surgery.isChecked():
            traits += 'Pré-cirurgia, '            
        if self.check_post_surgery.isChecked():
            traits += 'Pós-cirurgia, '
        if self.check_victim_of_violence.isChecked():
            traits += 'Vítima de violência, '
        if self.check_acute_physical_illness.isChecked():
            traits += 'Doença física em fase aguda, '
        if self.check_unknow_disease.isChecked():
            traits += 'Doença grave desconhecida, '
        if self.check_idea_of_eliminate.isChecked():
            traits += 'Ideia de eliminar alguém, '
        if self.check_umbanda.isChecked():
            traits += 'Veio da Umbanda, '
        if self.check_disappearence.isChecked():
            traits += 'Desaparecimento, '
        if self.check_homicidal.isChecked():
            traits += 'Homicida, '
        if self.check_problem_continues.isChecked():
            traits += 'Problema continua, '
        if self.check_violence_practice.isChecked():
            traits += 'Prática de violência, '
        if self.check_serious_physical_illness.isChecked():
            traits += 'Doença física grave, '
        if self.check_aggresive_mental_illness.isChecked():
            traits += 'Doença mental agressiva, '
        if self.check_possession.isChecked():
            traits += 'Possessão, '
        if self.check_problems_at_home.isChecked():
            traits += 'Problemas graves no lar, '
        if self.check_panic_sindrome.isChecked():
            traits += 'Síndrome do pânico'
        if traits.endswith(', '):
            traits = traits[:-2]
        traits += ' --- '      
        if traits.startswith(' --- '):
            traits = traits[5:]
        traits += self.txt_traits.toPlainText().strip()
        a.traits = traits
        
        
        if self.adding == True:
            a.latest_treatment = 'NENHUM'
        else:
            a.latest_treatment = self.cmb_treatment.currentText()
        
        
        if self.check_preparatory.isChecked():
            courses += 'Preparatório, '
        if self.check_basic1.isChecked():
            courses += 'Básico 1, '
        if self.check_basic2.isChecked():
            courses += 'Básico 2, '
        if self.check_apprentice1.isChecked():
            courses += 'Aprendiz do Evangelho 1, '
        if self.check_apprentice2.isChecked():
            courses += 'Aprendiz do Evangelho 2, '
        if self.check_education1.isChecked():
            courses += 'Educação Mediúnica 1, '
        if self.check_education2.isChecked():
            courses += 'Educação Mediúnica 2, '
        if self.check_exposer.isChecked():
            courses += 'Expositor, '
        if self.check_philosophy.isChecked():
            courses += 'Filosofia'
        if courses.endswith(', '):
            courses = courses[:-2]
        a.courses = courses
            
            
        if self.check_directors.isChecked():
            fowarding += 'Diretoria, '
        if self.check_depass.isChecked():
            fowarding += 'Depasse, '
        if self.check_social_assistant.isChecked():
            fowarding += 'Assistente Social, '
        if self.check_teaching.isChecked():
            fowarding += 'Ensino'
        if fowarding.endswith(', '):
            fowarding = fowarding[:-2]
        fowarding += ' --- '
        if fowarding.startswith(' --- '):
            fowarding = fowarding[5:]            
        fowarding += self.txt_fowarding.toPlainText().strip()
        a.fowarding = fowarding
        
        
        if self.radio_pasteur_a2.isChecked():
            treatments += 'Pasteur A2, '
        if self.radio_pasteur_a4.isChecked():
            treatments += 'Pasteur A4, '
        if self.radio_pasteur_12.isChecked():
            treatments += 'Pasteur 1/2, '
        if self.radio_pasteur_a3.isChecked():
            treatments += 'Pasteur A3, '
        if self.radio_pasteur_3e3m.isChecked():
            treatments += 'Pasteur 3E3M, '
        if self.radio_pasteur_p3f.isChecked():
            treatments += 'Pasteur P3F-Cura'
        if treatments.endswith(', '):
            treatments = treatments[:-2]
        a.treatment = treatments
        
               
        if self.check_good_thoughts.isChecked():
            guidance += 'Bons pensamentos, '
        if self.check_home_gospel.isChecked():
            guidance += 'Evangelho no lar, '
        if self.check_readings.isChecked():
            guidance += 'Leituras edificantes, '
        if self.check_doctor.isChecked():
            guidance += 'Médico de confiança, '
        if self.check_care_package.isChecked():
            guidance += 'Cesta básica, '
        if self.check_no_treatment.isChecked():
            guidance += 'Não fazer tratamento, '
        if self.check_home_sanitation.isChecked():
            guidance += 'Higienização do lar, '
        if self.check_intimate_makeover.isChecked():
            guidance += 'Reforma íntima, '
        if self.check_study.isChecked():
            guidance += 'Estudo da doutrina, '
        if self.check_frequency.isChecked():
            guidance += 'Frequência na assistência, '
        if self.check_no_pass.isChecked():
            guidance += 'Não aplicar passe'
        if guidance.endswith(', '):
            guidance = guidance[:-2]
        guidance += ' --- '
        if guidance.startswith(' --- '):
            guidance = guidance[5:]
        guidance += self.txt_info.toPlainText().strip()
        a.guidance = guidance
    
    def check_date(self, data):
        import datetime
        
        today = datetime.datetime.now()        
        
        date = data.split('/')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        
        if year >= today.year:
            return False
        else:
            if month > 12 or month < 1:
                return False
            else:
                if day < 1:
                    return False
                else:
                    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                        if day > 31:
                            return False
                    elif month == 2:
                        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                            if day > 29:
                                return False
                        else:
                            if day > 28:
                                return False
                    else:
                        if day > 30:
                            return False
        return True
    
    def test_mandatory_fields(self):
        self.error_message = ''
        
        if len(self.txt_name.text().strip()) < 3:
            self.error_message += '- NOME inválido\n'
        if len(self.txt_date.text().strip()) < 10:
            self.error_message += '- DATA DE NASCIMENTO inválida\n'
        else:            
            if not self.check_date(self.txt_date.text().strip()):
                self.error_message += '- DATA DE NASCIMENTO inválida\n'
        if len(self.txt_phone1.text().strip()) < 15 and len(self.txt_phone2.text().strip()) < 14:
            self.error_message += '- TELEFONES inválidos\n'
        if len(self.txt_address.text().strip()) < 3:
            self.error_message += '- ENDEREÇO inválido\n'
        if len(self.txt_neighbourhood.text().strip()) < 3:
            self.error_message += '- BAIRRO inválido\n'
        if len(self.txt_number.text().strip()) < 1:
            self.error_message += '- NÚMERO inválido\n'
        if len(self.txt_city.text().strip()) < 3:
            self.error_message += '- CIDADE inválida'
        
        if len(self.error_message) < 1:
            return True
        else:
            return False
    
    def shorten_places(self, text):
        places = ['ALAMEDA', 'AVENIDA', 'BECO', 'BLOCO', 'BOSQUE', 'CONDOMÍNIO', 'CONJUNTO HABITACIONAL', 'FAVELA', 'FAZENDA', 'JARDIM', 'LAGO', 'LAGOA', 'LARGO', 'MORRO', 'PARQUE', 'RECANTO', 'RUA', 'TRAVESSA', 'VIELA', 'VILA']        
        shortened = ['AL.', 'AV.', 'BC.', 'BL.', 'BSQ.', 'COND.', 'COHAB.', 'FAV.', 'FAZ.', 'JD.', 'LG.', 'LGA.', 'LRG.', 'MRO.', 'PRQ.','REC.', 'R.', 'TV.', 'VLA.', 'VL.']

        i = 0
        txt = text
        while i < len(shortened):
            if text.startswith(places[i]):                
                txt = text.replace(places[i], shortened[i], 1)                
            i += 1
        return txt
    
    def fill_table_view(self):
        query_result = dao_interview.select_interview(a)        
 
        for value in query_result:
            row = []
            for item in value:
                cell = QtGui.QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)     

    def clear_table_view(self):
        self.model.removeRows(0, self.model.rowCount())
    
    def save_changes(self):                  
        rs = dao_assisted.select_assisted(a, self.index)
        for value in rs:
            if value == None:
                item = ''
            else:
                item = value
            self.old_values.append(item)
    
    def check_changes(self):
        fields = ['Codigo', 'Nome, ', 'Data de Nascimento, ', 'Telefone (celular), ', 'Telefone (residencial), ', 'Gênero, ', 'Estado civil, ', 'Ocupação, ', 'Reside com, ', 'Endereço, ', 'Bairro, ', 'Número, ', 'Cidade, ', 'Estado, ', 'Toma sedativos, ', 'Tratamento médico, ', 'Dorme bem, ', 'Vícios, ', 'Sonhos, ', 'Trabalho, ', 'Família, ', 'Alimentação, ', 'Info para DEPOE, ', 'Ultimo tratamento, ', 'Cursos, ', 'Encaminhamento, ', 'Tratamentos, ', 'Orientação Espiritual']
        new_values = []
        
        rs = dao_assisted.select_assisted(a, self.index)
        for value in rs:
            if value == None:
                item = ''
            else:
                item = value
            new_values.append(item)               
            
        i = 1
        text = ''
        while i < len(fields):
            if fields[i] != 'Ultimo tratamento, ':
                if self.old_values[i] != new_values[i]:
                    text += fields[i]
            i += 1
            
        if text.endswith(', '):
            text = text[:-2]

        return text
    

    def index_changed(self):
        if self.txt_index.value() != 0:
            self.index = self.txt_index.value()
            self.fill_form()
        
    ####################################################
    # BUTTONS METHODS    
    ####################################################
    def btn_log_out_clicked(self):
        this_window = QtWidgets.QApplication.activeWindow()
        
        root = tkinter.Tk()
        root.withdraw()
        choice = messagebox.askquestion('SAIR DO SISTEMA', 'Deseja sair do sistema?')
        tkinter.Tk().destroy()
                
        if choice == 'yes':
            from form_login import Ui_FormLogin
            dao_user.set_off()
            dao_user.gen_historic()
            this_window.close()       
            self.FormLogin = QtWidgets.QMainWindow()
            self.ui = Ui_FormLogin()
            self.ui.setupUi(self.FormLogin)
            self.FormLogin.show()
    
    def btn_reports_clicked(self):
        from form_reports import Ui_FormReports                
        self.FormReports = QtWidgets.QMainWindow()
        self.ui = Ui_FormReports()
        self.ui.setupUi(self.FormReports)
        self.FormReports.show()

    def btn_backups_clicked(self):
        from form_backups import Ui_FormBackup
        self.FormBackup = QtWidgets.QMainWindow()
        self.ui = Ui_FormBackup()
        self.ui.setupUi(self.FormBackup)
        self.FormBackup.show()
            
    def btn_add_clicked(self):
        self.disable_read_only()
        self.empty_form()        
        self.disable_navigation()                
        self.clear_table_view()    
        
        self.txt_interviewer.setReadOnly(True)
        self.txt_interview.setReadOnly(True)
        self.cmb_treatment.setEnabled(False)
        self.tb_interviews.setEnabled(False)
                
        self.adding = True
        
        self.txt_name.setFocus()
        self.btn_add.setEnabled(False)
        self.btn_backups.setEnabled(False)
        self.btn_log_out.setEnabled(False)
        self.btn_cancel.setEnabled(True)
        self.btn_print.setEnabled(False)
        self.btn_save.setEnabled(True)
        self.btn_edit.setEnabled(False)
        self.btn_report.setEnabled(False)
        self.btn_delete.setEnabled(False)   
    
    def btn_cancel_clicked(self):
        self.enable_read_only()
        self.enable_navigation()
        self.action_buttons()        
        
        self.adding = False
        self.editing = False
        
        if self.writing_interview:
            self.btn_new_interview_clicked()
        
        if dao_assisted.id_gen_assisted() - 1 <= 0:
            self.empty_form()
        else:
            self.fill_form()
      
    def btn_save_clicked(self):
        if not self.test_mandatory_fields():
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', 'Não foi possível concluir o salvamento devido os seguintes erros:\n\n' + self.error_message)
            tkinter.Tk().destroy()
        else:
            root = tkinter.Tk()
            root.withdraw()
            choice = messagebox.askquestion('SALVAR MODIFICAÇÕES', 'Deseja salvar as alterações feitas?')
            tkinter.Tk().destroy()
            
            if choice == 'yes':
                historic_message = ''                
                
                if self.adding == True and self.editing == False:
                    self.get_values(a)
                    historic_message = 'ADICIONOU o registro de <{}>'.format(self.txt_name.text().strip().upper())
                    dao_assisted.insert_assisted(a)
                    dao_user.register_changes(u.name, historic_message)
                    self.txt_index.setMaximum(dao_assisted.id_gen_assisted() - 1)
                    self.adding = False      
                elif self.editing == True and self.adding == False:
                    self.save_changes()
                    self.get_values(a)
                    a.code = a.code - 1
                    dao_assisted.edit_assisted(a)
                    historic_message = 'EDITOU no registro de <{}>: '.format(self.txt_name.text().strip().upper())
                    historic_message += self.check_changes()   
                    dao_user.register_changes(u.name, historic_message)
                    self.editing = False
                    self.fill_form()
                
                self.btn_cancel_clicked()
                                    
    def btn_delete_clicked(self):
        root = tkinter.Tk()
        root.withdraw()
        choice = messagebox.askquestion('DELETAR REGISTRO', 'Deseja DELETAR o registro de <{}>?'.format(a.name))
        tkinter.Tk().destroy()
        
        if choice == 'yes':
            self.clear_table_view()
            dao_assisted.delete_assisted(self.index)
            historic_message = f'DELETOU o registro de <{a.name}>'
            dao_user.register_changes(u.name, historic_message)
            if dao_assisted.id_gen_assisted() - 1 == 0:
                self.txt_index.setMaximum(0)
                self.txt_index.setMinimum(0)
                self.empty_form()
                self.action_buttons()
            else:
                self.txt_index.setMaximum(dao_assisted.id_gen_assisted() - 1)
                if self.index > dao_assisted.id_gen_assisted() - 1:
                    self.index -= 1
                elif self.index < dao_assisted.id_gen_assisted() - 1:
                    self.index += 1                    
                else:
                    self.index = self.index
                self.txt_index.setValue(self.index)
                    
                self.fill_form()
                self.action_buttons()
                                                  
    def btn_edit_clicked(self):
        self.disable_navigation()
        self.disable_read_only()
        
        self.editing = True
        self.btn_new_interview.setEnabled(True)
        
        self.txt_interview.setText('Clique em <NOVA ENTREVISTA> para escrever uma entrevista')

        self.txt_name.setFocus()
        self.btn_add.setEnabled(False)
        self.btn_backups.setEnabled(False)
        self.btn_log_out.setEnabled(False)
        self.btn_cancel.setEnabled(True)
        self.btn_print.setEnabled(False)
        self.btn_save.setEnabled(True)
        self.btn_edit.setEnabled(False)
        self.btn_report.setEnabled(False)
        self.btn_delete.setEnabled(False)
        
    def btn_print_clicked(self):
        if dao_interview.count_interviews(a) > 2:
            root = tkinter.Tk()
            root.withdraw()
            choice = messagebox.askquestion('IMPRESSÃO', 'Parece que esse registro possui três ou mais entrevistas.\nDeseja imprimir apenas as entrevistas mais recentes?')
            tkinter.Tk().destroy()
            
            if choice == 'yes':
                dao_interview.print_interviews(a)
            else:
                dao_assisted.print_register(a)
        else:
            dao_assisted.print_register(a)
            
    def radio_addictions_no_toggled(self):
        if self.check_alcohol.isChecked():
            self.check_alcohol.toggle()
        if self.check_tobacco.isChecked():
            self.check_tobacco.toggle()
        if self.check_cigarette.isChecked():
            self.check_cigarette.toggle()
        if self.check_drugs.isChecked():
            self.check_drugs.toggle()
        if self.check_sex.isChecked():
            self.check_sex.toggle()
        self.check_alcohol.setEnabled(False)
        self.check_tobacco.setEnabled(False)
        self.check_cigarette.setEnabled(False)
        self.check_drugs.setEnabled(False)
        self.check_sex.setEnabled(False)
    
    def radio_addictions_yes_toggled(self):
        if self.check_alcohol.isChecked():
            self.check_alcohol.toggle()
        if self.check_tobacco.isChecked():
            self.check_tobacco.toggle()
        if self.check_cigarette.isChecked():
            self.check_cigarette.toggle()
        if self.check_drugs.isChecked():
            self.check_drugs.toggle()
        if self.check_sex.isChecked():
            self.check_sex.toggle()
        self.check_alcohol.setEnabled(True)
        self.check_tobacco.setEnabled(True)
        self.check_cigarette.setEnabled(True)
        self.check_drugs.setEnabled(True)
        self.check_sex.setEnabled(True)

    def btn_new_interview_clicked(self):
        self.tb_interviews.setEnabled(False)
        if not self.writing_interview:
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("images/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_new_interview.setIcon(new_icon)
            self.btn_new_interview.setText('CANCELAR')
            
            self.btn_save.setEnabled(False)
            self.btn_cancel.setEnabled(False)

            self.tab_personal_data.setEnabled(False)
            self.tab_extra_info.setEnabled(False)
            self.tab_fowarding.setEnabled(False)
            self.tab_guidance.setEnabled(False)

            # self.txt_interviewer.setReadOnly(False)
            self.cmb_treatment.setEnabled(True)
            self.txt_interview.setReadOnly(False)
            self.btn_save_interview.setEnabled(True)
            self.btn_new_interview.setEnabled(True)
            
            self.txt_interview.setFocus(True)
            self.txt_interviewer.setText(u.name)
            self.txt_interview.setText('')

            self.writing_interview = True
        else:
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("images/edit-3.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_new_interview.setIcon(new_icon)
            self.btn_new_interview.setText('NOVA ENTREVISTA')
            
            self.btn_save.setEnabled(True)
            self.btn_cancel.setEnabled(True)            
            
            self.tab_personal_data.setEnabled(True)
            self.tab_extra_info.setEnabled(True)
            self.tab_fowarding.setEnabled(True)
            self.tab_guidance.setEnabled(True)
            
            self.txt_interviewer.setReadOnly(True)
            self.cmb_treatment.setEnabled(False)
            self.txt_interview.setReadOnly(True)
            self.btn_save_interview.setEnabled(False)
            self.btn_new_interview.setEnabled(True)
            
            self.writing_interview = False

    def btn_save_interview_clicked(self):
        if len(self.txt_interviewer.text().strip()) < 1 or len(self.txt_interview.toPlainText().strip()) < 1:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', 'Os campos ENTREVISTADOR e ENTREVISTA precisam estar PREENCHIDOS')        
            tkinter.Tk().destroy()        
        else:
            root = tkinter.Tk()
            root.withdraw()
            choice = messagebox.askquestion('REGISTRAR ENTREVISTA', 'Deseja registrar esta entrevista?')
            tkinter.Tk().destroy()
        
            if choice == 'yes':                
                from datetime import datetime            
                today = datetime.now().strftime('%d/%m/%Y')
                
                i.code = dao_interview.id_gen_interview()
                i.date = today
                i.interviewer = self.txt_interviewer.text().strip().upper()
                i.treatment = self.cmb_treatment.currentText()
                i.interview = self.txt_interview.toPlainText().strip()
                
                dao_interview.insert_interview(i, a)
                historic_message = 'Adicionou uma ENTREVISTA ao registro de <{}>'.format(self.txt_name.text().strip().upper())
                dao_user.register_changes(u.name, historic_message)                
                self.btn_new_interview_clicked()
                self.clear_table_view()
                self.fill_table_view()                                
                self.tabWidget.setCurrentIndex(4)

    def cell_double_clicked(self, signal):
        row = signal.row()
        values = []
        
        for i in range(4):
            index = signal.sibling(row , i)
            index_dict = self.model.itemData(index)
            values.append(index_dict.get(0))
            
        self.txt_interviewer.setText(values[1])
        self.cmb_treatment.setCurrentText(values[2])
        self.txt_interview.setPlainText(values[3])                            
    
        

    def setupUi(self, FormFicha):
        FormFicha.setObjectName("FormFicha")
        FormFicha.resize(952, 743)
        self.centralwidget = QtWidgets.QWidget(FormFicha)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_index = QtWidgets.QSpinBox(self.centralwidget)
        self.txt_index.setObjectName("txt_index")
        self.gridLayout.addWidget(self.txt_index, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 175))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 175))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_add = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/plus-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_3.addWidget(self.btn_add, 0, 0, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_3.addWidget(self.btn_save, 0, 1, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon2)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_3.addWidget(self.btn_cancel, 0, 2, 1, 1)
        self.btn_edit = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_edit.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit.setIcon(icon3)
        self.btn_edit.setObjectName("btn_edit")
        self.gridLayout_3.addWidget(self.btn_edit, 1, 0, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon4)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout_3.addWidget(self.btn_delete, 1, 1, 1, 1)
        self.btn_print = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_print.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/printer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_print.setIcon(icon5)
        self.btn_print.setObjectName("btn_print")
        self.gridLayout_3.addWidget(self.btn_print, 1, 2, 1, 1)
        self.btn_report = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_report.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_report.setIcon(icon6)
        self.btn_report.setObjectName("btn_report")
        self.gridLayout_3.addWidget(self.btn_report, 2, 0, 1, 1)
        self.btn_backups = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_backups.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_backups.setIcon(icon7)
        self.btn_backups.setObjectName("btn_backups")
        self.gridLayout_3.addWidget(self.btn_backups, 2, 1, 1, 1)
        self.btn_log_out = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_log_out.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_log_out.setIcon(icon8)
        self.btn_log_out.setObjectName("btn_log_out")
        self.gridLayout_3.addWidget(self.btn_log_out, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_personal_data = QtWidgets.QWidget()
        self.tab_personal_data.setObjectName("tab_personal_data")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_personal_data)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.txt_name = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_name.setFont(font)
        self.txt_name.setObjectName("txt_name")
        self.gridLayout_4.addWidget(self.txt_name, 0, 1, 1, 9)
        self.label_5 = QtWidgets.QLabel(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 5)
        self.label_6 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 6, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 1, 9, 1, 1)
        self.txt_phone1 = QtWidgets.QLineEdit(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_phone1.sizePolicy().hasHeightForWidth())
        self.txt_phone1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_phone1.setFont(font)
        self.txt_phone1.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_phone1.setObjectName("txt_phone1")
        self.gridLayout_4.addWidget(self.txt_phone1, 2, 5, 1, 1)
        self.txt_phone2 = QtWidgets.QLineEdit(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_phone2.sizePolicy().hasHeightForWidth())
        self.txt_phone2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_phone2.setFont(font)
        self.txt_phone2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_phone2.setObjectName("txt_phone2")
        self.gridLayout_4.addWidget(self.txt_phone2, 2, 6, 1, 1)
        self.cmb_gender = QtWidgets.QComboBox(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_gender.sizePolicy().hasHeightForWidth())
        self.cmb_gender.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.cmb_gender.setFont(font)
        self.cmb_gender.setObjectName("cmb_gender")
        self.cmb_gender.addItem("")
        self.cmb_gender.addItem("")
        self.cmb_gender.addItem("")
        self.gridLayout_4.addWidget(self.cmb_gender, 2, 7, 1, 2)
        self.cmb_civil_state = QtWidgets.QComboBox(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_civil_state.sizePolicy().hasHeightForWidth())
        self.cmb_civil_state.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.cmb_civil_state.setFont(font)
        self.cmb_civil_state.setObjectName("cmb_civil_state")
        self.cmb_civil_state.addItem("")
        self.cmb_civil_state.addItem("")
        self.cmb_civil_state.addItem("")
        self.cmb_civil_state.addItem("")
        self.gridLayout_4.addWidget(self.cmb_civil_state, 2, 9, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 3, 0, 1, 3)
        self.label_22 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 4, 0, 1, 3)
        self.label_23 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 5, 0, 1, 2)
        self.label_24 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 6, 0, 1, 2)
        self.txt_number = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_number.setFont(font)
        self.txt_number.setObjectName("txt_number")
        self.gridLayout_4.addWidget(self.txt_number, 6, 9, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 7, 0, 1, 2)
        self.label_39 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout_4.addWidget(self.label_39, 7, 7, 1, 1)
        self.cmb_state = QtWidgets.QComboBox(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.cmb_state.setFont(font)
        self.cmb_state.setObjectName("cmb_state")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.cmb_state.addItem("")
        self.gridLayout_4.addWidget(self.cmb_state, 7, 8, 1, 2)
        self.txt_date = QtWidgets.QLineEdit(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_date.sizePolicy().hasHeightForWidth())
        self.txt_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_date.setFont(font)
        self.txt_date.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_date.setObjectName("txt_date")
        self.gridLayout_4.addWidget(self.txt_date, 2, 0, 1, 5)
        self.label_8 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 7, 1, 2)
        self.txt_ocupation = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_ocupation.setFont(font)
        self.txt_ocupation.setObjectName("txt_ocupation")
        self.gridLayout_4.addWidget(self.txt_ocupation, 3, 3, 1, 7)
        self.txt_lives_with = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_lives_with.setFont(font)
        self.txt_lives_with.setObjectName("txt_lives_with")
        self.gridLayout_4.addWidget(self.txt_lives_with, 4, 3, 1, 7)
        self.txt_address = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_address.setFont(font)
        self.txt_address.setObjectName("txt_address")
        self.gridLayout_4.addWidget(self.txt_address, 5, 3, 1, 7)
        self.label_25 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 6, 8, 1, 1)
        self.txt_neighbourhood = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_neighbourhood.setFont(font)
        self.txt_neighbourhood.setObjectName("txt_neighbourhood")
        self.gridLayout_4.addWidget(self.txt_neighbourhood, 6, 2, 1, 6)
        self.txt_city = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_city.setFont(font)
        self.txt_city.setObjectName("txt_city")
        self.gridLayout_4.addWidget(self.txt_city, 7, 2, 1, 5)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_personal_data, icon9, "")
        self.tab_extra_info = QtWidgets.QWidget()
        self.tab_extra_info.setObjectName("tab_extra_info")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_extra_info)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cmb_feeding = QtWidgets.QComboBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_feeding.sizePolicy().hasHeightForWidth())
        self.cmb_feeding.setSizePolicy(sizePolicy)
        self.cmb_feeding.setObjectName("cmb_feeding")
        self.cmb_feeding.addItem("")
        self.cmb_feeding.addItem("")
        self.cmb_feeding.addItem("")
        self.gridLayout_5.addWidget(self.cmb_feeding, 4, 1, 1, 5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radio_sedative_yes = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_sedative_yes.setFont(font)
        self.radio_sedative_yes.setObjectName("radio_sedative_yes")
        self.verticalLayout.addWidget(self.radio_sedative_yes)
        self.radio_sedative_no = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_sedative_no.setFont(font)
        self.radio_sedative_no.setObjectName("radio_sedative_no")
        self.verticalLayout.addWidget(self.radio_sedative_no)
        self.gridLayout_5.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.txt_family = QtWidgets.QTextEdit(self.groupBox_10)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_family.setFont(font)
        self.txt_family.setObjectName("txt_family")
        self.gridLayout_13.addWidget(self.txt_family, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_10, 3, 3, 1, 3)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.txt_work = QtWidgets.QTextEdit(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_work.setFont(font)
        self.txt_work.setObjectName("txt_work")
        self.gridLayout_12.addWidget(self.txt_work, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_9, 3, 0, 1, 3)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_extra_info)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.radio_dreams_yes = QtWidgets.QRadioButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_dreams_yes.setFont(font)
        self.radio_dreams_yes.setObjectName("radio_dreams_yes")
        self.gridLayout_9.addWidget(self.radio_dreams_yes, 0, 0, 1, 1)
        self.txt_dreams = QtWidgets.QTextEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_dreams.sizePolicy().hasHeightForWidth())
        self.txt_dreams.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_dreams.setFont(font)
        self.txt_dreams.setObjectName("txt_dreams")
        self.gridLayout_9.addWidget(self.txt_dreams, 0, 1, 2, 1)
        self.radio_dreams_no = QtWidgets.QRadioButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_dreams_no.setFont(font)
        self.radio_dreams_no.setObjectName("radio_dreams_no")
        self.gridLayout_9.addWidget(self.radio_dreams_no, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_8, 2, 0, 1, 6)
        self.label_40 = QtWidgets.QLabel(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.gridLayout_5.addWidget(self.label_40, 4, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.check_tobacco = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_tobacco.setFont(font)
        self.check_tobacco.setObjectName("check_tobacco")
        self.gridLayout_10.addWidget(self.check_tobacco, 1, 1, 1, 1)
        self.radio_addiction_yes = QtWidgets.QRadioButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_addiction_yes.setFont(font)
        self.radio_addiction_yes.setObjectName("radio_addiction_yes")
        self.gridLayout_10.addWidget(self.radio_addiction_yes, 0, 0, 1, 1)
        self.check_alcohol = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_alcohol.setFont(font)
        self.check_alcohol.setObjectName("check_alcohol")
        self.gridLayout_10.addWidget(self.check_alcohol, 0, 1, 1, 1)
        self.check_drugs = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_drugs.setFont(font)
        self.check_drugs.setObjectName("check_drugs")
        self.gridLayout_10.addWidget(self.check_drugs, 1, 2, 1, 1)
        self.radio_addiction_no = QtWidgets.QRadioButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_addiction_no.setFont(font)
        self.radio_addiction_no.setObjectName("radio_addiction_no")
        self.gridLayout_10.addWidget(self.radio_addiction_no, 1, 0, 1, 1)
        self.check_cigarette = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_cigarette.setFont(font)
        self.check_cigarette.setObjectName("check_cigarette")
        self.gridLayout_10.addWidget(self.check_cigarette, 0, 2, 1, 1)
        self.check_sex = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_sex.setFont(font)
        self.check_sex.setObjectName("check_sex")
        self.gridLayout_10.addWidget(self.check_sex, 0, 3, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_7, 1, 0, 1, 6)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.check_depression = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_depression.sizePolicy().hasHeightForWidth())
        self.check_depression.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_depression.setFont(font)
        self.check_depression.setObjectName("check_depression")
        self.gridLayout_11.addWidget(self.check_depression, 0, 0, 1, 1)
        self.check_disappearence = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_disappearence.sizePolicy().hasHeightForWidth())
        self.check_disappearence.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_disappearence.setFont(font)
        self.check_disappearence.setObjectName("check_disappearence")
        self.gridLayout_11.addWidget(self.check_disappearence, 0, 1, 1, 1)
        self.check_mental_disorder = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_mental_disorder.sizePolicy().hasHeightForWidth())
        self.check_mental_disorder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_mental_disorder.setFont(font)
        self.check_mental_disorder.setObjectName("check_mental_disorder")
        self.gridLayout_11.addWidget(self.check_mental_disorder, 1, 0, 1, 1)
        self.check_homicidal = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_homicidal.sizePolicy().hasHeightForWidth())
        self.check_homicidal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_homicidal.setFont(font)
        self.check_homicidal.setObjectName("check_homicidal")
        self.gridLayout_11.addWidget(self.check_homicidal, 1, 1, 1, 1)
        self.check_pre_surgery = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_pre_surgery.sizePolicy().hasHeightForWidth())
        self.check_pre_surgery.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_pre_surgery.setFont(font)
        self.check_pre_surgery.setObjectName("check_pre_surgery")
        self.gridLayout_11.addWidget(self.check_pre_surgery, 2, 0, 1, 1)
        self.check_problem_continues = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_problem_continues.sizePolicy().hasHeightForWidth())
        self.check_problem_continues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_problem_continues.setFont(font)
        self.check_problem_continues.setObjectName("check_problem_continues")
        self.gridLayout_11.addWidget(self.check_problem_continues, 2, 1, 1, 1)
        self.check_post_surgery = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_post_surgery.sizePolicy().hasHeightForWidth())
        self.check_post_surgery.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_post_surgery.setFont(font)
        self.check_post_surgery.setObjectName("check_post_surgery")
        self.gridLayout_11.addWidget(self.check_post_surgery, 3, 0, 1, 1)
        self.check_violence_practice = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_violence_practice.sizePolicy().hasHeightForWidth())
        self.check_violence_practice.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_violence_practice.setFont(font)
        self.check_violence_practice.setObjectName("check_violence_practice")
        self.gridLayout_11.addWidget(self.check_violence_practice, 3, 1, 1, 1)
        self.check_victim_of_violence = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_victim_of_violence.sizePolicy().hasHeightForWidth())
        self.check_victim_of_violence.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_victim_of_violence.setFont(font)
        self.check_victim_of_violence.setObjectName("check_victim_of_violence")
        self.gridLayout_11.addWidget(self.check_victim_of_violence, 4, 0, 1, 1)
        self.check_serious_physical_illness = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_serious_physical_illness.sizePolicy().hasHeightForWidth())
        self.check_serious_physical_illness.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_serious_physical_illness.setFont(font)
        self.check_serious_physical_illness.setObjectName("check_serious_physical_illness")
        self.gridLayout_11.addWidget(self.check_serious_physical_illness, 4, 1, 1, 1)
        self.check_acute_physical_illness = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_acute_physical_illness.sizePolicy().hasHeightForWidth())
        self.check_acute_physical_illness.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.check_acute_physical_illness.setFont(font)
        self.check_acute_physical_illness.setObjectName("check_acute_physical_illness")
        self.gridLayout_11.addWidget(self.check_acute_physical_illness, 5, 0, 1, 1)
        self.check_aggresive_mental_illness = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_aggresive_mental_illness.sizePolicy().hasHeightForWidth())
        self.check_aggresive_mental_illness.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_aggresive_mental_illness.setFont(font)
        self.check_aggresive_mental_illness.setObjectName("check_aggresive_mental_illness")
        self.gridLayout_11.addWidget(self.check_aggresive_mental_illness, 5, 1, 1, 1)
        self.check_unknow_disease = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_unknow_disease.sizePolicy().hasHeightForWidth())
        self.check_unknow_disease.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_unknow_disease.setFont(font)
        self.check_unknow_disease.setObjectName("check_unknow_disease")
        self.gridLayout_11.addWidget(self.check_unknow_disease, 6, 0, 1, 1)
        self.check_possession = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_possession.sizePolicy().hasHeightForWidth())
        self.check_possession.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_possession.setFont(font)
        self.check_possession.setObjectName("check_possession")
        self.gridLayout_11.addWidget(self.check_possession, 6, 1, 1, 1)
        self.check_idea_of_eliminate = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_idea_of_eliminate.sizePolicy().hasHeightForWidth())
        self.check_idea_of_eliminate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_idea_of_eliminate.setFont(font)
        self.check_idea_of_eliminate.setObjectName("check_idea_of_eliminate")
        self.gridLayout_11.addWidget(self.check_idea_of_eliminate, 7, 0, 1, 1)
        self.check_problems_at_home = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_problems_at_home.sizePolicy().hasHeightForWidth())
        self.check_problems_at_home.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_problems_at_home.setFont(font)
        self.check_problems_at_home.setObjectName("check_problems_at_home")
        self.gridLayout_11.addWidget(self.check_problems_at_home, 7, 1, 1, 1)
        self.check_umbanda = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_umbanda.sizePolicy().hasHeightForWidth())
        self.check_umbanda.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_umbanda.setFont(font)
        self.check_umbanda.setObjectName("check_umbanda")
        self.gridLayout_11.addWidget(self.check_umbanda, 8, 0, 1, 1)
        self.check_panic_sindrome = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_panic_sindrome.sizePolicy().hasHeightForWidth())
        self.check_panic_sindrome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_panic_sindrome.setFont(font)
        self.check_panic_sindrome.setObjectName("check_panic_sindrome")
        self.gridLayout_11.addWidget(self.check_panic_sindrome, 8, 1, 1, 1)
        self.txt_traits = QtWidgets.QTextEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_traits.sizePolicy().hasHeightForWidth())
        self.txt_traits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_traits.setFont(font)
        self.txt_traits.setObjectName("txt_traits")
        self.gridLayout_11.addWidget(self.txt_traits, 9, 0, 1, 2)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 8, 5, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radio_sleep_well_yes = QtWidgets.QRadioButton(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_sleep_well_yes.setFont(font)
        self.radio_sleep_well_yes.setObjectName("radio_sleep_well_yes")
        self.verticalLayout_3.addWidget(self.radio_sleep_well_yes)
        self.radio_sleep_well_no = QtWidgets.QRadioButton(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_sleep_well_no.setFont(font)
        self.radio_sleep_well_no.setObjectName("radio_sleep_well_no")
        self.verticalLayout_3.addWidget(self.radio_sleep_well_no)
        self.gridLayout_5.addWidget(self.groupBox_6, 0, 5, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radio_medical_treatment_yes = QtWidgets.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_medical_treatment_yes.setFont(font)
        self.radio_medical_treatment_yes.setObjectName("radio_medical_treatment_yes")
        self.verticalLayout_2.addWidget(self.radio_medical_treatment_yes)
        self.radio_medical_treatment_no = QtWidgets.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_medical_treatment_no.setFont(font)
        self.radio_medical_treatment_no.setObjectName("radio_medical_treatment_no")
        self.verticalLayout_2.addWidget(self.radio_medical_treatment_no)
        self.gridLayout_5.addWidget(self.groupBox_5, 0, 2, 1, 3)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/user-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_extra_info, icon10, "")
        self.tab_fowarding = QtWidgets.QWidget()
        self.tab_fowarding.setObjectName("tab_fowarding")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_fowarding)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab_fowarding)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_19.setFont(font)
        self.groupBox_19.setObjectName("groupBox_19")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_19)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.check_directors = QtWidgets.QCheckBox(self.groupBox_19)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_directors.setFont(font)
        self.check_directors.setObjectName("check_directors")
        self.gridLayout_14.addWidget(self.check_directors, 0, 0, 1, 1)
        self.check_depass = QtWidgets.QCheckBox(self.groupBox_19)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_depass.setFont(font)
        self.check_depass.setObjectName("check_depass")
        self.gridLayout_14.addWidget(self.check_depass, 0, 1, 1, 1)
        self.check_social_assistant = QtWidgets.QCheckBox(self.groupBox_19)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_social_assistant.setFont(font)
        self.check_social_assistant.setObjectName("check_social_assistant")
        self.gridLayout_14.addWidget(self.check_social_assistant, 0, 2, 1, 1)
        self.check_teaching = QtWidgets.QCheckBox(self.groupBox_19)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_teaching.setFont(font)
        self.check_teaching.setObjectName("check_teaching")
        self.gridLayout_14.addWidget(self.check_teaching, 0, 3, 1, 1)
        self.txt_fowarding = QtWidgets.QTextEdit(self.groupBox_19)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_fowarding.setFont(font)
        self.txt_fowarding.setObjectName("txt_fowarding")
        self.gridLayout_14.addWidget(self.txt_fowarding, 1, 0, 1, 4)
        self.gridLayout_6.addWidget(self.groupBox_19, 0, 0, 1, 1)
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_fowarding)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setObjectName("groupBox_13")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_13)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.check_preparatory = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_preparatory.setFont(font)
        self.check_preparatory.setObjectName("check_preparatory")
        self.verticalLayout_4.addWidget(self.check_preparatory)
        self.check_basic1 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_basic1.setFont(font)
        self.check_basic1.setObjectName("check_basic1")
        self.verticalLayout_4.addWidget(self.check_basic1)
        self.check_basic2 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_basic2.setFont(font)
        self.check_basic2.setObjectName("check_basic2")
        self.verticalLayout_4.addWidget(self.check_basic2)
        self.check_apprentice1 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_apprentice1.setFont(font)
        self.check_apprentice1.setObjectName("check_apprentice1")
        self.verticalLayout_4.addWidget(self.check_apprentice1)
        self.check_apprentice2 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_apprentice2.setFont(font)
        self.check_apprentice2.setObjectName("check_apprentice2")
        self.verticalLayout_4.addWidget(self.check_apprentice2)
        self.check_education1 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_education1.setFont(font)
        self.check_education1.setObjectName("check_education1")
        self.verticalLayout_4.addWidget(self.check_education1)
        self.check_education2 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_education2.setFont(font)
        self.check_education2.setObjectName("check_education2")
        self.verticalLayout_4.addWidget(self.check_education2)
        self.check_exposer = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_exposer.setFont(font)
        self.check_exposer.setObjectName("check_exposer")
        self.verticalLayout_4.addWidget(self.check_exposer)
        self.check_philosophy = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_philosophy.setFont(font)
        self.check_philosophy.setObjectName("check_philosophy")
        self.verticalLayout_4.addWidget(self.check_philosophy)
        self.gridLayout_6.addWidget(self.groupBox_13, 0, 1, 1, 1)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_fowarding, icon11, "")
        self.tab_guidance = QtWidgets.QWidget()
        self.tab_guidance.setObjectName("tab_guidance")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_guidance)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_guidance)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_14.setFont(font)
        self.groupBox_14.setObjectName("groupBox_14")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_pasteur_a2 = QtWidgets.QRadioButton(self.groupBox_14)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_a2.setFont(font)
        self.radio_pasteur_a2.setObjectName("radio_pasteur_a2")
        self.horizontalLayout.addWidget(self.radio_pasteur_a2)
        self.radio_pasteur_a4 = QtWidgets.QRadioButton(self.groupBox_14)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_a4.setFont(font)
        self.radio_pasteur_a4.setObjectName("radio_pasteur_a4")
        self.horizontalLayout.addWidget(self.radio_pasteur_a4)
        self.radio_pasteur_12 = QtWidgets.QRadioButton(self.groupBox_14)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_12.setFont(font)
        self.radio_pasteur_12.setObjectName("radio_pasteur_12")
        self.horizontalLayout.addWidget(self.radio_pasteur_12)
        self.gridLayout_7.addWidget(self.groupBox_14, 0, 0, 1, 1)
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_guidance)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setObjectName("groupBox_15")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radio_pasteur_a3 = QtWidgets.QRadioButton(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_a3.setFont(font)
        self.radio_pasteur_a3.setObjectName("radio_pasteur_a3")
        self.horizontalLayout_2.addWidget(self.radio_pasteur_a3)
        self.radio_pasteur_3e3m = QtWidgets.QRadioButton(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_3e3m.setFont(font)
        self.radio_pasteur_3e3m.setObjectName("radio_pasteur_3e3m")
        self.horizontalLayout_2.addWidget(self.radio_pasteur_3e3m)
        self.gridLayout_7.addWidget(self.groupBox_15, 1, 0, 1, 1)
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_guidance)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setObjectName("groupBox_16")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radio_pasteur_p3f = QtWidgets.QRadioButton(self.groupBox_16)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_p3f.setFont(font)
        self.radio_pasteur_p3f.setObjectName("radio_pasteur_p3f")
        self.horizontalLayout_3.addWidget(self.radio_pasteur_p3f)
        self.gridLayout_7.addWidget(self.groupBox_16, 2, 0, 1, 1)
        self.groupBox_18 = QtWidgets.QGroupBox(self.tab_guidance)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_18.setFont(font)
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.txt_info = QtWidgets.QTextEdit(self.groupBox_18)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_info.setFont(font)
        self.txt_info.setObjectName("txt_info")
        self.gridLayout_15.addWidget(self.txt_info, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_18, 3, 0, 1, 1)
        self.groupBox_17 = QtWidgets.QGroupBox(self.tab_guidance)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setObjectName("groupBox_17")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_17)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.check_good_thoughts = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_good_thoughts.setFont(font)
        self.check_good_thoughts.setObjectName("check_good_thoughts")
        self.verticalLayout_5.addWidget(self.check_good_thoughts)
        self.check_home_gospel = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_home_gospel.setFont(font)
        self.check_home_gospel.setObjectName("check_home_gospel")
        self.verticalLayout_5.addWidget(self.check_home_gospel)
        self.check_readings = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_readings.setFont(font)
        self.check_readings.setObjectName("check_readings")
        self.verticalLayout_5.addWidget(self.check_readings)
        self.check_doctor = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_doctor.setFont(font)
        self.check_doctor.setObjectName("check_doctor")
        self.verticalLayout_5.addWidget(self.check_doctor)
        self.check_care_package = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_care_package.setFont(font)
        self.check_care_package.setObjectName("check_care_package")
        self.verticalLayout_5.addWidget(self.check_care_package)
        self.check_no_treatment = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_no_treatment.setFont(font)
        self.check_no_treatment.setObjectName("check_no_treatment")
        self.verticalLayout_5.addWidget(self.check_no_treatment)
        self.check_home_sanitation = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_home_sanitation.setFont(font)
        self.check_home_sanitation.setObjectName("check_home_sanitation")
        self.verticalLayout_5.addWidget(self.check_home_sanitation)
        self.check_intimate_makeover = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_intimate_makeover.setFont(font)
        self.check_intimate_makeover.setObjectName("check_intimate_makeover")
        self.verticalLayout_5.addWidget(self.check_intimate_makeover)
        self.check_study = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_study.setFont(font)
        self.check_study.setObjectName("check_study")
        self.verticalLayout_5.addWidget(self.check_study)
        self.check_frequency = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_frequency.setFont(font)
        self.check_frequency.setObjectName("check_frequency")
        self.verticalLayout_5.addWidget(self.check_frequency)
        self.check_no_pass = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_no_pass.setFont(font)
        self.check_no_pass.setObjectName("check_no_pass")
        self.verticalLayout_5.addWidget(self.check_no_pass)
        self.gridLayout_7.addWidget(self.groupBox_17, 0, 1, 4, 1)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/compass.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_guidance, icon12, "")
        self.tab_interviews = QtWidgets.QWidget()
        self.tab_interviews.setObjectName("tab_interviews")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_interviews)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_interviews)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_41 = QtWidgets.QLabel(self.groupBox_11)
        self.label_41.setObjectName("label_41")
        self.gridLayout_16.addWidget(self.label_41, 0, 0, 1, 1)
        self.txt_interviewer = QtWidgets.QLineEdit(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_interviewer.setFont(font)
        self.txt_interviewer.setObjectName("txt_interviewer")
        self.gridLayout_16.addWidget(self.txt_interviewer, 0, 1, 1, 3)
        self.cmb_treatment = QtWidgets.QComboBox(self.groupBox_11)
        self.cmb_treatment.setObjectName("cmb_treatment")
        self.cmb_treatment.addItem("")
        self.cmb_treatment.addItem("")
        self.cmb_treatment.addItem("")
        self.cmb_treatment.addItem("")
        self.cmb_treatment.addItem("")
        self.gridLayout_16.addWidget(self.cmb_treatment, 1, 0, 1, 4)
        self.txt_interview = QtWidgets.QTextEdit(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_interview.setFont(font)
        self.txt_interview.setObjectName("txt_interview")
        self.gridLayout_16.addWidget(self.txt_interview, 2, 0, 1, 4)
        self.btn_new_interview = QtWidgets.QPushButton(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_new_interview.setFont(font)
        self.btn_new_interview.setIcon(icon3)
        self.btn_new_interview.setObjectName("btn_new_interview")
        self.gridLayout_16.addWidget(self.btn_new_interview, 3, 0, 1, 2)
        self.btn_save_interview = QtWidgets.QPushButton(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_interview.setFont(font)
        self.btn_save_interview.setIcon(icon3)
        self.btn_save_interview.setObjectName("btn_save_interview")
        self.gridLayout_16.addWidget(self.btn_save_interview, 3, 2, 1, 2)
        self.gridLayout_8.addWidget(self.groupBox_11, 0, 0, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_interviews)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.tb_interviews = QtWidgets.QTableView(self.groupBox_12)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tb_interviews.setFont(font)
        self.tb_interviews.setObjectName("tb_interviews")
        self.model = QtGui.QStandardItemModel(self.groupBox_12)
        self.model.setHorizontalHeaderLabels(['DATA', 'ENTREVISTADOR', 'TRATAMENTO', 'ENTREVISTA'])                
        self.tb_interviews.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_interviews.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_interviews.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tb_interviews.setModel(self.model)
        self.gridLayout_17.addWidget(self.tb_interviews, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_12, 0, 1, 1, 1)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("images/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_interviews, icon13, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 2)
        FormFicha.setCentralWidget(self.centralwidget)

        self.txt_index.valueChanged.connect(self.index_changed)
                
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_edit.clicked.connect(self.btn_edit_clicked)
        self.btn_print.clicked.connect(self.btn_print_clicked)
        self.btn_backups.clicked.connect(self.btn_backups_clicked)
        self.btn_report.clicked.connect(self.btn_reports_clicked)
        self.btn_log_out.clicked.connect(self.btn_log_out_clicked)

        self.btn_new_interview.clicked.connect(self.btn_new_interview_clicked)
        self.btn_save_interview.clicked.connect(self.btn_save_interview_clicked)
        self.tb_interviews.doubleClicked.connect(self.cell_double_clicked)    

        self.radio_addiction_yes.clicked.connect(self.radio_addictions_yes_toggled)
        self.radio_addiction_no.clicked.connect(self.radio_addictions_no_toggled)        

        self.get_user()
        
        self.enable_read_only()

        if dao_assisted.id_gen_assisted() - 1 != 0:
            self.txt_index.setValue(dao_assisted.id_gen_assisted() - 1)
            self.txt_index.setMinimum(1)
            self.txt_index.setMaximum(dao_assisted.id_gen_assisted() - 1)
            self.fill_form()
        else:
            self.empty_form()
            self.disable_navigation()
            self.txt_index.setMaximum(0)
            self.txt_index.setMinimum(0)

        self.action_buttons()

        self.retranslateUi(FormFicha)
        self.tabWidget.setCurrentIndex(0)
        self.cmb_state.setCurrentIndex(22)
        self.cmb_feeding.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FormFicha)

    def retranslateUi(self, FormFicha):
        _translate = QtCore.QCoreApplication.translate
        FormFicha.setWindowTitle(_translate("FormFicha", "GERENCIAMENTO DE ASSISTIDOS"))
        self.groupBox.setTitle(_translate("FormFicha", "AÇÕES"))
        self.btn_add.setText(_translate("FormFicha", "ADICIONAR"))
        self.btn_save.setText(_translate("FormFicha", "SALVAR"))
        self.btn_cancel.setText(_translate("FormFicha", "CANCELAR"))
        self.btn_edit.setText(_translate("FormFicha", "EDITAR"))
        self.btn_delete.setText(_translate("FormFicha", "EXCLUIR"))
        self.btn_print.setText(_translate("FormFicha", "IMPRIMIR"))
        self.btn_report.setText(_translate("FormFicha", "RELATÓRIO"))
        self.btn_backups.setText(_translate("FormFicha", "BACKUPS"))
        self.btn_log_out.setText(_translate("FormFicha", "SAIR"))
        self.label_4.setText(_translate("FormFicha", "NOME"))
        self.label_5.setText(_translate("FormFicha", "DATA DE NASCIMENTO"))
        self.label_6.setText(_translate("FormFicha", "TELEFONE (CELULAR)"))
        self.label_7.setText(_translate("FormFicha", "TELEFONE (RESIDENCIAL)"))
        self.label_14.setText(_translate("FormFicha", "ESTADO CIVIL"))
        self.txt_phone1.setInputMask(_translate("FormFicha", "(##) #####-####"))
        self.txt_phone1.setText(_translate("FormFicha", ""))
        self.txt_phone2.setInputMask(_translate("FormFicha", "(##) #####-####"))
        self.txt_phone2.setText(_translate("FormFicha", ""))
        self.cmb_gender.setItemText(0, _translate("FormFicha", "MASCULINO"))
        self.cmb_gender.setItemText(1, _translate("FormFicha", "FEMININO"))
        self.cmb_gender.setItemText(2, _translate("FormFicha", "OUTRO"))
        self.cmb_civil_state.setItemText(0, _translate("FormFicha", "SOLTEIRO(A)"))
        self.cmb_civil_state.setItemText(1, _translate("FormFicha", "CASADO(A)"))
        self.cmb_civil_state.setItemText(2, _translate("FormFicha", "DIVORCIADO(A)"))
        self.cmb_civil_state.setItemText(3, _translate("FormFicha", "VIÚVO(A)"))
        self.label_21.setText(_translate("FormFicha", "OCUPAÇÃO"))
        self.label_22.setText(_translate("FormFicha", "RESIDE COM"))
        self.label_23.setText(_translate("FormFicha", "ENDEREÇO"))
        self.label_24.setText(_translate("FormFicha", "BAIRRO"))
        self.label_26.setText(_translate("FormFicha", "CIDADE"))
        self.label_39.setText(_translate("FormFicha", "ESTADO"))
        self.cmb_state.setItemText(0, _translate("FormFicha", "ACRE"))
        self.cmb_state.setItemText(1, _translate("FormFicha", "ALAGOAS"))
        self.cmb_state.setItemText(2, _translate("FormFicha", "AMAPÁ"))
        self.cmb_state.setItemText(3, _translate("FormFicha", "AMAZONAS"))
        self.cmb_state.setItemText(4, _translate("FormFicha", "BAHIA"))
        self.cmb_state.setItemText(5, _translate("FormFicha", "CEARÁ"))
        self.cmb_state.setItemText(6, _translate("FormFicha", "ESPÍRITO SANTO"))
        self.cmb_state.setItemText(7, _translate("FormFicha", "MARANHÃO"))
        self.cmb_state.setItemText(8, _translate("FormFicha", "MATO GROSSO"))
        self.cmb_state.setItemText(9, _translate("FormFicha", "MATO GROSSO DO SUL"))
        self.cmb_state.setItemText(10, _translate("FormFicha", "MINAS GERAIS"))
        self.cmb_state.setItemText(11, _translate("FormFicha", "PARÁ"))
        self.cmb_state.setItemText(12, _translate("FormFicha", "PARAÍBA"))
        self.cmb_state.setItemText(13, _translate("FormFicha", "PARANÁ"))
        self.cmb_state.setItemText(14, _translate("FormFicha", "PERNAMBUCO"))
        self.cmb_state.setItemText(15, _translate("FormFicha", "PIAUÍ"))
        self.cmb_state.setItemText(16, _translate("FormFicha", "RIO DE JANEIRO"))
        self.cmb_state.setItemText(17, _translate("FormFicha", "RIO GRANDE DO NORTE"))
        self.cmb_state.setItemText(18, _translate("FormFicha", "RIO GRANDE DO SUL"))
        self.cmb_state.setItemText(19, _translate("FormFicha", "RONDÔNIA"))
        self.cmb_state.setItemText(20, _translate("FormFicha", "RORAIMA"))
        self.cmb_state.setItemText(21, _translate("FormFicha", "SANTA CATARINA"))
        self.cmb_state.setItemText(22, _translate("FormFicha", "SÃO PAULO"))
        self.cmb_state.setItemText(23, _translate("FormFicha", "SERGIPE"))
        self.cmb_state.setItemText(24, _translate("FormFicha", "TOCANTINS"))
        self.txt_date.setInputMask(_translate("FormFicha", "##/##/####"))
        self.label_8.setText(_translate("FormFicha", "GÊNERO"))
        self.label_25.setText(_translate("FormFicha", "NÚMERO"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_personal_data), _translate("FormFicha", "Dados Pessoais"))
        self.cmb_feeding.setItemText(0, _translate("FormFicha", "POUCA"))
        self.cmb_feeding.setItemText(1, _translate("FormFicha", "REGULAR"))
        self.cmb_feeding.setItemText(2, _translate("FormFicha", "MUITA"))
        self.groupBox_4.setTitle(_translate("FormFicha", "Toma sedativos?"))
        self.radio_sedative_yes.setText(_translate("FormFicha", "SIM"))
        self.radio_sedative_no.setText(_translate("FormFicha", "NÃO"))
        self.groupBox_10.setTitle(_translate("FormFicha", "FAMÍLIA"))
        self.groupBox_9.setTitle(_translate("FormFicha", "TRABALHO"))
        self.radio_dreams_yes.setText(_translate("FormFicha", "SONHOS"))
        self.radio_dreams_no.setText(_translate("FormFicha", "PESADELOS"))
        self.label_40.setText(_translate("FormFicha", "ALIMENTAÇÃO"))
        self.groupBox_7.setTitle(_translate("FormFicha", "VÍCIOS"))
        self.check_tobacco.setText(_translate("FormFicha", "Tabaco"))
        self.radio_addiction_yes.setText(_translate("FormFicha", "SIM"))
        self.check_alcohol.setText(_translate("FormFicha", "Álcool"))
        self.check_drugs.setText(_translate("FormFicha", "Drogas"))
        self.radio_addiction_no.setText(_translate("FormFicha", "NÃO"))
        self.check_cigarette.setText(_translate("FormFicha", "Fumo"))
        self.check_sex.setText(_translate("FormFicha", "Sexo"))
        self.groupBox_3.setTitle(_translate("FormFicha", "Características"))
        self.check_depression.setText(_translate("FormFicha", "Depressão Aguda"))
        self.check_disappearence.setText(_translate("FormFicha", "Desaparecimento"))
        self.check_mental_disorder.setText(_translate("FormFicha", "Disturbios Mentais"))
        self.check_homicidal.setText(_translate("FormFicha", "Homicida"))
        self.check_pre_surgery.setText(_translate("FormFicha", "Pré-Cirurgia"))
        self.check_problem_continues.setText(_translate("FormFicha", "Problema Continua"))
        self.check_post_surgery.setText(_translate("FormFicha", "Pós-Cirurgia"))
        self.check_violence_practice.setText(_translate("FormFicha", "Prática de Violência"))
        self.check_victim_of_violence.setText(_translate("FormFicha", "Vítima de Violência"))
        self.check_serious_physical_illness.setText(_translate("FormFicha", "Doença Física Grave"))
        self.check_acute_physical_illness.setText(_translate("FormFicha", "Doença Física em Fase Aguda"))
        self.check_aggresive_mental_illness.setText(_translate("FormFicha", "Doença Mental Agressiva"))
        self.check_unknow_disease.setText(_translate("FormFicha", "Doença Grave Desconhecida"))
        self.check_possession.setText(_translate("FormFicha", "Fascinação/Possessão"))
        self.check_idea_of_eliminate.setText(_translate("FormFicha", "Ideia de Eliminar Alguém"))
        self.check_problems_at_home.setText(_translate("FormFicha", "Problemas Graves no Lar"))
        self.check_umbanda.setText(_translate("FormFicha", "Veio da Umbanda"))
        self.check_panic_sindrome.setText(_translate("FormFicha", "Síndrome do Pânico"))
        self.groupBox_6.setTitle(_translate("FormFicha", "Dorme Bem?"))
        self.radio_sleep_well_yes.setText(_translate("FormFicha", "SIM"))
        self.radio_sleep_well_no.setText(_translate("FormFicha", "NÃO"))
        self.groupBox_5.setTitle(_translate("FormFicha", "Trat. Médico?"))
        self.radio_medical_treatment_yes.setText(_translate("FormFicha", "SIM"))
        self.radio_medical_treatment_no.setText(_translate("FormFicha", "NÃO"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_extra_info), _translate("FormFicha", "Informações Extras"))
        self.groupBox_19.setTitle(_translate("FormFicha", "ENCAMINHAMENTO"))
        self.check_directors.setText(_translate("FormFicha", "Diretoria"))
        self.check_depass.setText(_translate("FormFicha", "Depasse"))
        self.check_social_assistant.setText(_translate("FormFicha", "Ast. Social"))
        self.check_teaching.setText(_translate("FormFicha", "Ensino"))
        self.groupBox_13.setTitle(_translate("FormFicha", "FREQUÊNCIA"))
        self.check_preparatory.setText(_translate("FormFicha", "Preparatório (O que é Espiritísmo?)"))
        self.check_basic1.setText(_translate("FormFicha", "1º Básico"))
        self.check_basic2.setText(_translate("FormFicha", "2º Básico"))
        self.check_apprentice1.setText(_translate("FormFicha", "1º Aprendiz do Evangelho"))
        self.check_apprentice2.setText(_translate("FormFicha", "2º Aprendiz do Evangelho"))
        self.check_education1.setText(_translate("FormFicha", "1ª Educação Mediúnica"))
        self.check_education2.setText(_translate("FormFicha", "2ª Educação Mediúnica"))
        self.check_exposer.setText(_translate("FormFicha", "Expositor"))
        self.check_philosophy.setText(_translate("FormFicha", "Filosofia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fowarding), _translate("FormFicha", "Encaminhamento"))
        self.groupBox_14.setTitle(_translate("FormFicha", "1) Sábado 2º, 3º, 4º ou 5º"))
        self.radio_pasteur_a2.setText(_translate("FormFicha", "Pasteur - A2"))
        self.radio_pasteur_a4.setText(_translate("FormFicha", "Pasteur - A4"))
        self.radio_pasteur_12.setText(_translate("FormFicha", "Pasteur - 1/2"))
        self.groupBox_15.setTitle(_translate("FormFicha", "2) Domingo 2º, 3º, 4º ou 5º"))
        self.radio_pasteur_a3.setText(_translate("FormFicha", "Pasteur - A3"))
        self.radio_pasteur_3e3m.setText(_translate("FormFicha", "Pasteur - 3E, 3M"))
        self.groupBox_16.setTitle(_translate("FormFicha", "3) Sábado 2º, 3º, 4º ou 5º"))
        self.radio_pasteur_p3f.setText(_translate("FormFicha", "Pasteur - P3F  Cura"))
        self.groupBox_18.setTitle(_translate("FormFicha", "INFORMAÇÕES NECESSÁRIAS"))
        self.groupBox_17.setTitle(_translate("FormFicha", "ORIENTAÇÃO ESPIRITUAL"))
        self.check_good_thoughts.setText(_translate("FormFicha", "Ter bons pensamentos"))
        self.check_home_gospel.setText(_translate("FormFicha", "Evangelho no lar"))
        self.check_readings.setText(_translate("FormFicha", "Leituras edificantes"))
        self.check_doctor.setText(_translate("FormFicha", "Médico de confiança"))
        self.check_care_package.setText(_translate("FormFicha", "Cesta básica"))
        self.check_no_treatment.setText(_translate("FormFicha", "Não fazer tratamento paralelo"))
        self.check_home_sanitation.setText(_translate("FormFicha", "Higienização do lar"))
        self.check_intimate_makeover.setText(_translate("FormFicha", "Reforma íntima"))
        self.check_study.setText(_translate("FormFicha", "Estudo da doutrina"))
        self.check_frequency.setText(_translate("FormFicha", "Frequência na assistência"))
        self.check_no_pass.setText(_translate("FormFicha", "Não aplicar passe"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_guidance), _translate("FormFicha", "Colegiado"))
        self.groupBox_11.setTitle(_translate("FormFicha", "ENTREVISTA"))
        self.label_41.setText(_translate("FormFicha", "ENTREVISTADOR"))
        self.cmb_treatment.setItemText(0, _translate("FormFicha", "NENHUM"))
        self.cmb_treatment.setItemText(1, _translate("FormFicha", "HL"))
        self.cmb_treatment.setItemText(2, _translate("FormFicha", "P1/2"))
        self.cmb_treatment.setItemText(3, _translate("FormFicha", "P3E"))
        self.cmb_treatment.setItemText(4, _translate("FormFicha", "P3F"))
        self.btn_new_interview.setText(_translate("FormFicha", "NOVA ENTREVISTA"))
        self.btn_save_interview.setText(_translate("FormFicha", "SALVAR"))
        self.groupBox_12.setTitle(_translate("FormFicha", "ENTREVISTAS ANTERIORES"))        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_interviews), _translate("FormFicha", "Entrevistas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormFicha = QtWidgets.QMainWindow()
    ui = Ui_FormFicha()
    ui.setupUi(FormFicha)
    FormFicha.show()
    sys.exit(app.exec_())
