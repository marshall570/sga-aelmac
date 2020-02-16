# -*- coding: utf-8 -*-
class User:
    def __init__(self, code = None, name = None, user = None, password = None, category = None, status = None):
        self.code = code
        self.name = name
        self.user = user
        self.password = password
        self.category = category
        self.status = status
        
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, code):
        self._code = code
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, user):
        self._user = user
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password
        
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        self._category = category
        
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        self._status = status
    