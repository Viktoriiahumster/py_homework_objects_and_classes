from itertools import chain

class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.rating = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rating:
                lecturer.rating[course] += [grade]
            else:
                lecturer.rating[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        if not self.grades:
            return 0
        else:
            return sum(list(chain.from_iterable(self.grades.values()))) / len(
                list(chain.from_iterable(self.grades.values())))

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rate()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение невозможно')
            return
        return self.average_rate() > other.average_rate()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Сравнение невозможно')
            return
        return self.average_rate() == other.average_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    rating = {}

    def average_rate(self):
        if not self.rating:
            return 0
        else:
            return sum(list(chain.from_iterable(self.rating.values()))) / len(
            list(chain.from_iterable(self.rating.values())))

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение невозможно')
            return
        return self.average_rate() > other.average_rate()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение невозможно')
            return
        return self.average_rate() == other.average_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.rating[course] = sum(list(chain.from_iterable(student.grades.values()))) / len(list(chain.from_iterable(student.grades.values())))
            else:
                student.grades[course] = [grade]
                student.rating[course] = sum(list(chain.from_iterable(student.grades.values()))) / len(list(chain.from_iterable(student.grades.values())))
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



best_lecturer_1 = Lecturer('Ivan', 'Ivanov')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Nikolay', 'Smirnov')
best_lecturer_2.courses_attached += ['Python']

cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Noman', 'Sky')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

student_1 = Student('Denis', 'Sviridov', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ['C++']

student_2 = Student('Petya', 'Petrov', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['C++']

student_1.rate_lecturer(best_lecturer_1, 'Python', 10)
student_1.rate_lecturer(best_lecturer_1, 'Python', 4)
student_1.rate_lecturer(best_lecturer_1, 'Python', 10)

student_1.rate_lecturer(best_lecturer_2, 'Python', 8)
student_2.rate_lecturer(best_lecturer_2, 'Python', 2)

cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 10)

cool_reviewer_1.rate_hw(student_2, 'Python', 3)
cool_reviewer_1.rate_hw(student_2, 'Python', 1)
cool_reviewer_1.rate_hw(student_2, 'Python', 2)

print(student_1.grades)
print()
print(Lecturer.average_rate(best_lecturer_1))
print()
print(Reviewer.__str__(cool_reviewer_1))
print()
print(Lecturer.__str__(best_lecturer_1))
print()
print(Student.__str__(student_1))
print()
print(Student.__eq__(student_1, student_2))
print(Student.__lt__(student_1, student_2))
print()
print(Lecturer.__lt__(best_lecturer_1, best_lecturer_2))
print(Lecturer.__eq__(best_lecturer_1, best_lecturer_2))
print()


def student_average_rate(student_list, course):
    sum_rating = 0
    for student in student_list:
        if isinstance(student, Student) and course in student.courses_in_progress:
            sum_rating += student.average_rate()
    return sum_rating / len(student_list)

student_list = [student_1, student_2]

def lecturer_average_rate(lecturer_list, course):
    sum_rating = 0
    for lector in lecturer_list:
        if isinstance(lector, Lecturer) and course in lector.courses_attached:
            sum_rating += lector.average_rate()
    return sum_rating / len(lecturer_list)

lecturer_list = [best_lecturer_1, best_lecturer_2]


print(student_average_rate(student_list, 'Python'))
print(lecturer_average_rate(lecturer_list, 'Python'))