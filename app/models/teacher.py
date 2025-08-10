class Teacher:
    def __init__(self, first_name, last_name, teacher_email, dept):
        self.first_name = first_name
        self.last_name = last_name
        self.teacher_email = teacher_email
        self.dept = dept
       

    def to_dict(self):
        return self.__dict__
    
    @property
    def full_name(self):
        return f"{self.last_name}, {self.first_name}"