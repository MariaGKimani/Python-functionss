import datetime
class Student :
    # school ="AkiraChix"
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
    def show_full_name(self):
        return f"Hello your name is {self.first_name} {self.last_name}"
    from datetime import date
    def year_of_birth(self):
        year =  datetime.date.today().year
        return  year -self.age
    def show_intials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}"

    # school= "KU"   ///this is to change the school variable
    def greet_student(self):
        return f"Hello {self.name}, welcome to {self.school}"
    # def year_of_birth(self):
    #     year = 2023 - self.age
    #     return f"helo {self.name},you were born in {year} 
student1 = Student(first_name="Maria",last_name="Kimani",age= 22,country="Kenya")
print(student1.show_full_name())

print(student1.year_of_birth())