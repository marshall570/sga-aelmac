# -*- coding: utf-8 -*-
import tkinter
import random
import string
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
from AssistedModel import AssistedModel
from InterviewModel import InterviewModel
from AssistedController import AssistedController

# GLOBAL OBJECTS
assisted_controller = AssistedController()

assisted_model = AssistedModel()
interview_model = InterviewModel()


class Ui_FormFicha(object):
    # FORM VARIABLES
    index = 0
    error_message = ''
    adding = False
    editing = False
    writing_interview = False
    old_values = []
    name = None
    user = None
    category = None
    current_date = datetime.datetime.now()
    current_year = current_date.year

    # PASSIVE METHODS
    @staticmethod
    def get_user():
        result = assisted_controller.select_active_user()

        name = result[0]
        user = result[1]
        category = result[2]

    def empty_form(self):
        self.label_register.setText('Registrado em: ')
        self.label_birth.setText('DATA DE NASCIMENTO')
        self.txt_name.setText('')
        self.txt_date.setText('')
        self.txt_phone.setText('')
        self.txt_ocupation.setText('')
        self.txt_lives_with.setText('')
        self.txt_zip_code.setText('')
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
        self.txt_treatment.setText('')
        self.txt_interview.setPlainText(
            'SALVE O REGISTRO PARA DEPOIS ESCREVER AS ENTREVISTAS')
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
        rs = assisted_controller.select_assisted(self.index)

        new_values = []

        for value in rs:
            if value == None:
                item = ''
            else:
                item = value
            new_values.append(item)

        assisted_model.serial = new_values[0]
        assisted_model.position = new_values[1]
        assisted_model.register_date = new_values[2]
        assisted_model.name = new_values[3]
        assisted_model.date_of_birth = new_values[4]
        assisted_model.phone = new_values[5]
        assisted_model.gender = new_values[6]
        assisted_model.civil_state = new_values[7]
        assisted_model.ocupation = new_values[8]
        assisted_model.lives_with = new_values[9]
        assisted_model.zip_code = new_values[10]
        assisted_model.address = new_values[11]
        assisted_model.neighbourhood = new_values[12]
        assisted_model.number = new_values[13]
        assisted_model.city = new_values[14]
        assisted_model.state = new_values[15]
        assisted_model.sedatives = new_values[16]
        assisted_model.medical_treatment = new_values[17]
        assisted_model.sleep_well = new_values[18]
        assisted_model.addictions = new_values[19]
        assisted_model.dreams = new_values[20]
        assisted_model.work = new_values[21]
        assisted_model.family = new_values[22]
        assisted_model.feeding = new_values[23]
        assisted_model.traits = new_values[24]
        assisted_model.latest_treatment = new_values[25]
        assisted_model.courses = new_values[26]
        assisted_model.fowarding = new_values[27]
        assisted_model.treatment = new_values[28]
        assisted_model.guidance = new_values[29]

        self.clear_table_view()
        self.fill_table_view()

        self.label_register.setText('Registrado em: ' + assisted_model.register_date)
        self.txt_name.setText(assisted_model.name)
        self.label_birth.setText(f'DATA DE NASCIMENTO\n({self.get_age(assisted_model.date_of_birth)})')
        self.txt_date.setText(assisted_model.date_of_birth)
        self.txt_phone.setText(assisted_model.phone)
        self.cmb_gender.setCurrentText(assisted_model.gender)
        self.cmb_civil_state.setCurrentText(assisted_model.civil_state)
        self.txt_ocupation.setText(assisted_model.ocupation)
        self.txt_lives_with.setText(assisted_model.lives_with)
        self.txt_zip_code.setText(assisted_model.zip_code)
        self.txt_address.setText(assisted_model.address)
        self.txt_neighbourhood.setText(assisted_model.neighbourhood)
        self.txt_number.setText(assisted_model.number)
        self.txt_city.setText(assisted_model.city)
        self.cmb_state.setCurrentText(assisted_model.state)

        if assisted_model.sedatives == 'Não':
            self.radio_sedative_no.toggle()
        else:
            self.radio_sedative_yes.toggle()
        if assisted_model.medical_treatment == 'Não':
            self.radio_medical_treatment_no.toggle()
        else:
            self.radio_medical_treatment_yes.toggle()
        if assisted_model.sleep_well == 'Não':
            self.radio_sleep_well_no.toggle()
        else:
            self.radio_sleep_well_yes.toggle()

        if assisted_model.addictions.startswith('Não'):
            self.radio_addiction_no.toggle()
        else:
            self.radio_addiction_yes.toggle()
            if assisted_model.addictions.find('Álcool') != -1:
                self.check_alcohol.toggle()
            if assisted_model.addictions.find('Tabaco') != -1:
                self.check_tobacco.toggle()
            if assisted_model.addictions.find('Fumo') != -1:
                self.check_cigarette.toggle()
            if assisted_model.addictions.find('Drogas') != -1:
                self.check_drugs.toggle()
            if assisted_model.addictions.find('Sexo') != -1:
                self.check_sex.toggle()

        if assisted_model.dreams.startswith('SONHO'):
            self.radio_dreams_yes.toggle()
            self.txt_dreams.setText(assisted_model.dreams[7:])
        else:
            self.radio_dreams_no.toggle()
            self.txt_dreams.setText(assisted_model.dreams[9:])

        self.txt_work.setText(assisted_model.work)
        self.txt_family.setText(assisted_model.family)
        self.cmb_feeding.setCurrentText(assisted_model.feeding)

        if assisted_model.traits.find('Depressão aguda') != -1:
            self.check_depression.toggle()
        if assisted_model.traits.find('Distúrbios mentais') != -1:
            self.check_mental_disorder.toggle()
        if assisted_model.traits.find('Pré-cirurgia') != -1:
            self.check_pre_surgery.toggle()
        if assisted_model.traits.find('Pós-cirurgia') != -1:
            self.check_post_surgery.toggle()
        if assisted_model.traits.find('Vítima de violência') != -1:
            self.check_victim_of_violence.toggle()
        if assisted_model.traits.find('Doença física em fase aguda') != -1:
            self.check_acute_physical_illness.toggle()
        if assisted_model.traits.find('Doença grave desconhecida') != -1:
            self.check_unknow_disease.toggle()
        if assisted_model.traits.find('Ideia de eliminar alguém') != -1:
            self.check_idea_of_eliminate.toggle()
        if assisted_model.traits.find('Veio da Umbanda') != -1:
            self.check_umbanda.toggle()
        if assisted_model.traits.find('Desaparecimento') != -1:
            self.check_disappearence.toggle()
        if assisted_model.traits.find('Homicida') != -1:
            self.check_homicidal.toggle()
        if assisted_model.traits.find('Problema continua') != -1:
            self.check_problem_continues.toggle()
        if assisted_model.traits.find('Prática de violência') != -1:
            self.check_violence_practice.toggle()
        if assisted_model.traits.find('Doença física grave') != -1:
            self.check_serious_physical_illness.toggle()
        if assisted_model.traits.find('Doença mental agressiva') != -1:
            self.check_aggresive_mental_illness.toggle()
        if assisted_model.traits.find('Possessão') != -1:
            self.check_possession.toggle()
        if assisted_model.traits.find('Problemas graves no lar') != -1:
            self.check_problems_at_home.toggle()
        if assisted_model.traits.find('Síndrome do Pânico') != -1:
            self.check_panic_sindrome.toggle()
        if assisted_model.traits.find(' --- ') != -1:
            text = assisted_model.traits.split(' --- ')
            self.txt_traits.setText(text[1])
        else:
            self.txt_traits.setText(assisted_model.traits)

        self.txt_interviewer.setText('')
        self.txt_treatment.setText('')
        self.txt_interview.setText(
            'Clique em <EDITAR> para poder escrever uma entrevista')
        self.btn_save_interview.setEnabled(False)

        if assisted_model.courses.find('Preparatório') != -1:
            self.check_preparatory.toggle()
        if assisted_model.courses.find('Básico 1') != -1:
            self.check_basic1.toggle()
        if assisted_model.courses.find('Básico 2') != -1:
            self.check_basic2.toggle()
        if assisted_model.courses.find('Aprendiz do Evangelho 1') != -1:
            self.check_apprentice1.toggle()
        if assisted_model.courses.find('Aprendiz do Evangelho 2') != -1:
            self.check_apprentice2.toggle()
        if assisted_model.courses.find('Educação Mediúnica 1') != -1:
            self.check_education1.toggle()
        if assisted_model.courses.find('Educação Mediúnica 2') != -1:
            self.check_education2.toggle()
        if assisted_model.courses.find('Expositor') != -1:
            self.check_exposer.toggle()
        if assisted_model.courses.find('Filosofia') != -1:
            self.check_philosophy.toggle()

        if assisted_model.fowarding.find('Diretoria') != -1:
            self.check_directors.toggle()
        if assisted_model.fowarding.find('Depasse') != -1:
            self.check_depass.toggle()
        if assisted_model.fowarding.find('Assistente Social') != -1:
            self.check_social_assistant.toggle()
        if assisted_model.fowarding.find('Ensino') != -1:
            self.check_teaching.toggle()
        if assisted_model.fowarding.find(' --- ') != -1:
            text = assisted_model.fowarding.split(' --- ')
            self.txt_fowarding.setText(text[1])
        else:
            self.txt_fowarding.setText(assisted_model.fowarding)

        if assisted_model.treatment.find('Pasteur A2') != -1:
            self.radio_pasteur_a2.toggle()
        if assisted_model.treatment.find('Pasteur A4') != -1:
            self.radio_pasteur_a4.toggle()
        if assisted_model.treatment.find('Pasteur 1/2') != -1:
            self.radio_pasteur_12.toggle()
        if assisted_model.treatment.find('Pasteur A3') != -1:
            self.radio_pasteur_a3.toggle()
        if assisted_model.treatment.find('Pasteur 3E3M') != -1:
            self.radio_pasteur_3e3m.toggle()
        if assisted_model.treatment.find('Pasteur P3F-Cura') != -1:
            self.radio_pasteur_p3f.toggle()

        if assisted_model.guidance.find('Bons pensamentos') != -1:
            self.check_good_thoughts.toggle()
        if assisted_model.guidance.find('Evangelho no lar') != -1:
            self.check_home_gospel.toggle()
        if assisted_model.guidance.find('Leituras edificantes') != -1:
            self.check_readings.toggle()
        if assisted_model.guidance.find('Médico de confiança') != -1:
            self.check_doctor.toggle()
        if assisted_model.guidance.find('Cesta básica') != -1:
            self.check_care_package.toggle()
        if assisted_model.guidance.find('Não fazer tratamento') != -1:
            self.check_no_treatment.toggle()
        if assisted_model.guidance.find('Higienização do lar') != -1:
            self.check_home_sanitation.toggle()
        if assisted_model.guidance.find('Reforma íntima') != -1:
            self.check_intimate_makeover.toggle()
        if assisted_model.guidance.find('Estudo da doutrina') != -1:
            self.check_study.toggle()
        if assisted_model.guidance.find('Frequência na assistência') != -1:
            self.check_frequency.toggle()
        if assisted_model.guidance.find('Não aplicar passe') != -1:
            self.check_no_pass.toggle()
        if assisted_model.guidance.find(' --- ') != -1:
            text = assisted_model.guidance.split(' --- ')
            self.txt_info.setText(text[1])
        else:
            self.txt_info.setText(assisted_model.guidance)

    def enable_navigation(self):
        self.txt_index.setEnabled(True)

    def disable_navigation(self):
        self.txt_index.setEnabled(False)

    def enable_read_only(self):
        self.txt_name.setReadOnly(True)
        self.txt_date.setReadOnly(True)
        self.txt_phone.setReadOnly(True)
        self.cmb_gender.setEnabled(False)
        self.cmb_civil_state.setEnabled(False)
        self.txt_ocupation.setReadOnly(True)
        self.txt_lives_with.setReadOnly(True)
        self.txt_zip_code.setReadOnly(True)
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
        self.txt_treatment.setReadOnly(False)
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
        self.txt_phone.setReadOnly(False)
        self.cmb_gender.setEnabled(True)
        self.cmb_civil_state.setEnabled(True)
        self.txt_ocupation.setReadOnly(False)
        self.txt_lives_with.setReadOnly(False)
        self.txt_zip_code.setReadOnly(False)
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
        self.txt_treatment.setReadOnly(False)
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
        if assisted_controller.count_assisted() == 0:
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

    def get_values(self, assisted_model):
        addictions = ''
        dreams = ''
        traits = ''
        courses = ''
        fowarding = ''
        treatments = ''
        guidance = ''

        assisted_model.serial = str(self.current_date.year) + '-' + ''.join(
            random.choices(string.ascii_lowercase + string.digits, k=8))
        assisted_model.position = assisted_controller.count_assisted() + 1

        if self.adding is True:
            assisted_model.register_date = self.current_date.strftime('%d/%m/%Y')

        assisted_model.name = self.txt_name.text().strip().upper()
        assisted_model.date_of_birth = self.txt_date.text().strip()
        assisted_model.phone = self.txt_phone.text().strip() if len(
            self.txt_phone.text().strip()) > 13 else ''
        assisted_model.gender = self.cmb_gender.currentText()
        assisted_model.civil_state = self.cmb_civil_state.currentText()
        assisted_model.ocupation = self.txt_ocupation.text().strip().upper()
        assisted_model.lives_with = self.txt_lives_with.text().strip().upper()
        assisted_model.zip_code = self.txt_zip_code.text().strip()
        assisted_model.address = self.shorten_places(
            self.txt_address.text().strip().upper())
        assisted_model.neighbourhood = self.shorten_places(
            self.txt_neighbourhood.text().strip().upper())
        assisted_model.number = self.txt_number.text().strip().upper()
        assisted_model.city = self.txt_city.text().strip().upper()
        assisted_model.state = self.cmb_state.currentText()
        assisted_model.sedatives = 'Sim' if self.radio_sedative_yes.isChecked() else 'Não'
        assisted_model.medical_treatment = 'Sim' if self.radio_medical_treatment_yes.isChecked() else 'Não'
        assisted_model.sleep_well = 'Sim' if self.radio_sleep_well_yes.isChecked() else 'Não'

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
        assisted_model.addictions = addictions

        if self.radio_dreams_yes.isChecked():
            dreams = 'SONHO, '
        else:
            dreams = 'PESADELO, '
        dreams += self.txt_dreams.toPlainText().strip()
        if dreams.endswith(', '):
            dreams = dreams[:-2]
        assisted_model.dreams = dreams

        assisted_model.work = self.txt_work.toPlainText().strip()
        assisted_model.family = self.txt_family.toPlainText().strip()
        assisted_model.feeding = self.cmb_feeding.currentText()

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
        assisted_model.traits = traits

        if self.adding is True:
            assisted_model.latest_treatment = 'NENHUM'
        else:
            assisted_model.latest_treatment = self.txt_treatment.text()

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
        assisted_model.courses = courses

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
        assisted_model.fowarding = fowarding

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
        assisted_model.treatment = treatments

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
        assisted_model.guidance = guidance

    def check_date(self, data):
        date = data.split('/')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])

        if year >= self.current_date.year:
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

    def get_age(self, date):
        split_date = date.split('/')
        birth_year = int(split_date[2])

        if self.current_year - birth_year < 14:
            return 'CRIANÇA'
        else:
            return 'ADULTO'

    def test_mandatory_fields(self):
        self.error_message = ''

        if len(self.txt_name.text().strip()) < 3:
            self.error_message += '- NOME inválido\n'
        if len(self.txt_date.text().strip()) < 10:
            self.error_message += '- DATA DE NASCIMENTO inválida\n'
        else:
            if not self.check_date(self.txt_date.text().strip()):
                self.error_message += '- DATA DE NASCIMENTO inválida\n'
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
        places = ['ALAMEDA', 'AVENIDA', 'BECO', 'BLOCO', 'BOSQUE', 'CONDOMÍNIO', 'CONJUNTO HABITACIONAL', 'FAVELA',
                  'FAZENDA', 'JARDIM', 'LAGO', 'LAGOA', 'LARGO', 'MORRO', 'PARQUE', 'RECANTO', 'RUA', 'TRAVESSA',
                  'VIELA', 'VILA']
        shortened = ['AL.', 'AV.', 'BC.', 'BL.', 'BSQ.', 'COND.', 'COHAB.', 'FAV.', 'FAZ.', 'JD.', 'LG.', 'LGA.',
                     'LRG.', 'MRO.', 'PRQ.', 'REC.', 'R.', 'TV.', 'VLA.', 'VL.']

        i = 0
        txt = text
        while i < len(shortened):
            if text.startswith(places[i]):
                txt = text.replace(places[i], shortened[i], 1)
            i += 1
        return txt

    def fill_table_view(self):
        query_result = assisted_controller.select_interview(assisted_model)

        for value in query_result:
            row = []
            for item in value:
                cell = QtGui.QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)

    def clear_table_view(self):
        self.model.removeRows(0, self.model.rowCount())

    def save_changes(self):
        rs = assisted_controller.select_assisted(self.index)
        for value in rs:
            if value == None:
                item = ''
            else:
                item = value
            self.old_values.append(item)

    def check_changes(self):
        fields = ['Codigo', 'Nome, ', 'Data de Nascimento, ', 'Telefone (celular), ', 'Telefone (residencial), ',
                  'Gênero, ', 'Estado civil, ', 'Ocupação, ', 'Reside com, ', 'CEP, ', 'Endereço, ', 'Bairro, ',
                  'Número, ', 'Cidade, ', 'Estado, ', 'Toma sedativos, ', 'Tratamento médico, ', 'Dorme bem, ',
                  'Vícios, ', 'Sonhos, ', 'Trabalho, ', 'Família, ', 'Alimentação, ', 'Info para DEPOE, ',
                  'Ultimo tratamento, ', 'Cursos, ', 'Encaminhamento, ', 'Tratamentos, ', 'Orientação Espiritual']
        new_values = []

        rs = assisted_controller.select_assisted(self.index)
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
            self.tabWidget.setCurrentIndex(0)

    ####################################################
    # BUTTONS METHODS
    ####################################################

    def btn_log_out_clicked(self):
        this_window = QtWidgets.QApplication.activeWindow()

        root = tkinter.Tk()
        root.withdraw()
        choice = messagebox.askquestion(
            'SAIR DO SISTEMA', 'Deseja sair do sistema?')
        tkinter.Tk().destroy()

        if choice == 'yes':
            from login import Ui_FrameLogin
            assisted_controller.set_off()
            assisted_controller.gen_historic()
            this_window.close()
            self.FormLogin = QtWidgets.QMainWindow()
            self.ui = Ui_FrameLogin()
            self.ui.setupUi(self.FormLogin)
            self.FormLogin.show()

    def btn_reports_clicked(self):
        from report import Ui_FormReports
        self.FormReports = QtWidgets.QMainWindow()
        self.ui = Ui_FormReports()
        self.ui.setupUi(self.FormReports)
        self.FormReports.show()

    def btn_backups_clicked(self):
        from backup import Ui_FormBackup
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
        self.txt_treatment.setEnabled(False)
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

        if assisted_controller.count_assisted() <= 0:
            self.empty_form()
        else:
            self.fill_form()

    def btn_save_clicked(self):
        if not self.test_mandatory_fields():
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror(
                'ERRO', 'Não foi possível concluir o salvamento devido os seguintes erros:\n\n' + self.error_message)
            tkinter.Tk().destroy()
        else:
            root = tkinter.Tk()
            root.withdraw()
            choice = messagebox.askquestion(
                'SALVAR MODIFICAÇÕES', 'Deseja salvar as alterações feitas?')
            tkinter.Tk().destroy()

            if choice == 'yes':
                historic_message = ''

                if self.adding == True and self.editing == False:
                    self.get_values(assisted_model)
                    historic_message = f'ADICIONOU o registro de <{self.txt_name.text().strip().upper()}>'
                    assisted_controller.insert_assisted(assisted_model)
                    assisted_controller.register_changes(
                        self.name, historic_message)

                    self.txt_index.setMaximum(
                        assisted_controller.count_assisted())
                    self.txt_index.setMinimum(0)
                    self.txt_index.setValue(
                        assisted_controller.count_assisted())

                elif self.editing == True and self.adding == False:
                    self.save_changes()
                    self.get_values(assisted_model)
                    assisted_controller.update_assisted(
                        assisted_model, self.index)

                    historic_message = f'EDITOU no registro de <{self.txt_name.text().strip().upper()}>: '
                    historic_message += self.check_changes()
                    assisted_controller.register_changes(
                        self.name, historic_message)
                    self.fill_form()

                self.btn_cancel_clicked()

    def btn_delete_clicked(self):
        root = tkinter.Tk()
        root.withdraw()
        choice = messagebox.askquestion(
            'DELETAR REGISTRO', f'Deseja DELETAR o registro de <{assisted_model.name}>?')
        tkinter.Tk().destroy()

        if choice == 'yes':
            self.clear_table_view()
            assisted_controller.delete_assisted(self.index)
            historic_message = f'DELETOU o registro de <{assisted_model.name}>'
            assisted_controller.register_changes(self.name, historic_message)
            if assisted_controller.count_assisted() == 0:
                self.txt_index.setMaximum(0)
                self.txt_index.setMinimum(0)
                self.empty_form()
                self.action_buttons()
            else:
                self.txt_index.setMaximum(assisted_controller.count_assisted())

                if self.index > assisted_controller.count_assisted():
                    self.index -= 1
                elif self.index < assisted_controller.count_assisted():
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

        self.txt_interview.setText(
            'Clique em <NOVA ENTREVISTA> para escrever uma entrevista')

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
        if assisted_controller.count_interviews(assisted_model) > 2:
            root = tkinter.Tk()
            root.withdraw()
            choice = messagebox.askquestion(
                'IMPRESSÃO', 'Parece que esse registro possui três ou mais entrevistas.\nDeseja imprimir apenas as entrevistas mais recentes?')
            tkinter.Tk().destroy()

            if choice == 'yes':
                assisted_controller.print_interviews(assisted_model)
            else:
                assisted_controller.print_register(assisted_model, self.index)
        else:
            assisted_controller.print_register(assisted_model, self.index)

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
            new_icon = QtGui.QIcon.fromTheme('dialog-cancel')
            self.btn_new_interview.setIcon(new_icon)
            self.btn_new_interview.setText('CANCELAR')

            self.btn_save.setEnabled(False)
            self.btn_cancel.setEnabled(False)

            self.tab_personal_data.setEnabled(False)
            self.tab_extra_info.setEnabled(False)
            self.tab_fowarding.setEnabled(False)
            self.tab_guidance.setEnabled(False)

            self.txt_interviewer.setReadOnly(False)
            self.txt_treatment.setEnabled(True)
            self.txt_interview.setReadOnly(False)
            self.btn_save_interview.setEnabled(True)
            self.btn_new_interview.setEnabled(True)

            self.txt_interviewer.setFocus()
            self.txt_interviewer.setText(self.name)
            self.txt_interview.setText('')

            self.writing_interview = True

        else:
            new_icon = QtGui.QIcon.fromTheme('document-edit')            
            self.btn_new_interview.setIcon(new_icon)
            self.btn_new_interview.setText('NOVA ENTREVISTA')

            self.btn_save.setEnabled(False)
            self.btn_cancel.setEnabled(True)

            self.tab_personal_data.setEnabled(True)
            self.tab_extra_info.setEnabled(True)
            self.tab_fowarding.setEnabled(True)
            self.tab_guidance.setEnabled(True)

            self.txt_interviewer.setReadOnly(True)
            self.txt_treatment.setEnabled(False)
            self.txt_interview.setReadOnly(True)
            self.btn_save_interview.setEnabled(False)
            self.btn_new_interview.setEnabled(True)

            self.writing_interview = False

    def btn_save_interview_clicked(self):
        if len(self.txt_interviewer.text().strip()) < 1 or len(self.txt_interview.toPlainText().strip()) < 1:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror(
                'ERRO', 'Os campos ENTREVISTADOR e ENTREVISTA precisam estar PREENCHIDOS')
            tkinter.Tk().destroy()

        else:
            root = tkinter.Tk()
            root.withdraw()
            choice = messagebox.askquestion(
                'REGISTRAR ENTREVISTA', 'Deseja registrar esta entrevista?')
            tkinter.Tk().destroy()

            if choice == 'yes':
                interview_model.code = ''.join(random.choices(
                    string.ascii_lowercase + string.digits, k=8))
                interview_model.date = self.current_date.strftime('%d/%m/%Y')
                interview_model.interviewer = self.txt_interviewer.text().strip().upper()
                interview_model.treatment = self.txt_treatment.text().strip().upper()
                interview_model.interview = self.txt_interview.toPlainText().strip()

                assisted_controller.insert_interview(
                    interview_model, assisted_model)
                historic_message = f'Adicionou uma ENTREVISTA ao registro de <{self.txt_name.text().strip().upper()}>'
                assisted_controller.register_changes(
                    self.name, historic_message)
                self.btn_new_interview_clicked()
                self.clear_table_view()
                self.fill_table_view()
                self.tabWidget.setCurrentIndex(4)

    def cell_double_clicked(self, signal):
        row = signal.row()
        values = []

        for i in range(4):
            index = signal.sibling(row, i)
            index_dict = self.model.itemData(index)
            values.append(index_dict.get(0))

        self.txt_interviewer.setText(values[1])
        self.txt_treatment.setText(values[2])
        self.txt_interview.setPlainText(values[3])

    def setupUi(self, FormFicha):
        FormFicha.setObjectName("FormFicha")
        FormFicha.setWindowTitle("GERENCIADOR DE ASSISTIDOS")
        self.centralwidget = QtWidgets.QWidget(FormFicha)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_register = QtWidgets.QLabel(self.centralwidget)
        self.label_register.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_register.sizePolicy().hasHeightForWidth())
        self.label_register.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_register.setFont(font)
        self.label_register.setText("Registrado em : ")
        self.label_register.setObjectName("label_register")
        self.gridLayout.addWidget(self.label_register, 0, 1, 1, 1)
        self.txt_index = QtWidgets.QSpinBox(self.centralwidget)
        self.txt_index.setObjectName("txt_index")
        self.gridLayout.addWidget(self.txt_index, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 175))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 175))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("AÇÕES")
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
        self.btn_add.setText("ADICIONAR")
        icon = QtGui.QIcon.fromTheme("list-add")
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
        self.btn_save.setText("SALVAR")
        icon = QtGui.QIcon.fromTheme("document-save")
        self.btn_save.setIcon(icon)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_3.addWidget(self.btn_save, 0, 1, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setText("CANCELAR")
        icon = QtGui.QIcon.fromTheme("dialog-cancel")
        self.btn_cancel.setIcon(icon)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_3.addWidget(self.btn_cancel, 0, 2, 1, 1)
        self.btn_edit = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_edit.setFont(font)
        self.btn_edit.setText("EDITAR")
        icon = QtGui.QIcon.fromTheme("document-edit")
        self.btn_edit.setIcon(icon)
        self.btn_edit.setObjectName("btn_edit")
        self.gridLayout_3.addWidget(self.btn_edit, 1, 0, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setText("EXCLUIR")
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.btn_delete.setIcon(icon)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout_3.addWidget(self.btn_delete, 1, 1, 1, 1)
        self.btn_print = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_print.setFont(font)
        self.btn_print.setText("IMPRIMIR")
        icon = QtGui.QIcon.fromTheme("document-print")
        self.btn_print.setIcon(icon)
        self.btn_print.setObjectName("btn_print")
        self.gridLayout_3.addWidget(self.btn_print, 1, 2, 1, 1)
        self.btn_report = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_report.setFont(font)
        self.btn_report.setText("RELATÓRIO")
        icon = QtGui.QIcon.fromTheme("filename-title-amarok")
        self.btn_report.setIcon(icon)
        self.btn_report.setObjectName("btn_report")
        self.gridLayout_3.addWidget(self.btn_report, 2, 0, 1, 1)
        self.btn_backups = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_backups.setFont(font)
        self.btn_backups.setText("BACKUPS")
        icon = QtGui.QIcon.fromTheme("network-server-database")
        self.btn_backups.setIcon(icon)
        self.btn_backups.setObjectName("btn_backups")
        self.gridLayout_3.addWidget(self.btn_backups, 2, 1, 1, 1)
        self.btn_log_out = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_log_out.setFont(font)
        self.btn_log_out.setText("SAIR")
        icon = QtGui.QIcon.fromTheme("system-shutdown")
        self.btn_log_out.setIcon(icon)
        self.btn_log_out.setObjectName("btn_log_out")
        self.gridLayout_3.addWidget(self.btn_log_out, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_personal_data = QtWidgets.QWidget()
        self.tab_personal_data.setObjectName("tab_personal_data")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_personal_data)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txt_name = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_name.setFont(font)
        self.txt_name.setText("")
        self.txt_name.setObjectName("txt_name")
        self.gridLayout_2.addWidget(self.txt_name, 2, 1, 1, 9)
        self.cmb_state = QtWidgets.QComboBox(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.cmb_state.setFont(font)
        self.cmb_state.setCurrentText("ACRE")
        self.cmb_state.setObjectName("cmb_state")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(0, "ACRE")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(1, "ALAGOAS")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(2, "AMAPÁ")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(3, "AMAZONAS")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(4, "BAHIA")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(5, "CEARÁ")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(6, "ESPÍRITO SANTO")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(7, "MARANHÃO")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(8, "MATO GROSSO")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(9, "MATO GROSSO DO SUL")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(10, "MINAS GERAIS")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(11, "PARÁ")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(12, "PARAÍBA")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(13, "PARANÁ")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(14, "PERNAMBUCO")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(15, "PIAUÍ")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(16, "RIO DE JANEIRO")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(17, "RIO GRANDE DO NORTE")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(18, "RIO GRANDE DO SUL")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(19, "RONDÔNIA")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(20, "RORAIMA")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(21, "SANTA CATARINA")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(22, "SÃO PAULO")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(23, "SERGIPE")
        self.cmb_state.addItem("")
        self.cmb_state.setItemText(24, "TOCANTINS")
        self.gridLayout_2.addWidget(self.cmb_state, 9, 8, 1, 2)
        self.label_23 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setText("CEP")
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("NOME")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.txt_number = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_number.setFont(font)
        self.txt_number.setText("")
        self.txt_number.setObjectName("txt_number")
        self.gridLayout_2.addWidget(self.txt_number, 9, 2, 1, 5)
        self.cmb_gender = QtWidgets.QComboBox(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cmb_gender.sizePolicy().hasHeightForWidth())
        self.cmb_gender.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.cmb_gender.setFont(font)
        self.cmb_gender.setCurrentText("MASCULINO")
        self.cmb_gender.setObjectName("cmb_gender")
        self.cmb_gender.addItem("")
        self.cmb_gender.setItemText(0, "MASCULINO")
        self.cmb_gender.addItem("")
        self.cmb_gender.setItemText(1, "FEMININO")
        self.cmb_gender.addItem("")
        self.cmb_gender.setItemText(2, "OUTRO")
        self.gridLayout_2.addWidget(self.cmb_gender, 4, 7, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setText("GÊNERO")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 7, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setText("OCUPAÇÃO")
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 5, 0, 1, 2)
        self.label_birth = QtWidgets.QLabel(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_birth.sizePolicy().hasHeightForWidth())
        self.label_birth.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_birth.setFont(font)
        self.label_birth.setText("DATA DE NASCIMENTO")
        self.label_birth.setAlignment(QtCore.Qt.AlignCenter)
        self.label_birth.setObjectName("label_birth")
        self.gridLayout_2.addWidget(self.label_birth, 3, 0, 1, 4)
        self.txt_address = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_address.setFont(font)
        self.txt_address.setText("")
        self.txt_address.setObjectName("txt_address")
        self.gridLayout_2.addWidget(self.txt_address, 7, 5, 1, 5)
        self.txt_zip_code = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_zip_code.setFont(font)
        self.txt_zip_code.setInputMask("#####-###")
        self.txt_zip_code.setText("-")
        self.txt_zip_code.setObjectName("txt_zip_code")
        self.gridLayout_2.addWidget(self.txt_zip_code, 7, 1, 1, 3)
        self.label_25 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setText("CIDADE")
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 8, 8, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setText("NÚMERO")
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 9, 0, 1, 2)
        self.txt_city = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_city.setFont(font)
        self.txt_city.setText("")
        self.txt_city.setObjectName("txt_city")
        self.gridLayout_2.addWidget(self.txt_city, 8, 9, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setText("ESTADO")
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 9, 7, 1, 1)
        self.txt_lives_with = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_lives_with.setFont(font)
        self.txt_lives_with.setText("")
        self.txt_lives_with.setObjectName("txt_lives_with")
        self.gridLayout_2.addWidget(self.txt_lives_with, 6, 3, 1, 7)
        self.txt_neighbourhood = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_neighbourhood.setFont(font)
        self.txt_neighbourhood.setText("")
        self.txt_neighbourhood.setObjectName("txt_neighbourhood")
        self.gridLayout_2.addWidget(self.txt_neighbourhood, 8, 2, 1, 6)
        self.label_14 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setText("ESTADO CIVIL")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 3, 9, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setText("RESIDE COM")
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 6, 0, 1, 3)
        self.label_27 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setText("ENDEREÇO")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 7, 4, 1, 1)
        self.cmb_civil_state = QtWidgets.QComboBox(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cmb_civil_state.sizePolicy().hasHeightForWidth())
        self.cmb_civil_state.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.cmb_civil_state.setFont(font)
        self.cmb_civil_state.setCurrentText("SOLTEIRO(A)")
        self.cmb_civil_state.setObjectName("cmb_civil_state")
        self.cmb_civil_state.addItem("")
        self.cmb_civil_state.setItemText(0, "SOLTEIRO(A)")
        self.cmb_civil_state.addItem("")
        self.cmb_civil_state.setItemText(1, "CASADO(A)")
        self.cmb_civil_state.addItem("")
        self.cmb_civil_state.setItemText(2, "DIVORCIADO(A)")
        self.cmb_civil_state.addItem("")
        self.cmb_civil_state.setItemText(3, "VIÚVO(A)")
        self.gridLayout_2.addWidget(self.cmb_civil_state, 4, 9, 1, 1)
        self.txt_ocupation = QtWidgets.QLineEdit(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_ocupation.setFont(font)
        self.txt_ocupation.setText("")
        self.txt_ocupation.setObjectName("txt_ocupation")
        self.gridLayout_2.addWidget(self.txt_ocupation, 5, 3, 1, 7)
        self.txt_date = QtWidgets.QLineEdit(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txt_date.sizePolicy().hasHeightForWidth())
        self.txt_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_date.setFont(font)
        self.txt_date.setInputMask("##/##/####")
        self.txt_date.setText("//")
        self.txt_date.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_date.setObjectName("txt_date")
        self.gridLayout_2.addWidget(self.txt_date, 4, 0, 1, 4)
        self.label_7 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setText("TELEFONE")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 4, 1, 3)
        self.txt_phone = QtWidgets.QLineEdit(self.tab_personal_data)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txt_phone.sizePolicy().hasHeightForWidth())
        self.txt_phone.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_phone.setFont(font)
        self.txt_phone.setInputMask("(##) ##########")
        self.txt_phone.setText("() ")
        self.txt_phone.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_phone.setObjectName("txt_phone")
        self.gridLayout_2.addWidget(self.txt_phone, 4, 4, 1, 3)
        self.label_24 = QtWidgets.QLabel(self.tab_personal_data)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setText("BAIRRO")
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 8, 0, 1, 2)
        icon = QtGui.QIcon.fromTheme("user")
        self.tabWidget.addTab(self.tab_personal_data, icon, "Dados Pessoais")
        self.tab_extra_info = QtWidgets.QWidget()
        self.tab_extra_info.setObjectName("tab_extra_info")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_extra_info)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cmb_feeding = QtWidgets.QComboBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cmb_feeding.sizePolicy().hasHeightForWidth())
        self.cmb_feeding.setSizePolicy(sizePolicy)
        self.cmb_feeding.setCurrentText("POUCA")
        self.cmb_feeding.setObjectName("cmb_feeding")
        self.cmb_feeding.addItem("")
        self.cmb_feeding.setItemText(0, "POUCA")
        self.cmb_feeding.addItem("")
        self.cmb_feeding.setItemText(1, "REGULAR")
        self.cmb_feeding.addItem("")
        self.cmb_feeding.setItemText(2, "MUITA")
        self.gridLayout_5.addWidget(self.cmb_feeding, 4, 1, 1, 5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setTitle("Toma sedativos?")
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
        self.radio_sedative_yes.setText("SIM")
        self.radio_sedative_yes.setObjectName("radio_sedative_yes")
        self.verticalLayout.addWidget(self.radio_sedative_yes)
        self.radio_sedative_no = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_sedative_no.setFont(font)
        self.radio_sedative_no.setText("NÃO")
        self.radio_sedative_no.setObjectName("radio_sedative_no")
        self.verticalLayout.addWidget(self.radio_sedative_no)
        self.gridLayout_5.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setTitle("FAMÍLIA")
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setTitle("TRABALHO")
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
        self.radio_dreams_yes.setText("SONHOS")
        self.radio_dreams_yes.setObjectName("radio_dreams_yes")
        self.gridLayout_9.addWidget(self.radio_dreams_yes, 0, 0, 1, 1)
        self.txt_dreams = QtWidgets.QTextEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txt_dreams.sizePolicy().hasHeightForWidth())
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
        self.radio_dreams_no.setText("PESADELOS")
        self.radio_dreams_no.setObjectName("radio_dreams_no")
        self.gridLayout_9.addWidget(self.radio_dreams_no, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_8, 2, 0, 1, 6)
        self.label_40 = QtWidgets.QLabel(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setText("ALIMENTAÇÃO")
        self.label_40.setObjectName("label_40")
        self.gridLayout_5.addWidget(self.label_40, 4, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setTitle("VÍCIOS")
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
        self.check_tobacco.setText("Tabaco")
        self.check_tobacco.setObjectName("check_tobacco")
        self.gridLayout_10.addWidget(self.check_tobacco, 1, 1, 1, 1)
        self.radio_addiction_yes = QtWidgets.QRadioButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_addiction_yes.setFont(font)
        self.radio_addiction_yes.setText("SIM")
        self.radio_addiction_yes.setObjectName("radio_addiction_yes")
        self.gridLayout_10.addWidget(self.radio_addiction_yes, 0, 0, 1, 1)
        self.check_alcohol = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_alcohol.setFont(font)
        self.check_alcohol.setText("Álcool")
        self.check_alcohol.setObjectName("check_alcohol")
        self.gridLayout_10.addWidget(self.check_alcohol, 0, 1, 1, 1)
        self.check_drugs = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_drugs.setFont(font)
        self.check_drugs.setText("Drogas")
        self.check_drugs.setObjectName("check_drugs")
        self.gridLayout_10.addWidget(self.check_drugs, 1, 2, 1, 1)
        self.radio_addiction_no = QtWidgets.QRadioButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_addiction_no.setFont(font)
        self.radio_addiction_no.setText("NÃO")
        self.radio_addiction_no.setObjectName("radio_addiction_no")
        self.gridLayout_10.addWidget(self.radio_addiction_no, 1, 0, 1, 1)
        self.check_cigarette = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_cigarette.setFont(font)
        self.check_cigarette.setText("Fumo")
        self.check_cigarette.setObjectName("check_cigarette")
        self.gridLayout_10.addWidget(self.check_cigarette, 0, 2, 1, 1)
        self.check_sex = QtWidgets.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_sex.setFont(font)
        self.check_sex.setText("Sexo")
        self.check_sex.setObjectName("check_sex")
        self.gridLayout_10.addWidget(self.check_sex, 0, 3, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_7, 1, 0, 1, 6)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setTitle("Características")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.check_depression = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_depression.sizePolicy().hasHeightForWidth())
        self.check_depression.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_depression.setFont(font)
        self.check_depression.setText("Depressão Aguda")
        self.check_depression.setObjectName("check_depression")
        self.gridLayout_11.addWidget(self.check_depression, 0, 0, 1, 1)
        self.check_disappearence = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_disappearence.sizePolicy().hasHeightForWidth())
        self.check_disappearence.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_disappearence.setFont(font)
        self.check_disappearence.setText("Desaparecimento")
        self.check_disappearence.setObjectName("check_disappearence")
        self.gridLayout_11.addWidget(self.check_disappearence, 0, 1, 1, 1)
        self.check_mental_disorder = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_mental_disorder.sizePolicy().hasHeightForWidth())
        self.check_mental_disorder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_mental_disorder.setFont(font)
        self.check_mental_disorder.setText("Disturbios Mentais")
        self.check_mental_disorder.setObjectName("check_mental_disorder")
        self.gridLayout_11.addWidget(self.check_mental_disorder, 1, 0, 1, 1)
        self.check_homicidal = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_homicidal.sizePolicy().hasHeightForWidth())
        self.check_homicidal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_homicidal.setFont(font)
        self.check_homicidal.setText("Homicida")
        self.check_homicidal.setObjectName("check_homicidal")
        self.gridLayout_11.addWidget(self.check_homicidal, 1, 1, 1, 1)
        self.check_pre_surgery = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_pre_surgery.sizePolicy().hasHeightForWidth())
        self.check_pre_surgery.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_pre_surgery.setFont(font)
        self.check_pre_surgery.setText("Pré-Cirurgia")
        self.check_pre_surgery.setObjectName("check_pre_surgery")
        self.gridLayout_11.addWidget(self.check_pre_surgery, 2, 0, 1, 1)
        self.check_problem_continues = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_problem_continues.sizePolicy().hasHeightForWidth())
        self.check_problem_continues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_problem_continues.setFont(font)
        self.check_problem_continues.setText("Problema Continua")
        self.check_problem_continues.setObjectName("check_problem_continues")
        self.gridLayout_11.addWidget(self.check_problem_continues, 2, 1, 1, 1)
        self.check_post_surgery = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_post_surgery.sizePolicy().hasHeightForWidth())
        self.check_post_surgery.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_post_surgery.setFont(font)
        self.check_post_surgery.setText("Pós-Cirurgia")
        self.check_post_surgery.setObjectName("check_post_surgery")
        self.gridLayout_11.addWidget(self.check_post_surgery, 3, 0, 1, 1)
        self.check_violence_practice = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_violence_practice.sizePolicy().hasHeightForWidth())
        self.check_violence_practice.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_violence_practice.setFont(font)
        self.check_violence_practice.setText("Prática de Violência")
        self.check_violence_practice.setObjectName("check_violence_practice")
        self.gridLayout_11.addWidget(self.check_violence_practice, 3, 1, 1, 1)
        self.check_victim_of_violence = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_victim_of_violence.sizePolicy().hasHeightForWidth())
        self.check_victim_of_violence.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_victim_of_violence.setFont(font)
        self.check_victim_of_violence.setText("Vítima de Violência")
        self.check_victim_of_violence.setObjectName("check_victim_of_violence")
        self.gridLayout_11.addWidget(self.check_victim_of_violence, 4, 0, 1, 1)
        self.check_serious_physical_illness = QtWidgets.QCheckBox(
            self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_serious_physical_illness.sizePolicy().hasHeightForWidth())
        self.check_serious_physical_illness.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_serious_physical_illness.setFont(font)
        self.check_serious_physical_illness.setText("Doença Física Grave")
        self.check_serious_physical_illness.setObjectName(
            "check_serious_physical_illness")
        self.gridLayout_11.addWidget(
            self.check_serious_physical_illness, 4, 1, 1, 1)
        self.check_acute_physical_illness = QtWidgets.QCheckBox(
            self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_acute_physical_illness.sizePolicy().hasHeightForWidth())
        self.check_acute_physical_illness.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.check_acute_physical_illness.setFont(font)
        self.check_acute_physical_illness.setText(
            "Doença Física em Fase Aguda")
        self.check_acute_physical_illness.setObjectName(
            "check_acute_physical_illness")
        self.gridLayout_11.addWidget(
            self.check_acute_physical_illness, 5, 0, 1, 1)
        self.check_aggresive_mental_illness = QtWidgets.QCheckBox(
            self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_aggresive_mental_illness.sizePolicy().hasHeightForWidth())
        self.check_aggresive_mental_illness.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_aggresive_mental_illness.setFont(font)
        self.check_aggresive_mental_illness.setText("Doença Mental Agressiva")
        self.check_aggresive_mental_illness.setObjectName(
            "check_aggresive_mental_illness")
        self.gridLayout_11.addWidget(
            self.check_aggresive_mental_illness, 5, 1, 1, 1)
        self.check_unknow_disease = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_unknow_disease.sizePolicy().hasHeightForWidth())
        self.check_unknow_disease.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_unknow_disease.setFont(font)
        self.check_unknow_disease.setText("Doença Grave Desconhecida")
        self.check_unknow_disease.setObjectName("check_unknow_disease")
        self.gridLayout_11.addWidget(self.check_unknow_disease, 6, 0, 1, 1)
        self.check_possession = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_possession.sizePolicy().hasHeightForWidth())
        self.check_possession.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_possession.setFont(font)
        self.check_possession.setText("Fascinação/Possessão")
        self.check_possession.setObjectName("check_possession")
        self.gridLayout_11.addWidget(self.check_possession, 6, 1, 1, 1)
        self.check_idea_of_eliminate = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_idea_of_eliminate.sizePolicy().hasHeightForWidth())
        self.check_idea_of_eliminate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_idea_of_eliminate.setFont(font)
        self.check_idea_of_eliminate.setText("Ideia de Eliminar Alguém")
        self.check_idea_of_eliminate.setObjectName("check_idea_of_eliminate")
        self.gridLayout_11.addWidget(self.check_idea_of_eliminate, 7, 0, 1, 1)
        self.check_problems_at_home = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_problems_at_home.sizePolicy().hasHeightForWidth())
        self.check_problems_at_home.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_problems_at_home.setFont(font)
        self.check_problems_at_home.setText("Problemas Graves no Lar")
        self.check_problems_at_home.setObjectName("check_problems_at_home")
        self.gridLayout_11.addWidget(self.check_problems_at_home, 7, 1, 1, 1)
        self.check_umbanda = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_umbanda.sizePolicy().hasHeightForWidth())
        self.check_umbanda.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_umbanda.setFont(font)
        self.check_umbanda.setText("Veio da Umbanda")
        self.check_umbanda.setObjectName("check_umbanda")
        self.gridLayout_11.addWidget(self.check_umbanda, 8, 0, 1, 1)
        self.check_panic_sindrome = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.check_panic_sindrome.sizePolicy().hasHeightForWidth())
        self.check_panic_sindrome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_panic_sindrome.setFont(font)
        self.check_panic_sindrome.setText("Síndrome do Pânico")
        self.check_panic_sindrome.setObjectName("check_panic_sindrome")
        self.gridLayout_11.addWidget(self.check_panic_sindrome, 8, 1, 1, 1)
        self.txt_traits = QtWidgets.QTextEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txt_traits.sizePolicy().hasHeightForWidth())
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setTitle("Dorme Bem?")
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
        self.radio_sleep_well_yes.setText("SIM")
        self.radio_sleep_well_yes.setObjectName("radio_sleep_well_yes")
        self.verticalLayout_3.addWidget(self.radio_sleep_well_yes)
        self.radio_sleep_well_no = QtWidgets.QRadioButton(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_sleep_well_no.setFont(font)
        self.radio_sleep_well_no.setText("NÃO")
        self.radio_sleep_well_no.setObjectName("radio_sleep_well_no")
        self.verticalLayout_3.addWidget(self.radio_sleep_well_no)
        self.gridLayout_5.addWidget(self.groupBox_6, 0, 5, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_extra_info)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setTitle("Trat. Médico?")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radio_medical_treatment_yes = QtWidgets.QRadioButton(
            self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_medical_treatment_yes.setFont(font)
        self.radio_medical_treatment_yes.setText("SIM")
        self.radio_medical_treatment_yes.setObjectName(
            "radio_medical_treatment_yes")
        self.verticalLayout_2.addWidget(self.radio_medical_treatment_yes)
        self.radio_medical_treatment_no = QtWidgets.QRadioButton(
            self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_medical_treatment_no.setFont(font)
        self.radio_medical_treatment_no.setText("NÃO")
        self.radio_medical_treatment_no.setObjectName(
            "radio_medical_treatment_no")
        self.verticalLayout_2.addWidget(self.radio_medical_treatment_no)
        self.gridLayout_5.addWidget(self.groupBox_5, 0, 2, 1, 3)
        icon = QtGui.QIcon.fromTheme("list-add-user")
        self.tabWidget.addTab(self.tab_extra_info, icon, "Informações Extras")
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
        self.groupBox_19.setTitle("ENCAMINHAMENTO")
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
        self.check_directors.setText("Diretoria")
        self.check_directors.setObjectName("check_directors")
        self.gridLayout_14.addWidget(self.check_directors, 0, 0, 1, 1)
        self.check_depass = QtWidgets.QCheckBox(self.groupBox_19)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_depass.setFont(font)
        self.check_depass.setText("Depasse")
        self.check_depass.setObjectName("check_depass")
        self.gridLayout_14.addWidget(self.check_depass, 0, 1, 1, 1)
        self.check_social_assistant = QtWidgets.QCheckBox(self.groupBox_19)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_social_assistant.setFont(font)
        self.check_social_assistant.setText("Ast. Social")
        self.check_social_assistant.setObjectName("check_social_assistant")
        self.gridLayout_14.addWidget(self.check_social_assistant, 0, 2, 1, 1)
        self.check_teaching = QtWidgets.QCheckBox(self.groupBox_19)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_teaching.setFont(font)
        self.check_teaching.setText("Ensino")
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
        self.groupBox_13.setTitle("FREQUÊNCIA")
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
        self.check_preparatory.setText("Preparatório (O que é Espiritísmo?)")
        self.check_preparatory.setObjectName("check_preparatory")
        self.verticalLayout_4.addWidget(self.check_preparatory)
        self.check_basic1 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_basic1.setFont(font)
        self.check_basic1.setText("1º Básico")
        self.check_basic1.setObjectName("check_basic1")
        self.verticalLayout_4.addWidget(self.check_basic1)
        self.check_basic2 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_basic2.setFont(font)
        self.check_basic2.setText("2º Básico")
        self.check_basic2.setObjectName("check_basic2")
        self.verticalLayout_4.addWidget(self.check_basic2)
        self.check_apprentice1 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_apprentice1.setFont(font)
        self.check_apprentice1.setText("1º Aprendiz do Evangelho")
        self.check_apprentice1.setObjectName("check_apprentice1")
        self.verticalLayout_4.addWidget(self.check_apprentice1)
        self.check_apprentice2 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_apprentice2.setFont(font)
        self.check_apprentice2.setText("2º Aprendiz do Evangelho")
        self.check_apprentice2.setObjectName("check_apprentice2")
        self.verticalLayout_4.addWidget(self.check_apprentice2)
        self.check_education1 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_education1.setFont(font)
        self.check_education1.setText("1ª Educação Mediúnica")
        self.check_education1.setObjectName("check_education1")
        self.verticalLayout_4.addWidget(self.check_education1)
        self.check_education2 = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_education2.setFont(font)
        self.check_education2.setText("2ª Educação Mediúnica")
        self.check_education2.setObjectName("check_education2")
        self.verticalLayout_4.addWidget(self.check_education2)
        self.check_exposer = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_exposer.setFont(font)
        self.check_exposer.setText("Expositor")
        self.check_exposer.setObjectName("check_exposer")
        self.verticalLayout_4.addWidget(self.check_exposer)
        self.check_philosophy = QtWidgets.QCheckBox(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_philosophy.setFont(font)
        self.check_philosophy.setText("Filosofia")
        self.check_philosophy.setObjectName("check_philosophy")
        self.verticalLayout_4.addWidget(self.check_philosophy)
        self.gridLayout_6.addWidget(self.groupBox_13, 0, 1, 1, 1)
        icon = QtGui.QIcon.fromTheme("arrow-right")
        self.tabWidget.addTab(self.tab_fowarding, icon, "Encaminhamento")
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
        self.groupBox_14.setTitle("1) Sábado 2º, 3º, 4º ou 5º")
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radio_pasteur_a2 = QtWidgets.QRadioButton(self.groupBox_14)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_a2.setFont(font)
        self.radio_pasteur_a2.setText("Pasteur - A2")
        self.radio_pasteur_a2.setObjectName("radio_pasteur_a2")
        self.gridLayout_4.addWidget(self.radio_pasteur_a2, 0, 0, 1, 1)
        self.radio_pasteur_12 = QtWidgets.QRadioButton(self.groupBox_14)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_12.setFont(font)
        self.radio_pasteur_12.setText("Pasteur - 1/2")
        self.radio_pasteur_12.setObjectName("radio_pasteur_12")
        self.gridLayout_4.addWidget(self.radio_pasteur_12, 0, 1, 1, 1)
        self.radio_pasteur_a4 = QtWidgets.QRadioButton(self.groupBox_14)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_a4.setFont(font)
        self.radio_pasteur_a4.setText("Pasteur - A4")
        self.radio_pasteur_a4.setObjectName("radio_pasteur_a4")
        self.gridLayout_4.addWidget(self.radio_pasteur_a4, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_14, 0, 0, 1, 1)
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_guidance)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setTitle("2) Domingo 2º, 3º, 4º ou 5º")
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
        self.radio_pasteur_a3.setText("Pasteur - A3")
        self.radio_pasteur_a3.setObjectName("radio_pasteur_a3")
        self.horizontalLayout_2.addWidget(self.radio_pasteur_a3)
        self.radio_pasteur_3e3m = QtWidgets.QRadioButton(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radio_pasteur_3e3m.setFont(font)
        self.radio_pasteur_3e3m.setText("Pasteur - 3E, 3M")
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
        self.groupBox_16.setTitle("3) Sábado 2º, 3º, 4º ou 5º")
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
        self.radio_pasteur_p3f.setText("Pasteur - P3F  Cura")
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
        self.groupBox_18.setTitle("INFORMAÇÕES NECESSÁRIAS")
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
        self.groupBox_17.setTitle("ORIENTAÇÃO ESPIRITUAL")
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
        self.check_good_thoughts.setText("Ter bons pensamentos")
        self.check_good_thoughts.setObjectName("check_good_thoughts")
        self.verticalLayout_5.addWidget(self.check_good_thoughts)
        self.check_home_gospel = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_home_gospel.setFont(font)
        self.check_home_gospel.setText("Evangelho no lar")
        self.check_home_gospel.setObjectName("check_home_gospel")
        self.verticalLayout_5.addWidget(self.check_home_gospel)
        self.check_readings = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_readings.setFont(font)
        self.check_readings.setText("Leituras edificantes")
        self.check_readings.setObjectName("check_readings")
        self.verticalLayout_5.addWidget(self.check_readings)
        self.check_doctor = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_doctor.setFont(font)
        self.check_doctor.setText("Médico de confiança")
        self.check_doctor.setObjectName("check_doctor")
        self.verticalLayout_5.addWidget(self.check_doctor)
        self.check_care_package = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_care_package.setFont(font)
        self.check_care_package.setText("Cesta básica")
        self.check_care_package.setObjectName("check_care_package")
        self.verticalLayout_5.addWidget(self.check_care_package)
        self.check_no_treatment = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_no_treatment.setFont(font)
        self.check_no_treatment.setText("Não fazer tratamento paralelo")
        self.check_no_treatment.setObjectName("check_no_treatment")
        self.verticalLayout_5.addWidget(self.check_no_treatment)
        self.check_home_sanitation = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_home_sanitation.setFont(font)
        self.check_home_sanitation.setText("Higienização do lar")
        self.check_home_sanitation.setObjectName("check_home_sanitation")
        self.verticalLayout_5.addWidget(self.check_home_sanitation)
        self.check_intimate_makeover = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_intimate_makeover.setFont(font)
        self.check_intimate_makeover.setText("Reforma íntima")
        self.check_intimate_makeover.setObjectName("check_intimate_makeover")
        self.verticalLayout_5.addWidget(self.check_intimate_makeover)
        self.check_study = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_study.setFont(font)
        self.check_study.setText("Estudo da doutrina")
        self.check_study.setObjectName("check_study")
        self.verticalLayout_5.addWidget(self.check_study)
        self.check_frequency = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_frequency.setFont(font)
        self.check_frequency.setText("Frequência na assistência")
        self.check_frequency.setObjectName("check_frequency")
        self.verticalLayout_5.addWidget(self.check_frequency)
        self.check_no_pass = QtWidgets.QCheckBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.check_no_pass.setFont(font)
        self.check_no_pass.setText("Não aplicar passe")
        self.check_no_pass.setObjectName("check_no_pass")
        self.verticalLayout_5.addWidget(self.check_no_pass)
        self.gridLayout_7.addWidget(self.groupBox_17, 0, 1, 4, 1)
        icon = QtGui.QIcon.fromTheme("compass")
        self.tabWidget.addTab(self.tab_guidance, icon, "Colegiado")
        self.tab_interviews = QtWidgets.QWidget()
        self.tab_interviews.setObjectName("tab_interviews")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_interviews)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_interviews)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setTitle("ENTREVISTA")
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_16.setObjectName("gridLayout_16")
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
        self.btn_new_interview.setText("NOVA ENTREVISTA")
        icon = QtGui.QIcon.fromTheme("document-edit")
        self.btn_new_interview.setIcon(icon)
        self.btn_new_interview.setObjectName("btn_new_interview")
        self.gridLayout_16.addWidget(self.btn_new_interview, 3, 0, 1, 2)
        self.label_41 = QtWidgets.QLabel(self.groupBox_11)
        self.label_41.setText("ENTREVISTADOR")
        self.label_41.setObjectName("label_41")
        self.gridLayout_16.addWidget(self.label_41, 0, 0, 1, 1)
        self.txt_interviewer = QtWidgets.QLineEdit(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_interviewer.setFont(font)
        self.txt_interviewer.setText("")
        self.txt_interviewer.setObjectName("txt_interviewer")
        self.gridLayout_16.addWidget(self.txt_interviewer, 0, 1, 1, 3)
        self.btn_save_interview = QtWidgets.QPushButton(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_interview.setFont(font)
        self.btn_save_interview.setText("SALVAR")
        icon = QtGui.QIcon.fromTheme("document-save")
        self.btn_save_interview.setIcon(icon)
        self.btn_save_interview.setObjectName("btn_save_interview")
        self.gridLayout_16.addWidget(self.btn_save_interview, 3, 2, 1, 2)
        self.txt_treatment = QtWidgets.QLineEdit(self.groupBox_11)
        self.txt_treatment.setToolTip("")
        self.txt_treatment.setInputMask("")
        self.txt_treatment.setText("")
        self.txt_treatment.setPlaceholderText("Insira os tratamentos aqui")
        self.txt_treatment.setObjectName("txt_treatment")
        self.gridLayout_16.addWidget(self.txt_treatment, 1, 0, 1, 4)
        self.gridLayout_8.addWidget(self.groupBox_11, 0, 0, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_interviews)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setTitle("ENTREVISTAS ANTERIORES")
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
        icon = QtGui.QIcon.fromTheme("document-edit-sign")
        self.tabWidget.addTab(self.tab_interviews, icon, "Entrevistas")
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
        self.btn_save_interview.clicked.connect(
            self.btn_save_interview_clicked)
        self.tb_interviews.doubleClicked.connect(self.cell_double_clicked)

        self.radio_addiction_yes.clicked.connect(
            self.radio_addictions_yes_toggled)
        self.radio_addiction_no.clicked.connect(
            self.radio_addictions_no_toggled)

        self.get_user()
        self.enable_read_only()

        if assisted_controller.count_assisted() > 0:
            self.txt_index.setMinimum(1)
            self.txt_index.setMaximum(assisted_controller.count_assisted())
            self.txt_index.setValue(assisted_controller.count_assisted())
            self.fill_form()
        else:
            self.empty_form()
            self.disable_navigation()
            self.txt_index.setMaximum(0)
            self.txt_index.setMinimum(0)

        self.action_buttons()

        self.tabWidget.setCurrentIndex(0)
        self.cmb_state.setCurrentIndex(22)
        self.cmb_feeding.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormFicha)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormFicha = QtWidgets.QMainWindow()
    ui = Ui_FormFicha()
    ui.setupUi(FormFicha)
    FormFicha.show()
    sys.exit(app.exec_())
