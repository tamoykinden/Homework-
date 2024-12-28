class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.course_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.course_attached = []
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.course_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Создаем студентов
student1 = Student('Денис', 'Тамойкин', 'М')
student1.courses_in_progress.append('Python')

# Создаем лекторов
lecturer1 = Lecturer('Петр', 'Петров')
lecturer1.course_attached.append('Python')

# Создаем проверяющих
reviewer1 = Reviewer('Сидор', 'Сидоров')
reviewer1.course_attached.append('Python')

# Проверяющий выставляет оценку студенту
reviewer1.rate_hw(student1, 'Python', 9)

# Студент выставляет оценку лектору
student1.rate_lecturer(lecturer1, 'Python', 10)

# Выводим оценки
print(student1.grades)  # {'Python': [9]}
print(lecturer1.grades)  # {'Python': [10]}