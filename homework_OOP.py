class Student:
    instances = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.__class__.instances.append(self)

    @classmethod
    def get_elements_class(cls):
        return cls.instances

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def student_feedback(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.finished_courses or course in self.courses_in_progress):
            if lecturer.feedback.get(course) is None:
                my_list = [int(grade)]
                lecturer.feedback[course] = my_list
            else:
                my_list = lecturer.feedback[course]
                my_list.append(grade)
                lecturer.feedback[course] = my_list

    def avg(self):
        main_list = []
        for key in self.grades:
            my_list = self.grades[key]
            main_list = main_list + my_list
        summ = 0
        for i in range(len(main_list)):
            num = main_list[i]
            summ = summ + int(num)
        if len(main_list) > 0:
            avg = summ / len(main_list)
            avg = round(avg, 2)
            return avg
        else:
            avg = 0
            return avg

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avg() == other.avg()

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg() < other.avg()

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.avg() != other.avg()

    def __le__(self, other):
        if isinstance(other, Student):
            return self.avg() <= other.avg()

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.avg() >= other.avg()

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.avg() > other.avg()

    def __str__(self):
        courses = ''
        for course in self.courses_in_progress:
            courses = courses + course + ' '
        finish_courses = ''
        for course in self.finished_courses:
            finish_courses = finish_courses + course + ' '
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg()} \nКурсы в процессе изучения:  {courses} \nЗавершенные курсы: {finish_courses}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturers = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.feedback = {}
        self.__class__.lecturers.append(self)

    @classmethod
    def get_elements_class(cls):
        return cls.lecturers

    def __avg__(self):
        main_list = []
        for key in self.feedback:
            my_list = self.feedback[key]
            main_list = main_list + my_list
        summ = 0
        for i in range(len(main_list)):
            num = main_list[i]
            summ = summ + int(num)
        if len(main_list) > 0:
            avg = summ / len(main_list)
            avg = round(avg, 2)
            return avg
        else:
            avg = 0
            return avg

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.__avg__() == other.__avg__()

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.__avg__() < other.__avg__()

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.__avg__() != other.__avg__()

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.__avg__() <= other.__avg__()

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.__avg__() >= other.__avg__()

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.__avg__() > other.__avg__()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__avg__()}\n'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and (
                course in student.courses_in_progress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \n'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

some_Reviewer = Reviewer('Some', 'Buddy')
some_Reviewer.courses_attached += ['Python']
some_Reviewer.rate_hw(best_student, 'Python', 10)
some_Reviewer.rate_hw(best_student, 'Python', 8)
some_Reviewer.rate_hw(best_student, 'Python', 10)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Git']
some_lecturer.courses_attached += ['Python']

best_student.student_feedback(some_lecturer, 'Python', 9)
best_student.student_feedback(some_lecturer, 'Git', 10)

print(some_Reviewer)
print(best_student)
print(some_lecturer)

# Exercise 4
lecturer_1 = Lecturer('Oleg', 'Gezhen')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Vladimir', 'Yazikov')
lecturer_2.courses_attached += ['HTML&CSS']
reviewer_1 = Reviewer('Tora', 'Samisko')
reviewer_1.courses_attached += ['HTML&CSS']
reviewer_2 = Reviewer('Igor', 'Sverchkov')
reviewer_2.courses_attached += ['Python']
student_1 = Student('Ivan', 'Guskov', 'man')
student_1.finished_courses += ['HTML&CSS']
student_1.courses_in_progress += ['Python', 'Git']
student_2 = Student('Dima', 'Vdovin', 'man')
student_2.finished_courses += ['HTML&CSS']
student_2.courses_in_progress += ['Python', 'SQL']

reviewer_1.rate_hw(student_1, 'HTML&CSS', 8)
reviewer_1.rate_hw(student_2, 'HTML&CSS', 10)
student_1.student_feedback(lecturer_2, 'HTML&CSS', 9)
student_2.student_feedback(lecturer_2, 'HTML&CSS', 10)
student_1.student_feedback(lecturer_1, 'Python', 6)
student_2.student_feedback(lecturer_1, 'Python', 5)

print(lecturer_2)
print(lecturer_1)
print(student_1)
print(student_2)

print(student_1 < student_2)
print(lecturer_2 > lecturer_1)


def avg_grade_students(course):
    # I decided to get a list of students from the class
    summ = 0
    count = 0
    for stud in Student.get_elements_class():
        if stud.grades.get(course) is not None:
            list_grade = stud.grades.get(course)
            count = count + len(list_grade)
            summ = summ + sum(list_grade)
        else:
            continue
    avg_grade = summ / count
    avg_grade = round(avg_grade, 2)
    return avg_grade

def avg_grade_lecturer(course):
    # I decided to get a list of lecturers from the class
    count = 0
    summ = 0
    for lect in Lecturer.get_elements_class():
        if lect.feedback.get(course) is not None:
            list_grade = lect.feedback.get(course)
            count = count + len(list_grade)
            summ = summ + sum(list_grade)
        else:
            continue
    avg_grade = summ / count
    avg_grade = round(avg_grade, 2)
    return avg_grade


print(avg_grade_students('HTML&CSS'))
print(avg_grade_lecturer('HTML&CSS'))
