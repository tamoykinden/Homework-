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
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values()) if self.grades else 0
        return (super().__str__() + f"\nСредняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __eq__(self, other):
        return self._avg_grade() == other._avg_grade() if isinstance(other, Student) else NotImplemented

    def __lt__(self, other):
        return self._avg_grade() < other._avg_grade() if isinstance(other, Student) else NotImplemented

    def _avg_grade(self):
        return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values()) if self.grades else 0


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
        avg_grade = sum(sum(grades) for grades in self.lecture_grades.values()) / sum(len(grades) for grades in self.lecture_grades.values()) if self.lecture_grades else 0
        return super().__str__() + f"\nСредняя оценка за лекции: {avg_grade:.1f}"

    def __eq__(self, other):
        return self._avg_grade() == other._avg_grade() if isinstance(other, Lecturer) else NotImplemented

    def __lt__(self, other):
        return self._avg_grade() < other._avg_grade() if isinstance(other, Lecturer) else NotImplemented

    def _avg_grade(self):
        return sum(sum(grades) for grades in self.lecture_grades.values()) / sum(len(grades) for grades in self.lecture_grades.values()) if self.lecture_grades else 0


class Reviewer(Mentor):
    pass