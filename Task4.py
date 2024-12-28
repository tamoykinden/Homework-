class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        avg_grade = self._avg_grade()
        return (super().__str__() + f"\nСредняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def _avg_grade(self):
        if not self.grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._avg_grade() == other._avg_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._avg_grade() < other._avg_grade()


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def __str__(self):
        avg_grade = self._avg_grade()
        return super().__str__() + f"\nСредняя оценка за лекции: {avg_grade:.1f}"

    def _avg_grade(self):
        if not self.lecture_grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.lecture_grades.values())
        total_count = sum(len(grades) for grades in self.lecture_grades.values())
        return total_grades / total_count

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._avg_grade() == other._avg_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._avg_grade() < other._avg_grade()


class Reviewer(Mentor):
    pass


# Функция для подсчета средней оценки за домашние задания по курсу
def avg_hw_grade(students, course):
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_grades / total_count if total_count > 0 else 0


# Функция для подсчета средней оценки за лекции по курсу
def avg_lecture_grade(lecturers, course):
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.lecture_grades:
            total_grades += sum(lecturer.lecture_grades[course])
            total_count += len(lecturer.lecture_grades[course])
    return total_grades / total_count if total_count > 0 else 0


# Создаем экземпляры классов
student1 = Student("Ruoy", "Eman", "male")
student1.courses_in_progress = ["Python", "Git"]
student1.finished_courses = ["Введение в программирование"]
student1.grades = {"Python": [9, 10, 8], "Git": [7, 8, 9]}

student2 = Student("Alice", "Smith", "female")
student2.courses_in_progress = ["Python", "Git"]
student2.grades = {"Python": [7, 8, 9], "Git": [6, 7, 8]}

lecturer1 = Lecturer("Some", "Buddy")
lecturer1.lecture_grades = {"Python": [10, 9, 10], "Git": [8, 9, 10]}

lecturer2 = Lecturer("Jane", "Doe")
lecturer2.lecture_grades = {"Python": [7, 8, 9], "Git": [6, 7, 8]}

reviewer1 = Reviewer("John", "Doe")
reviewer1.courses_attached = ["Python"]

reviewer2 = Reviewer("Emily", "Smith")
reviewer2.courses_attached = ["Git"]

# Вызываем методы
reviewer1.rate_hw(student1, "Python", 10)
reviewer2.rate_hw(student1, "Git", 8)

# Выводим информацию
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Сравниваем студентов и лекторов
print(student1 > student2)  # True
print(lecturer1 > lecturer2)  # True

# Вызываем функции для подсчета средней оценки
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка за домашние задания по курсу Python: {avg_hw_grade(students, 'Python'):.1f}")
print(f"Средняя оценка за лекции по курсу Python: {avg_lecture_grade(lecturers, 'Python'):.1f}")