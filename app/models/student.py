class Student:
    def __init__(self,laid, first_name, last_name, dob, student_email, student_grad_year, parent_first_name, parent_last_name, parent_email, most_recent_504_evaluation, entry_to_504_program, upcoming_meeting_date, upcoming_meeting_time, date_of_most_recent_documentation_from_qual_prof,  name_and_title_of_qual_prof,diagnosis, accommodations, courses, teachers, upcoming_meetings_attendees, status504):
        self.laid = laid
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.student_email = student_email
        self.student_grad_year = student_grad_year
        self.parent_first_name = parent_first_name
        self.parent_last_name = parent_last_name
        self.parent_email = parent_email
        self.most_recent_504_evaluation = most_recent_504_evaluation
        self.entry_to_504_program = entry_to_504_program
        self.upcoming_meeting_date = upcoming_meeting_date
        self.upcoming_meeting_time = upcoming_meeting_time
        self.date_of_most_recent_documentation_from_qual_prof = date_of_most_recent_documentation_from_qual_prof
        self.name_and_title_of_qual_prof = name_and_title_of_qual_prof
        self.diagnosis = diagnosis
        self.accommodations = accommodations
        self.course = courses
        self.teachers = teachers
        self.upcoming_meeting_attendees = upcoming_meetings_attendees
        self.status504 = status504

    def to_dict(self):
        return self.__dict__