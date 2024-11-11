class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = []
        self.grades = {}

    def takeSubject(self, name):
        self.subjects.append(name) 
        
    def list_subjects(self):
        for subject in self.subjects:
            print(f"Subject: {subject.name}, Difficulty: {subject.difficulty}")
    
    def take_grade(self, subject_name, grade):
        self.grades[subject_name] = grade 

    def list_grades(self):
        for subject, grade in self.grades.items():
            print(f"Subject: {subject} -> Grade: {grade}")

    def ortacha_bahosi(self):      
        umumiy_baho = 0
        baholar_soni = 0
        for i in self.grades.values():
            baholar_soni += 1
            umumiy_baho += i
        print(umumiy_baho / baholar_soni)





class Subject:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty       


math = Subject("math", 10)
history = Subject("history", 8)

ali = Student("Ali", 18)
ali.takeSubject(math)
ali.takeSubject(history)
ali.list_subjects()
ali.take_grade("Math", 5)
ali.take_grade("History", 6)


ali.list_grades()
ali.ortacha_bahosi()