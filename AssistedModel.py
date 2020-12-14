# -*- coding: utf-8 -*-
class AssistedModel:
    def __init__(self, serial=None, position=None, register_date=None, name=None, date_of_birth=None, phone=None,
                 gender=None, civil_state=None, ocupation=None, lives_with=None, zip_code=None, address=None,
                 neighbourhood=None, number=None, city=None, state=None, sedatives=None, medical_treatment=None,
                 sleep_well=None, addictions=None, dreams=None, work=None, family=None, feeding=None, traits=None,
                 latest_treatment=None, courses=None, fowarding=None, treatment=None, guidance=None):
        self.serial = serial
        self.position = position
        self.register_date = register_date
        self.name = name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.gender = gender
        self.civil_state = civil_state
        self.ocupation = ocupation
        self.lives_with = lives_with
        self.zip_code = zip_code
        self.address = address
        self.neighbourhood = neighbourhood
        self.number = number
        self.city = city
        self.state = state
        self.sedatives = sedatives
        self.medical_treatment = medical_treatment
        self.sleep_well = sleep_well
        self.addictions = addictions
        self.dreams = dreams
        self.work = work
        self.family = family
        self.feeding = feeding
        self.traits = traits
        self.latest_treatment = latest_treatment
        self.courses = courses
        self.fowarding = fowarding
        self.treatment = treatment
        self.guidance = guidance

    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, serial):
        self._serial = serial

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, register_date):
        self._register_date = register_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def civil_state(self):
        return self._civil_state

    @civil_state.setter
    def civil_state(self, civil_state):
        self._civil_state = civil_state

    @property
    def ocupation(self):
        return self._ocupation

    @ocupation.setter
    def ocupation(self, ocupation):
        self._ocupation = ocupation

    @property
    def lives_with(self):
        return self._lives_with

    @lives_with.setter
    def lives_with(self, lives_with):
        self._lives_with = lives_with

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        self._zip_code = zip_code

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def neighbourhood(self):
        return self._neighbourhood

    @neighbourhood.setter
    def neighbourhood(self, neighbourhood):
        self._neighbourhood = neighbourhood

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def sedatives(self):
        return self._sedatives

    @sedatives.setter
    def sedatives(self, sedatives):
        self._sedatives = sedatives

    @property
    def medical_treatment(self):
        return self._medical_treatment

    @medical_treatment.setter
    def medical_treatment(self, medical_treatment):
        self._medical_treatment = medical_treatment

    @property
    def sleep_well(self):
        return self._sleep_well

    @sleep_well.setter
    def sleep_well(self, sleep_well):
        self._sleep_well = sleep_well

    @property
    def addictions(self):
        return self._addictions

    @addictions.setter
    def addictions(self, addictions):
        self._addictions = addictions

    @property
    def dreams(self):
        return self._dreams

    @dreams.setter
    def dreams(self, dreams):
        self._dreams = dreams

    @property
    def work(self):
        return self._work

    @work.setter
    def work(self, work):
        self._work = work

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = family

    @property
    def feeding(self):
        return self._feeding

    @feeding.setter
    def feeding(self, feeding):
        self._feeding = feeding

    @property
    def traits(self):
        return self._traits

    @traits.setter
    def traits(self, traits):
        self._traits = traits

    @property
    def latest_treatment(self):
        return self._latest_treatment

    @traits.setter
    def latest_treatment(self, latest_treatment):
        self._latest_treatment = latest_treatment

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, courses):
        self._courses = courses

    @property
    def fowarding(self):
        return self._fowarding

    @fowarding.setter
    def fowarding(self, fowarding):
        self._fowarding = fowarding

    @property
    def treatment(self):
        return self._treatment

    @treatment.setter
    def treatment(self, treatment):
        self._treatment = treatment

    @property
    def guidance(self):
        return self._guidance

    @guidance.setter
    def guidance(self, guidance):
        self._guidance = guidance
