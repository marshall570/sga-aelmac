# -*- coding: utf-8 -*-
import tkinter
from PyQt5 import QtCore, QtGui, QtWidgets
from dto_user import User
from dto_assisted import Assisted
from dto_interview import Interview
from tkinter import messagebox
from dao_assisted import DataAcessAssisted
from dao_interview import DataAcessInterview

# GLOBAL OBJECTS
dao_assisted = DataAcessAssisted()
dao_interview = DataAcessInterview()
a = Assisted()
i = Interview()

class Ui_FormFicha(object):
    # FORM VARIABLES    
    index = 0
    error_message = ''
    adding = False
    editing = False
    writing_interview = False
    
    # PASSIVE METHODS
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
            self.check_drgus.toggle()
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
        # if self.radio_hl.isChecked():
        #     self.radio_hl.toggle()        
        # if self.radio_p12.isChecked():
        #     self.radio_p12.toggle()        
        # if self.radio_p3e.isChecked():
        #     self.radio_p3e.toggle()        
        # if self.radio_p3f.isChecked():
        #     self.radio_p3f.toggle()
        self.txt_interview.setPlainText('EDITE UM REGISTRO EXISTENTE PARA ESCREVER NOVAS ENTREVISTAS')
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
        dao_assisted.select_assisted(a, self.index)
        
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
            self.txt_dreams.setText(a.dreams.replace('SONHO, ', ''))
        else:
            self.radio_dreams_no.toggle()        
            self.txt_dreams.setText(a.dreams.replace('PESADELO, ', ''))
       
       
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
        # if self.radio_hl.isChecked():
        #     self.radio_hl.toggle()        
        # if self.radio_p12.isChecked():
        #     self.radio_p12.toggle()        
        # if self.radio_p3e.isChecked():
        #     self.radio_p3e.toggle()        
        # if self.radio_p3f.isChecked():
        #     self.radio_p3f.toggle()
        self.txt_interview.setText('')
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
        self.btn_search_index.setEnabled(True)
        self.btn_first.setEnabled(True)
        self.btn_previous.setEnabled(True)
        self.btn_next.setEnabled(True)
        self.btn_last.setEnabled(True)

    def disable_navigation(self):
        self.txt_index.setEnabled(False)
        self.btn_search_index.setEnabled(False)
        self.btn_first.setEnabled(False)
        self.btn_previous.setEnabled(False)
        self.btn_next.setEnabled(False)
        self.btn_last.setEnabled(False)

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
        # self.radio_hl.setEnabled(False)    
        # self.radio_p12.setEnabled(False)     
        # self.radio_p3e.setEnabled(False)
        # self.radio_p3f.setEnabled(False)
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
        # self.radio_hl.setEnabled(False)    
        # self.radio_p12.setEnabled(False)     
        # self.radio_p3e.setEnabled(False)
        # self.radio_p3f.setEnabled(False)
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
            self.btn_search_index.setEnabled(False)
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
            self.btn_search_index.setEnabled(True)
            self.btn_report.setEnabled(True)
            self.btn_delete.setEnabled(True)
        
    def navigation_buttons(self):
        total = dao_assisted.id_gen_assisted() - 1

        if total <= 1:
            self.disable_navigation()
        else:
            if self.index == 1 and total != 1:
                self.btn_first.setEnabled(False)
                self.btn_previous.setEnabled(False)
                self.btn_next.setEnabled(True)
                self.btn_last.setEnabled(True)
            elif self.index == total and total > 1:
                self.btn_first.setEnabled(True)
                self.btn_previous.setEnabled(True)
                self.btn_next.setEnabled(False)
                self.btn_last.setEnabled(False)
            else:
                self.btn_first.setEnabled(True)
                self.btn_previous.setEnabled(True)
                self.btn_next.setEnabled(True)
                self.btn_last.setEnabled(True)

        self.lbl_index.setText(str(self.index))
        self.lbl_total_index.setText(str(total))

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
        a.ocupation = self.txt_ocupation.text().strip()
        a.lives_with = self.txt_lives_with.text().strip()
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
    

    # BUTTONS METHODS    
    def btn_first_clicked(self):
        self.index = 1
        dao_assisted.select_assisted(a, self.index)
        self.fill_form()
        self.navigation_buttons()

    def btn_previous_clicked(self):
        self.index -= 1
        dao_assisted.select_assisted(a, self.index)
        self.fill_form()
        self.navigation_buttons()

    def btn_next_clicked(self):
        self.index += 1
        dao_assisted.select_assisted(a, self.index)
        self.fill_form()
        self.navigation_buttons()

    def btn_last_clicked(self):
        self.index = dao_assisted.id_gen_assisted() - 1
        dao_assisted.select_assisted(a, self.index)
        self.fill_form()
        self.navigation_buttons()    
    
    def btn_log_out_clicked(self):
        root = tkinter.Tk()
        root.withdraw()
        choice = messagebox.askquestion('SAIR DO SISTEMA', 'Deseja sair do sistema?')
        tkinter.Tk().destroy()
                
        if choice == 'yes':
            from form_login import Ui_FormLogin
            # dao.set_off()
            FormFicha.close()
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
        self.navigation_buttons()
        self.action_buttons()        
        
        self.adding = False
        self.editing = False
        
        if self.writing_interview:
            self.btn_new_interview_clicked()
        
        if dao_assisted.id_gen_assisted() - 1 <= 0:
            self.empty_form()
        else:
            self.btn_last_clicked()   
      
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
                if self.adding:
                    self.get_values(a)
                    dao_assisted.insert_assisted(a)
                    self.btn_last_clicked()
                    self.btn_cancel_clicked()
                    self.adding = False      
                elif self.editing:
                    self.get_values(a)
                    dao_assisted.edit_assisted(a)
                    self.btn_last_clicked()
                    self.btn_cancel_clicked()
                    self.editing = False
                                    
    def btn_delete_clicked(self):
        root = tkinter.Tk()
        root.withdraw()
        choice = messagebox.askquestion('DELETAR REGISTRO', 'Deseja DELETAR o registro de <{}>?'.format(a.name))
        tkinter.Tk().destroy()
        
        if choice == 'yes':
            dao_assisted.delete_assisted(self.index)
            if dao_assisted.id_gen_assisted() - 1 == 0:
                self.empty_form()
                self.action_buttons()
                self.navigation_buttons()
                
                self.lbl_index.setText('0')    
                self.lbl_total_index.setText('0')    
            else:
                if self.index > dao_assisted.id_gen_assisted() - 1:
                    self.index -= 1
                elif self.index < dao_assisted.id_gen_assisted() - 1:
                    self.index += 1                    
                else:
                    self.index = self.index
                    
                self.fill_form()
                self.action_buttons()
                self.navigation_buttons()
                                                  
    def btn_edit_clicked(self):
        self.disable_navigation()
        self.disable_read_only()
        
        self.editing = True
        self.btn_new_interview.setEnabled(True)

        
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
        dao_assisted.print_register(a)                   

    def radio_addictions_no_toggled(self):
        if self.check_alcohol.isChecked():
            self.check_alcohol.toggle()
        if self.check_tobacco.isChecked():
            self.check_tobacco.toggle()
        if self.check_cigarette.isChecked():
            self.check_cigarette.toggle()
        if self.check_drugs.isChecked():
            self.check_drgus.toggle()
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
            self.check_drgus.toggle()
        if self.check_sex.isChecked():
            self.check_sex.toggle()
        self.check_alcohol.setEnabled(True)
        self.check_tobacco.setEnabled(True)
        self.check_cigarette.setEnabled(True)
        self.check_drugs.setEnabled(True)
        self.check_sex.setEnabled(True)

    def btn_new_interview_clicked(self):
        if not self.writing_interview:
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("images/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_new_interview.setIcon(new_icon)
            self.btn_new_interview.setText('CANCELAR')
            
            self.txt_interviewer.setReadOnly(False)
            self.cmb_treatment.setEnabled(True)
            self.txt_interview.setReadOnly(False)
            self.tb_interviews.setEnabled(False)
            self.btn_save_interview.setEnabled(True)
            self.btn_new_interview.setEnabled(True)
            
            self.writing_interview = True
        else:
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("images/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_new_interview.setIcon(new_icon)
            self.btn_new_interview.setText('NOVA ENTREVISTA')
            
            self.txt_interviewer.setReadOnly(True)
            self.cmb_treatment.setEnabled(False)
            self.txt_interview.setReadOnly(True)
            self.tb_interviews.setEnabled(True)
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
                i.interview = self.txt_interview.toPlainText().strip().upper()
                
                dao_interview.insert_interview(i, a)
                self.btn_new_interview_clicked()
                self.btn_cancel_clicked()
                self.tabWidget.setCurrentIndex(2)

    def fill_table_view(self):
        query_result = dao_interview.select_interview()
        self.tb_interviews.setRowCount(len(query_result))
        
        row = 0
        for tup in query_result:
            col = 0
            for item in tup:
                cell = QtWidgets.QTableWidgetItem(item)
                cell.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tb_interviews.setItem(row, col, cell)
                col += 1
            row += 1
            
            
            
            
                                    

    def setupUi(self, FormFicha):
        FormFicha.setObjectName("FormFicha")
        FormFicha.resize(897, 650)
        self.centralwidget = QtWidgets.QWidget(FormFicha)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 881, 441))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_personal_data = QtWidgets.QWidget()
        self.tab_personal_data.setObjectName("tab_personal_data")
        self.label_4 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_name = QtWidgets.QLineEdit(self.tab_personal_data)
        self.txt_name.setGeometry(QtCore.QRect(70, 10, 791, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_name.setFont(font)
        self.txt_name.setObjectName("txt_name")
        self.label_5 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.txt_date = QtWidgets.QLineEdit(self.tab_personal_data)
        self.txt_date.setGeometry(QtCore.QRect(10, 90, 171, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_date.setFont(font)
        self.txt_date.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_date.setObjectName("txt_date")
        self.label_6 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_6.setGeometry(QtCore.QRect(200, 60, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.txt_phone1 = QtWidgets.QLineEdit(self.tab_personal_data)
        self.txt_phone1.setGeometry(QtCore.QRect(200, 90, 161, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_phone1.setFont(font)
        self.txt_phone1.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_phone1.setObjectName("txt_phone1")
        self.txt_phone2 = QtWidgets.QLineEdit(self.tab_personal_data)
        self.txt_phone2.setGeometry(QtCore.QRect(380, 90, 191, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_phone2.setFont(font)
        self.txt_phone2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_phone2.setObjectName("txt_phone2")
        self.label_7 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_7.setGeometry(QtCore.QRect(380, 60, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_8.setGeometry(QtCore.QRect(590, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.cmb_gender = QtWidgets.QComboBox(self.tab_personal_data)
        self.cmb_gender.setGeometry(QtCore.QRect(590, 90, 121, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.cmb_gender.setFont(font)
        self.cmb_gender.setObjectName("cmb_gender")
        self.cmb_gender.addItem("")
        self.cmb_gender.addItem("")
        self.cmb_gender.addItem("")
        self.label_14 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_14.setGeometry(QtCore.QRect(740, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.cmb_civil_state = QtWidgets.QComboBox(self.tab_personal_data)
        self.cmb_civil_state.setGeometry(QtCore.QRect(740, 90, 121, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.cmb_civil_state.setFont(font)
        self.cmb_civil_state.setObjectName("cmb_civil_state")
        self.cmb_civil_state.addItem("")
        self.cmb_civil_state.addItem("")
        self.cmb_civil_state.addItem("")
        self.cmb_civil_state.addItem("")
        self.txt_ocupation = QtWidgets.QLineEdit(self.tab_personal_data)
        self.txt_ocupation.setGeometry(QtCore.QRect(110, 140, 751, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_ocupation.setFont(font)
        self.txt_ocupation.setObjectName("txt_ocupation")
        self.label_21 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_21.setGeometry(QtCore.QRect(10, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_22.setGeometry(QtCore.QRect(10, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.txt_lives_with = QtWidgets.QLineEdit(self.tab_personal_data)
        self.txt_lives_with.setGeometry(QtCore.QRect(110, 190, 751, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_lives_with.setFont(font)
        self.txt_lives_with.setObjectName("txt_lives_with")
        self.label_23 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_23.setGeometry(QtCore.QRect(10, 250, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.txt_address = QtWidgets.QLineEdit(self.tab_personal_data)
        self.txt_address.setGeometry(QtCore.QRect(100, 250, 761, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_address.setFont(font)
        self.txt_address.setObjectName("txt_address")
        self.label_24 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_24.setGeometry(QtCore.QRect(10, 300, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.txt_neighbourhood = QtWidgets.QLineEdit(self.tab_personal_data)
        self.txt_neighbourhood.setGeometry(QtCore.QRect(80, 300, 511, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_neighbourhood.setFont(font)
        self.txt_neighbourhood.setObjectName("txt_neighbourhood")
        self.txt_number = QtWidgets.QLineEdit(self.tab_personal_data)
        self.txt_number.setGeometry(QtCore.QRect(700, 300, 161, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_number.setFont(font)
        self.txt_number.setObjectName("txt_number")
        self.label_25 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_25.setGeometry(QtCore.QRect(620, 300, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.txt_city = QtWidgets.QLineEdit(self.tab_personal_data)
        self.txt_city.setGeometry(QtCore.QRect(80, 350, 441, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.txt_city.setFont(font)
        self.txt_city.setObjectName("txt_city")
        self.label_26 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_26.setGeometry(QtCore.QRect(10, 350, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_39 = QtWidgets.QLabel(self.tab_personal_data)
        self.label_39.setGeometry(QtCore.QRect(550, 350, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.cmb_state = QtWidgets.QComboBox(self.tab_personal_data)
        self.cmb_state.setGeometry(QtCore.QRect(620, 350, 241, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_personal_data, icon, "")
        self.tab_extra_info = QtWidgets.QWidget()
        self.tab_extra_info.setObjectName("tab_extra_info")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_extra_info)
        self.groupBox_3.setGeometry(QtCore.QRect(480, 10, 391, 385))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.txt_traits = QtWidgets.QTextEdit(self.groupBox_3)
        self.txt_traits.setGeometry(QtCore.QRect(10, 300, 371, 75))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_traits.setFont(font)
        self.txt_traits.setObjectName("txt_traits")
        self.check_depression = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_depression.setGeometry(QtCore.QRect(10, 30, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_depression.setFont(font)
        self.check_depression.setObjectName("check_depression")
        self.check_mental_disorder = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_mental_disorder.setGeometry(QtCore.QRect(10, 60, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_mental_disorder.setFont(font)
        self.check_mental_disorder.setObjectName("check_mental_disorder")
        self.check_pre_surgery = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_pre_surgery.setGeometry(QtCore.QRect(10, 90, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_pre_surgery.setFont(font)
        self.check_pre_surgery.setObjectName("check_pre_surgery")
        self.check_post_surgery = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_post_surgery.setGeometry(QtCore.QRect(10, 120, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_post_surgery.setFont(font)
        self.check_post_surgery.setObjectName("check_post_surgery")
        self.check_victim_of_violence = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_victim_of_violence.setGeometry(QtCore.QRect(10, 150, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_victim_of_violence.setFont(font)
        self.check_victim_of_violence.setObjectName("check_victim_of_violence")
        self.check_acute_physical_illness = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_acute_physical_illness.setGeometry(QtCore.QRect(10, 180, 201, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.check_acute_physical_illness.setFont(font)
        self.check_acute_physical_illness.setObjectName("check_acute_physical_illness")
        self.check_unknow_disease = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_unknow_disease.setGeometry(QtCore.QRect(10, 210, 201, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_unknow_disease.setFont(font)
        self.check_unknow_disease.setObjectName("check_unknow_disease")
        self.check_idea_of_eliminate = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_idea_of_eliminate.setGeometry(QtCore.QRect(10, 240, 191, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_idea_of_eliminate.setFont(font)
        self.check_idea_of_eliminate.setObjectName("check_idea_of_eliminate")
        self.check_umbanda = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_umbanda.setGeometry(QtCore.QRect(10, 270, 191, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_umbanda.setFont(font)
        self.check_umbanda.setObjectName("check_umbanda")
        self.check_homicidal = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_homicidal.setGeometry(QtCore.QRect(205, 60, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_homicidal.setFont(font)
        self.check_homicidal.setObjectName("check_homicidal")
        self.check_possession = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_possession.setGeometry(QtCore.QRect(205, 210, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_possession.setFont(font)
        self.check_possession.setObjectName("check_possession")
        self.check_problems_at_home = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_problems_at_home.setGeometry(QtCore.QRect(205, 240, 191, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_problems_at_home.setFont(font)
        self.check_problems_at_home.setObjectName("check_problems_at_home")
        self.check_aggresive_mental_illness = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_aggresive_mental_illness.setGeometry(QtCore.QRect(205, 180, 201, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_aggresive_mental_illness.setFont(font)
        self.check_aggresive_mental_illness.setObjectName("check_aggresive_mental_illness")
        self.check_serious_physical_illness = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_serious_physical_illness.setGeometry(QtCore.QRect(205, 150, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_serious_physical_illness.setFont(font)
        self.check_serious_physical_illness.setObjectName("check_serious_physical_illness")
        self.check_panic_sindrome = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_panic_sindrome.setGeometry(QtCore.QRect(205, 270, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_panic_sindrome.setFont(font)
        self.check_panic_sindrome.setObjectName("check_panic_sindrome")
        self.check_violence_practice = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_violence_practice.setGeometry(QtCore.QRect(205, 120, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_violence_practice.setFont(font)
        self.check_violence_practice.setObjectName("check_violence_practice")
        self.check_disappearence = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_disappearence.setGeometry(QtCore.QRect(205, 30, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_disappearence.setFont(font)
        self.check_disappearence.setObjectName("check_disappearence")
        self.check_problem_continues = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_problem_continues.setGeometry(QtCore.QRect(205, 90, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_problem_continues.setFont(font)
        self.check_problem_continues.setObjectName("check_problem_continues")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_extra_info)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 151, 55))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.radio_sedative_yes = QtWidgets.QRadioButton(self.groupBox_4)
        self.radio_sedative_yes.setGeometry(QtCore.QRect(15, 25, 51, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_sedative_yes.setFont(font)
        self.radio_sedative_yes.setObjectName("radio_sedative_yes")
        self.radio_sedative_no = QtWidgets.QRadioButton(self.groupBox_4)
        self.radio_sedative_no.setGeometry(QtCore.QRect(85, 25, 51, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_sedative_no.setFont(font)
        self.radio_sedative_no.setObjectName("radio_sedative_no")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_extra_info)
        self.groupBox_5.setGeometry(QtCore.QRect(165, 10, 151, 55))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.radio_medical_treatment_yes = QtWidgets.QRadioButton(self.groupBox_5)
        self.radio_medical_treatment_yes.setGeometry(QtCore.QRect(15, 25, 51, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_medical_treatment_yes.setFont(font)
        self.radio_medical_treatment_yes.setObjectName("radio_medical_treatment_yes")
        self.radio_medical_treatment_no = QtWidgets.QRadioButton(self.groupBox_5)
        self.radio_medical_treatment_no.setGeometry(QtCore.QRect(85, 25, 51, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_medical_treatment_no.setFont(font)
        self.radio_medical_treatment_no.setObjectName("radio_medical_treatment_no")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_extra_info)
        self.groupBox_6.setGeometry(QtCore.QRect(320, 10, 151, 55))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.radio_sleep_well_yes = QtWidgets.QRadioButton(self.groupBox_6)
        self.radio_sleep_well_yes.setGeometry(QtCore.QRect(15, 25, 51, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_sleep_well_yes.setFont(font)
        self.radio_sleep_well_yes.setObjectName("radio_sleep_well_yes")
        self.radio_sleep_well_no = QtWidgets.QRadioButton(self.groupBox_6)
        self.radio_sleep_well_no.setGeometry(QtCore.QRect(85, 25, 51, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_sleep_well_no.setFont(font)
        self.radio_sleep_well_no.setObjectName("radio_sleep_well_no")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_extra_info)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 70, 461, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.radio_addiction_yes = QtWidgets.QRadioButton(self.groupBox_7)
        self.radio_addiction_yes.setGeometry(QtCore.QRect(10, 30, 51, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_addiction_yes.setFont(font)
        self.radio_addiction_yes.setObjectName("radio_addiction_yes")
        self.radio_addiction_no = QtWidgets.QRadioButton(self.groupBox_7)
        self.radio_addiction_no.setGeometry(QtCore.QRect(10, 60, 51, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_addiction_no.setFont(font)
        self.radio_addiction_no.setObjectName("radio_addiction_no")
        self.check_alcohol = QtWidgets.QCheckBox(self.groupBox_7)
        self.check_alcohol.setGeometry(QtCore.QRect(80, 45, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_alcohol.setFont(font)
        self.check_alcohol.setObjectName("check_alcohol")
        self.check_tobacco = QtWidgets.QCheckBox(self.groupBox_7)
        self.check_tobacco.setGeometry(QtCore.QRect(160, 45, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_tobacco.setFont(font)
        self.check_tobacco.setObjectName("check_tobacco")
        self.check_cigarette = QtWidgets.QCheckBox(self.groupBox_7)
        self.check_cigarette.setGeometry(QtCore.QRect(240, 45, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_cigarette.setFont(font)
        self.check_cigarette.setObjectName("check_cigarette")
        self.check_drugs = QtWidgets.QCheckBox(self.groupBox_7)
        self.check_drugs.setGeometry(QtCore.QRect(310, 45, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_drugs.setFont(font)
        self.check_drugs.setObjectName("check_drugs")
        self.check_sex = QtWidgets.QCheckBox(self.groupBox_7)
        self.check_sex.setGeometry(QtCore.QRect(390, 45, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_sex.setFont(font)
        self.check_sex.setObjectName("check_sex")
        self.label_40 = QtWidgets.QLabel(self.tab_extra_info)
        self.label_40.setGeometry(QtCore.QRect(10, 365, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_extra_info)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 170, 461, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.radio_dreams_yes = QtWidgets.QRadioButton(self.groupBox_8)
        self.radio_dreams_yes.setGeometry(QtCore.QRect(10, 20, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_dreams_yes.setFont(font)
        self.radio_dreams_yes.setObjectName("radio_dreams_yes")
        self.radio_dreams_no = QtWidgets.QRadioButton(self.groupBox_8)
        self.radio_dreams_no.setGeometry(QtCore.QRect(10, 50, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_dreams_no.setFont(font)
        self.radio_dreams_no.setObjectName("radio_dreams_no")
        self.txt_dreams = QtWidgets.QTextEdit(self.groupBox_8)
        self.txt_dreams.setGeometry(QtCore.QRect(130, 10, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_dreams.setFont(font)
        self.txt_dreams.setObjectName("txt_dreams")
        self.cmb_feeding = QtWidgets.QComboBox(self.tab_extra_info)
        self.cmb_feeding.setGeometry(QtCore.QRect(130, 365, 341, 32))
        self.cmb_feeding.setObjectName("cmb_feeding")
        self.cmb_feeding.addItem("")
        self.cmb_feeding.addItem("")
        self.cmb_feeding.addItem("")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_extra_info)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 267, 225, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.txt_work = QtWidgets.QTextEdit(self.groupBox_9)
        self.txt_work.setGeometry(QtCore.QRect(10, 30, 205, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_work.setFont(font)
        self.txt_work.setObjectName("txt_work")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_extra_info)
        self.groupBox_10.setGeometry(QtCore.QRect(250, 267, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName("groupBox_10")
        self.txt_family = QtWidgets.QTextEdit(self.groupBox_10)
        self.txt_family.setGeometry(QtCore.QRect(10, 30, 202, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_family.setFont(font)
        self.txt_family.setObjectName("txt_family")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/user_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_extra_info, icon1, "")
        self.tab_interviews = QtWidgets.QWidget()
        self.tab_interviews.setObjectName("tab_interviews")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_interviews)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 10, 441, 385))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_41 = QtWidgets.QLabel(self.groupBox_11)
        self.label_41.setGeometry(QtCore.QRect(10, 37, 131, 18))
        self.label_41.setObjectName("label_41")
        self.txt_interviewer = QtWidgets.QLineEdit(self.groupBox_11)
        self.txt_interviewer.setGeometry(QtCore.QRect(140, 30, 290, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_interviewer.setFont(font)
        self.txt_interviewer.setObjectName("txt_interviewer")
        self.label_42 = QtWidgets.QLabel(self.groupBox_11)
        self.label_42.setGeometry(QtCore.QRect(10, 83, 131, 18))
        self.label_42.setObjectName("label_42")
        self.cmb_treatment = QtWidgets.QComboBox(self.groupBox_11)
        self.cmb_treatment.setGeometry(QtCore.QRect(120, 77, 310, 32))
        self.cmb_treatment.setObjectName("cmb_treatment")
        self.cmb_treatment.addItem("")
        self.cmb_treatment.addItem("")
        self.cmb_treatment.addItem("")
        self.cmb_treatment.addItem("")
        self.cmb_treatment.addItem("")
        # self.radio_hl = QtWidgets.QRadioButton(self.groupBox_11)
        # self.radio_hl.setGeometry(QtCore.QRect(60, 70, 51, 22))
        # self.radio_hl.setObjectName("radio_hl")
        # self.radio_hl.setVisible(False)
        # self.radio_p12 = QtWidgets.QRadioButton(self.groupBox_11)
        # self.radio_p12.setGeometry(QtCore.QRect(140, 70, 71, 22))
        # self.radio_p12.setObjectName("radio_p12")
        # self.radio_p12.setVisible(False)
        # self.radio_p3e = QtWidgets.QRadioButton(self.groupBox_11)
        # self.radio_p3e.setGeometry(QtCore.QRect(230, 70, 71, 22))
        # self.radio_p3e.setObjectName("radio_p3e")
        # self.radio_p3e.setVisible(False)
        # self.radio_p3f = QtWidgets.QRadioButton(self.groupBox_11)
        # self.radio_p3f.setGeometry(QtCore.QRect(310, 70, 71, 22))
        # self.radio_p3f.setObjectName("radio_p3f")
        # self.radio_p3f.setVisible(False)
        self.txt_interview = QtWidgets.QTextEdit(self.groupBox_11)
        self.txt_interview.setGeometry(QtCore.QRect(10, 120, 421, 209))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_interview.setFont(font)
        self.txt_interview.setObjectName("txt_interview")
        self.btn_new_interview = QtWidgets.QPushButton(self.groupBox_11)
        self.btn_new_interview.setGeometry(QtCore.QRect(10, 340, 201, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_new_interview.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_new_interview.setIcon(icon2)
        self.btn_new_interview.setObjectName("btn_new_interview")
        self.btn_new_interview.clicked.connect(self.btn_new_interview_clicked)
        self.btn_new_interview.setEnabled(False)        
        self.btn_save_interview = QtWidgets.QPushButton(self.groupBox_11)
        self.btn_save_interview.setGeometry(QtCore.QRect(230, 340, 201, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("images/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_interview.setFont(font)
        self.btn_save_interview.setIcon(icon20)
        self.btn_save_interview.setObjectName("btn_save_interview")
        self.btn_save_interview.clicked.connect(self.btn_save_interview_clicked)
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_interviews)
        self.groupBox_12.setGeometry(QtCore.QRect(460, 10, 405, 385))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setObjectName("groupBox_12")
        self.tb_interviews = QtWidgets.QTableWidget(self.groupBox_12)
        self.tb_interviews.setGeometry(QtCore.QRect(10, 30, 385, 345))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tb_interviews.setFont(font)
        self.tb_interviews.setObjectName("tb_interviews")
        self.tb_interviews.setColumnCount(4)
        self.tb_interviews.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_interviews.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_interviews.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_interviews.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_interviews.setHorizontalHeaderItem(3, item)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/overlays.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_interviews, icon3, "")
        self.tab_fowarding = QtWidgets.QWidget()
        self.tab_fowarding.setObjectName("tab_fowarding")
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab_fowarding)
        self.groupBox_19.setGeometry(QtCore.QRect(10, 10, 401, 391))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_19.setFont(font)
        self.groupBox_19.setObjectName("groupBox_19")
        self.check_directors = QtWidgets.QCheckBox(self.groupBox_19)
        self.check_directors.setGeometry(QtCore.QRect(20, 40, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_directors.setFont(font)
        self.check_directors.setObjectName("check_directors")
        self.check_depass = QtWidgets.QCheckBox(self.groupBox_19)
        self.check_depass.setGeometry(QtCore.QRect(110, 40, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_depass.setFont(font)
        self.check_depass.setObjectName("check_depass")
        self.check_social_assistant = QtWidgets.QCheckBox(self.groupBox_19)
        self.check_social_assistant.setGeometry(QtCore.QRect(200, 40, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_social_assistant.setFont(font)
        self.check_social_assistant.setObjectName("check_social_assistant")
        self.check_teaching = QtWidgets.QCheckBox(self.groupBox_19)
        self.check_teaching.setGeometry(QtCore.QRect(300, 40, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_teaching.setFont(font)
        self.check_teaching.setObjectName("check_teaching")
        self.txt_fowarding = QtWidgets.QTextEdit(self.groupBox_19)
        self.txt_fowarding.setGeometry(QtCore.QRect(20, 80, 361, 291))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_fowarding.setFont(font)
        self.txt_fowarding.setObjectName("txt_fowarding")
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_fowarding)
        self.groupBox_13.setGeometry(QtCore.QRect(430, 10, 431, 391))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setObjectName("groupBox_13")
        self.check_preparatory = QtWidgets.QCheckBox(self.groupBox_13)
        self.check_preparatory.setGeometry(QtCore.QRect(30, 30, 291, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_preparatory.setFont(font)
        self.check_preparatory.setObjectName("check_preparatory")
        self.check_basic1 = QtWidgets.QCheckBox(self.groupBox_13)
        self.check_basic1.setGeometry(QtCore.QRect(30, 70, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_basic1.setFont(font)
        self.check_basic1.setObjectName("check_basic1")
        self.check_basic2 = QtWidgets.QCheckBox(self.groupBox_13)
        self.check_basic2.setGeometry(QtCore.QRect(30, 110, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_basic2.setFont(font)
        self.check_basic2.setObjectName("check_basic2")
        self.check_apprentice1 = QtWidgets.QCheckBox(self.groupBox_13)
        self.check_apprentice1.setGeometry(QtCore.QRect(30, 150, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_apprentice1.setFont(font)
        self.check_apprentice1.setObjectName("check_apprentice1")
        self.check_apprentice2 = QtWidgets.QCheckBox(self.groupBox_13)
        self.check_apprentice2.setGeometry(QtCore.QRect(30, 190, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_apprentice2.setFont(font)
        self.check_apprentice2.setObjectName("check_apprentice2")
        self.check_education1 = QtWidgets.QCheckBox(self.groupBox_13)
        self.check_education1.setGeometry(QtCore.QRect(30, 230, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_education1.setFont(font)
        self.check_education1.setObjectName("check_education1")
        self.check_education2 = QtWidgets.QCheckBox(self.groupBox_13)
        self.check_education2.setGeometry(QtCore.QRect(30, 270, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_education2.setFont(font)
        self.check_education2.setObjectName("check_education2")
        self.check_exposer = QtWidgets.QCheckBox(self.groupBox_13)
        self.check_exposer.setGeometry(QtCore.QRect(30, 310, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_exposer.setFont(font)
        self.check_exposer.setObjectName("check_exposer")
        self.check_philosophy = QtWidgets.QCheckBox(self.groupBox_13)
        self.check_philosophy.setGeometry(QtCore.QRect(30, 350, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_philosophy.setFont(font)
        self.check_philosophy.setObjectName("check_philosophy")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../SGA/images/user_go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_fowarding, icon4, "")
        self.tab_guidance = QtWidgets.QWidget()
        self.tab_guidance.setObjectName("tab_guidance")
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_guidance)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 10, 381, 121))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_14.setFont(font)
        self.groupBox_14.setObjectName("groupBox_14")
        self.radio_pasteur_a2 = QtWidgets.QRadioButton(self.groupBox_14)
        self.radio_pasteur_a2.setGeometry(QtCore.QRect(20, 55, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_a2.setFont(font)
        self.radio_pasteur_a2.setObjectName("radio_pasteur_a2")
        self.radio_pasteur_a4 = QtWidgets.QRadioButton(self.groupBox_14)
        self.radio_pasteur_a4.setGeometry(QtCore.QRect(140, 55, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_a4.setFont(font)
        self.radio_pasteur_a4.setObjectName("radio_pasteur_a4")
        self.radio_pasteur_12 = QtWidgets.QRadioButton(self.groupBox_14)
        self.radio_pasteur_12.setGeometry(QtCore.QRect(260, 55, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_12.setFont(font)
        self.radio_pasteur_12.setObjectName("radio_pasteur_12")
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_guidance)
        self.groupBox_15.setGeometry(QtCore.QRect(10, 140, 381, 121))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setObjectName("groupBox_15")
        self.radio_pasteur_a3 = QtWidgets.QRadioButton(self.groupBox_15)
        self.radio_pasteur_a3.setGeometry(QtCore.QRect(50, 55, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_a3.setFont(font)
        self.radio_pasteur_a3.setObjectName("radio_pasteur_a3")
        self.radio_pasteur_3e3m = QtWidgets.QRadioButton(self.groupBox_15)
        self.radio_pasteur_3e3m.setGeometry(QtCore.QRect(210, 55, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_3e3m.setFont(font)
        self.radio_pasteur_3e3m.setObjectName("radio_pasteur_3e3m")
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_guidance)
        self.groupBox_16.setGeometry(QtCore.QRect(10, 270, 381, 121))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setObjectName("groupBox_16")
        self.radio_pasteur_p3f = QtWidgets.QRadioButton(self.groupBox_16)
        self.radio_pasteur_p3f.setGeometry(QtCore.QRect(120, 55, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_p3f.setFont(font)
        self.radio_pasteur_p3f.setObjectName("radio_pasteur_p3f")
        self.groupBox_17 = QtWidgets.QGroupBox(self.tab_guidance)
        self.groupBox_17.setGeometry(QtCore.QRect(400, 10, 461, 231))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setObjectName("groupBox_17")
        self.check_good_thoughts = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_good_thoughts.setGeometry(QtCore.QRect(20, 40, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_good_thoughts.setFont(font)
        self.check_good_thoughts.setObjectName("check_good_thoughts")
        self.check_home_gospel = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_home_gospel.setGeometry(QtCore.QRect(20, 70, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_home_gospel.setFont(font)
        self.check_home_gospel.setObjectName("check_home_gospel")
        self.check_readings = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_readings.setGeometry(QtCore.QRect(20, 100, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_readings.setFont(font)
        self.check_readings.setObjectName("check_readings")
        self.check_doctor = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_doctor.setGeometry(QtCore.QRect(20, 130, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_doctor.setFont(font)
        self.check_doctor.setObjectName("check_doctor")
        self.check_care_package = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_care_package.setGeometry(QtCore.QRect(20, 160, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_care_package.setFont(font)
        self.check_care_package.setObjectName("check_care_package")
        self.check_no_treatment = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_no_treatment.setGeometry(QtCore.QRect(20, 190, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_no_treatment.setFont(font)
        self.check_no_treatment.setObjectName("check_no_treatment")
        self.check_home_sanitation = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_home_sanitation.setGeometry(QtCore.QRect(250, 40, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_home_sanitation.setFont(font)
        self.check_home_sanitation.setObjectName("check_home_sanitation")
        self.check_intimate_makeover = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_intimate_makeover.setGeometry(QtCore.QRect(250, 70, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_intimate_makeover.setFont(font)
        self.check_intimate_makeover.setObjectName("check_intimate_makeover")
        self.check_study = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_study.setGeometry(QtCore.QRect(250, 100, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_study.setFont(font)
        self.check_study.setObjectName("check_study")
        self.check_frequency = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_frequency.setGeometry(QtCore.QRect(250, 130, 181, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_frequency.setFont(font)
        self.check_frequency.setObjectName("check_frequency")
        self.check_no_pass = QtWidgets.QCheckBox(self.groupBox_17)
        self.check_no_pass.setGeometry(QtCore.QRect(250, 160, 181, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_no_pass.setFont(font)
        self.check_no_pass.setObjectName("check_no_pass")
        self.groupBox_18 = QtWidgets.QGroupBox(self.tab_guidance)
        self.groupBox_18.setGeometry(QtCore.QRect(400, 250, 461, 141))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_18.setFont(font)
        self.groupBox_18.setObjectName("groupBox_18")
        self.txt_info = QtWidgets.QTextEdit(self.groupBox_18)
        self.txt_info.setGeometry(QtCore.QRect(10, 30, 441, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_info.setFont(font)
        self.txt_info.setObjectName("txt_info")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/lightbulb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_guidance, icon5, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(500, 470, 391, 171))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btn_add = QtWidgets.QPushButton(self.groupBox)
        self.btn_add.setGeometry(QtCore.QRect(10, 40, 121, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon6)
        self.btn_add.setObjectName("btn_add")
        self.btn_save = QtWidgets.QPushButton(self.groupBox)
        self.btn_save.setGeometry(QtCore.QRect(135, 40, 121, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon7)
        self.btn_save.setObjectName("btn_save")
        self.btn_cancel = QtWidgets.QPushButton(self.groupBox)
        self.btn_cancel.setGeometry(QtCore.QRect(260, 40, 121, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon8)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_delete = QtWidgets.QPushButton(self.groupBox)
        self.btn_delete.setGeometry(QtCore.QRect(135, 80, 121, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/bin_empty.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon9)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_edit = QtWidgets.QPushButton(self.groupBox)
        self.btn_edit.setGeometry(QtCore.QRect(10, 80, 121, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_edit.setFont(font)
        self.btn_edit.setIcon(icon2)
        self.btn_edit.setObjectName("btn_edit")
        self.btn_print = QtWidgets.QPushButton(self.groupBox)
        self.btn_print.setGeometry(QtCore.QRect(260, 80, 121, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_print.setFont(font)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_print.setIcon(icon10)
        self.btn_print.setObjectName("btn_print")
        self.btn_backups = QtWidgets.QPushButton(self.groupBox)
        self.btn_backups.setGeometry(QtCore.QRect(135, 120, 121, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_backups.setFont(font)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/database_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_backups.setIcon(icon11)
        self.btn_backups.setObjectName("btn_backups")
        self.btn_report = QtWidgets.QPushButton(self.groupBox)
        self.btn_report.setGeometry(QtCore.QRect(10, 120, 121, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_report.setFont(font)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_report.setIcon(icon12)
        self.btn_report.setObjectName("btn_report")
        self.btn_log_out = QtWidgets.QPushButton(self.groupBox)
        self.btn_log_out.setGeometry(QtCore.QRect(260, 120, 121, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_log_out.setFont(font)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("images/door_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_log_out.setIcon(icon13)
        self.btn_log_out.setObjectName("btn_log_out")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 470, 481, 171))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.txt_index = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_index.setGeometry(QtCore.QRect(10, 40, 321, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_index.setFont(font)
        self.txt_index.setObjectName("txt_index")
        self.btn_search_index = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_search_index.setGeometry(QtCore.QRect(340, 40, 131, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_search_index.setFont(font)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("images/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search_index.setIcon(icon14)
        self.btn_search_index.setObjectName("btn_search_index")
        self.btn_first = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_first.setGeometry(QtCore.QRect(10, 120, 115, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_first.setFont(font)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("images/resultset_first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_first.setIcon(icon15)
        self.btn_first.setObjectName("btn_first")
        self.btn_previous = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_previous.setGeometry(QtCore.QRect(125, 120, 115, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_previous.setFont(font)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("images/resultset_previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_previous.setIcon(icon16)
        self.btn_previous.setObjectName("btn_previous")
        self.btn_next = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_next.setGeometry(QtCore.QRect(240, 120, 115, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_next.setFont(font)
        self.btn_next.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("images/resultset_next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon17)
        self.btn_next.setObjectName("btn_next")
        self.btn_last = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_last.setGeometry(QtCore.QRect(355, 120, 115, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_last.setFont(font)
        self.btn_last.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("images/resultset_last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_last.setIcon(icon18)
        self.btn_last.setObjectName("btn_last")
        self.lbl_index = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_index.setGeometry(QtCore.QRect(120, 88, 100, 18))
        self.lbl_index.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_index.setObjectName("lbl_index")
        self.lbl_total_index = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_total_index.setGeometry(QtCore.QRect(255, 88, 100, 20))
        self.lbl_total_index.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total_index.setObjectName("lbl_total_index")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(230, 88, 21, 18))
        self.label_3.setObjectName("label_3")
        FormFicha.setCentralWidget(self.centralwidget)
        
                
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_edit.clicked.connect(self.btn_edit_clicked)
        self.btn_print.clicked.connect(self.btn_print_clicked)
        self.btn_backups.clicked.connect(self.btn_backups_clicked)
        self.btn_report.clicked.connect(self.btn_reports_clicked)
        self.btn_log_out.clicked.connect(self.btn_log_out_clicked)

        self.btn_first.clicked.connect(self.btn_first_clicked)
        self.btn_previous.clicked.connect(self.btn_previous_clicked)        
        self.btn_next.clicked.connect(self.btn_next_clicked)
        self.btn_last.clicked.connect(self.btn_last_clicked)

        
        self.enable_read_only()
        if dao_assisted.id_gen_assisted() - 1 != 0:
            self.btn_last_clicked()            
            self.lbl_index.setText(str(dao_assisted.id_gen_assisted() - 1))    
            self.lbl_total_index.setText(str(dao_assisted.id_gen_assisted() - 1))    
        else:
            self.empty_form()
            self.disable_navigation()
            self.lbl_index.setText('0')    
            self.lbl_total_index.setText('0')    
        self.action_buttons()    
        self.fill_table_view()
        

        self.retranslateUi(FormFicha)
        self.tabWidget.setCurrentIndex(0)
        self.cmb_state.setCurrentIndex(22)
        self.cmb_feeding.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FormFicha)

    def retranslateUi(self, FormFicha):
        _translate = QtCore.QCoreApplication.translate
        FormFicha.setWindowTitle(_translate("FormFicha", "GERENCIAMENTO DE ASSISTIDOS"))
        self.label_4.setText(_translate("FormFicha", "NOME"))
        self.label_5.setText(_translate("FormFicha", "DATA DE NASCIMENTO"))
        self.txt_date.setInputMask(_translate("FormFicha", "##/##/####"))
        self.label_6.setText(_translate("FormFicha", "TELEFONE (CELULAR)"))
        self.txt_phone1.setInputMask(_translate("FormFicha", "(##) #####-####"))
        self.txt_phone2.setInputMask(_translate("FormFicha", "(##) #####-####"))
        self.label_7.setText(_translate("FormFicha", "TELEFONE (RESIDENCIAL)"))
        self.label_8.setText(_translate("FormFicha", "GÊNERO"))
        self.cmb_gender.setItemText(0, _translate("FormFicha", "MASCULINO"))
        self.cmb_gender.setItemText(1, _translate("FormFicha", "FEMININO"))
        self.cmb_gender.setItemText(2, _translate("FormFicha", "OUTRO"))
        self.label_14.setText(_translate("FormFicha", "ESTADO CIVIL"))
        self.cmb_civil_state.setItemText(0, _translate("FormFicha", "SOLTEIRO(A)"))
        self.cmb_civil_state.setItemText(1, _translate("FormFicha", "CASADO(A)"))
        self.cmb_civil_state.setItemText(2, _translate("FormFicha", "DIVORCIADO(A)"))
        self.cmb_civil_state.setItemText(3, _translate("FormFicha", "VIÚVO(A)"))
        self.label_21.setText(_translate("FormFicha", "OCUPAÇÃO"))
        self.label_22.setText(_translate("FormFicha", "RESIDE COM"))
        self.label_23.setText(_translate("FormFicha", "ENDEREÇO"))
        self.label_24.setText(_translate("FormFicha", "BAIRRO"))
        self.label_25.setText(_translate("FormFicha", "NÚMERO"))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_personal_data), _translate("FormFicha", "Dados Pessoais"))
        self.groupBox_3.setTitle(_translate("FormFicha", "Características"))
        self.check_depression.setText(_translate("FormFicha", "Depressão Aguda"))
        self.check_mental_disorder.setText(_translate("FormFicha", "Disturbios Mentais"))
        self.check_pre_surgery.setText(_translate("FormFicha", "Pré-Cirurgia"))
        self.check_post_surgery.setText(_translate("FormFicha", "Pós-Cirurgia"))
        self.check_victim_of_violence.setText(_translate("FormFicha", "Vítima de Violência"))
        self.check_acute_physical_illness.setText(_translate("FormFicha", "Doença Física em Fase Aguda"))
        self.check_unknow_disease.setText(_translate("FormFicha", "Doença Grave Desconhecida"))
        self.check_idea_of_eliminate.setText(_translate("FormFicha", "Ideia de Eliminar Alguém"))
        self.check_umbanda.setText(_translate("FormFicha", "Veio da Umbanda"))
        self.check_homicidal.setText(_translate("FormFicha", "Homicida"))
        self.check_possession.setText(_translate("FormFicha", "Fascinação/Possessão"))
        self.check_problems_at_home.setText(_translate("FormFicha", "Problemas Graves no Lar"))
        self.check_aggresive_mental_illness.setText(_translate("FormFicha", "Doença Mental Agressiva"))
        self.check_serious_physical_illness.setText(_translate("FormFicha", "Doença Física Grave"))
        self.check_panic_sindrome.setText(_translate("FormFicha", "Síndrome do Pânico"))
        self.check_violence_practice.setText(_translate("FormFicha", "Prática de Violência"))
        self.check_disappearence.setText(_translate("FormFicha", "Desaparecimento"))
        self.check_problem_continues.setText(_translate("FormFicha", "Problema Continua"))
        self.groupBox_4.setTitle(_translate("FormFicha", "Toma sedativos?"))
        self.radio_sedative_yes.setText(_translate("FormFicha", "SIM"))
        self.radio_sedative_no.setText(_translate("FormFicha", "NÃO"))
        self.groupBox_5.setTitle(_translate("FormFicha", "Trat. Médico?"))
        self.radio_medical_treatment_yes.setText(_translate("FormFicha", "SIM"))
        self.radio_medical_treatment_no.setText(_translate("FormFicha", "NÃO"))
        self.groupBox_6.setTitle(_translate("FormFicha", "Dorme Bem?"))
        self.radio_sleep_well_yes.setText(_translate("FormFicha", "SIM"))
        self.radio_sleep_well_no.setText(_translate("FormFicha", "NÃO"))
        self.groupBox_7.setTitle(_translate("FormFicha", "VÍCIOS"))
        self.radio_addiction_yes.setText(_translate("FormFicha", "SIM"))
        self.radio_addiction_no.setText(_translate("FormFicha", "NÃO"))
        self.check_alcohol.setText(_translate("FormFicha", "Álcool"))
        self.check_tobacco.setText(_translate("FormFicha", "Tabaco"))
        self.check_cigarette.setText(_translate("FormFicha", "Fumo"))
        self.check_drugs.setText(_translate("FormFicha", "Drogas"))
        self.check_sex.setText(_translate("FormFicha", "Sexo"))
        self.label_40.setText(_translate("FormFicha", "ALIMENTAÇÃO"))
        self.radio_dreams_yes.setText(_translate("FormFicha", "SONHOS"))
        self.radio_dreams_no.setText(_translate("FormFicha", "PESADELOS"))
        self.cmb_feeding.setItemText(0, _translate("FormFicha", "POUCA"))
        self.cmb_feeding.setItemText(1, _translate("FormFicha", "REGULAR"))
        self.cmb_feeding.setItemText(2, _translate("FormFicha", "MUITA"))
        self.groupBox_9.setTitle(_translate("FormFicha", "TRABALHO"))
        self.groupBox_10.setTitle(_translate("FormFicha", "FAMÍLIA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_extra_info), _translate("FormFicha", "Informações Extras"))
        self.groupBox_11.setTitle(_translate("FormFicha", "ENTREVISTA"))
        self.label_41.setText(_translate("FormFicha", "ENTREVISTADOR"))
        self.label_42.setText(_translate("FormFicha", "TRATAMENTO"))
        self.cmb_treatment.setItemText(0, _translate("FormFicha", "NENHUM"))
        self.cmb_treatment.setItemText(1, _translate("FormFicha", "HL"))
        self.cmb_treatment.setItemText(2, _translate("FormFicha", "P1/2"))
        self.cmb_treatment.setItemText(3, _translate("FormFicha", "P3E"))
        self.cmb_treatment.setItemText(4, _translate("FormFicha", "P3F"))
        # self.radio_hl.setText(_translate("FormFicha", "HL"))
        # self.radio_p12.setText(_translate("FormFicha", "P1/2"))
        # self.radio_p3e.setText(_translate("FormFicha", "P3E"))
        # self.radio_p3f.setText(_translate("FormFicha", "P3F"))
        self.btn_new_interview.setText(_translate("FormFicha", "NOVA ENTREVISTA"))
        self.btn_save_interview.setText(_translate("FormFicha", "SALVAR"))
        self.groupBox_12.setTitle(_translate("FormFicha", "ENTREVISTAS ANTERIORES"))
        item = self.tb_interviews.horizontalHeaderItem(0)
        item.setText(_translate("FormFicha", "DATA"))
        item = self.tb_interviews.horizontalHeaderItem(1)
        item.setText(_translate("FormFicha", "ENTREVISTADOR"))
        item = self.tb_interviews.horizontalHeaderItem(2)
        item.setText(_translate("FormFicha", "TRATAMENTO"))
        item = self.tb_interviews.horizontalHeaderItem(3)
        item.setText(_translate("FormFicha", "ENTREVISTA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_interviews), _translate("FormFicha", "Entrevistas"))
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
        self.groupBox_18.setTitle(_translate("FormFicha", "INFORMAÇÕES NECESSÁRIAS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_guidance), _translate("FormFicha", "Colegiado"))
        self.groupBox.setTitle(_translate("FormFicha", "AÇÕES"))
        self.btn_add.setText(_translate("FormFicha", "ADICIONAR"))
        self.btn_save.setText(_translate("FormFicha", "SALVAR"))
        self.btn_cancel.setText(_translate("FormFicha", "CANCELAR"))
        self.btn_delete.setText(_translate("FormFicha", "EXCLUIR"))
        self.btn_edit.setText(_translate("FormFicha", "EDITAR"))
        self.btn_print.setText(_translate("FormFicha", "IMPRIMIR"))
        self.btn_backups.setText(_translate("FormFicha", "BACKUPS"))
        self.btn_report.setText(_translate("FormFicha", "RELATÓRIO"))
        self.btn_log_out.setText(_translate("FormFicha", "SAIR"))
        self.groupBox_2.setTitle(_translate("FormFicha", "NAVEGAÇÃO"))
        self.txt_index.setText(_translate("FormFicha", "Digite um indice para ir até ele"))
        self.btn_search_index.setText(_translate("FormFicha", "PESQUISAR"))
        self.btn_first.setText(_translate("FormFicha", "PRIMEIRO"))
        self.btn_previous.setText(_translate("FormFicha", "ANTERIOR"))
        self.btn_next.setText(_translate("FormFicha", "PRÓXIMO"))
        self.btn_last.setText(_translate("FormFicha", "ÚLTIMO"))
        # self.lbl_index.setText(_translate("FormFicha", "0"))
        # self.lbl_total_index.setText(_translate("FormFicha", "0"))
        self.label_3.setText(_translate("FormFicha", "DE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormFicha = QtWidgets.QMainWindow()
    ui = Ui_FormFicha()
    ui.setupUi(FormFicha)
    FormFicha.show()
    sys.exit(app.exec_())
