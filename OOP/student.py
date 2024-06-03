class Student:
    school:"AkiraChix"
    def __init__(self,first_name,last_name,age,country,code,school):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.code=code
        self.school=school
    def greet_student(self):
        greet=f"hello {self.first_name} welcome to {self.school}. your code is {self.code}"  
        return greet  
    def greeting(self):
        greetings=f"hello {self.first_name} you were born in the year {2024-self.age}"
        return greetings
    def Student_initials(self):
        initials=f"your initials are {self.first_name[0]}.{self.last_name[0]}"
        return initials
    def display_names(self):
        display=f"{self.first_name} {self.last_name}"
        return display

