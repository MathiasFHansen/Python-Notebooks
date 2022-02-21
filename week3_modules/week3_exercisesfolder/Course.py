

class Course():
    def __init__(self, name, teacher, ETCS, optional_grade):
        self.myname = name
        self.myteacher = teacher
        self.myETCS = ETCS
        self.myoptional_grade = optional_grade

    def generate_courses():
        c1 = Course("Math","Hanne","30","7")
        c2 = Course("English","Beate","40","7")
        c3 = Course("History","Lars","20","7")
        course_lst = [c1,c2,c3]
        return course_lst
