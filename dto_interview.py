class Interview:
    def __init__(self, code = None, date = None, interviewer = None, treatment = None, interview = None):
        self.code = code
        self.date = date
        self.interviewer = interviewer
        self.treatment = treatment
        self.interview = interview
        
        
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, code):
        self._code = code


    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        self._date = date
        
        
    @property
    def interviewer(self):
        return self._interviewer
    @interviewer.setter
    def interviewer(self, interviewer):
        self._interviewer = interviewer
        
        
    @property
    def treatment(self):
        return self._treatment
    @treatment.setter
    def treatment(self, treatment):
        self._treatment = treatment
        
        
    @property
    def interview(self):
        return self._interview
    @interview.setter
    def interview(self, interview):
        self._interview = interview
        
