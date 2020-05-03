# 1. Створіть клас з ім'ям student, що містить поля: прізвище та ініціали, номер групи,
# успішність (масив з п'яти елементів). Створити масив з десяти елементів такого типу,
# впорядкувати записи за зростанням середнього бала.
# Додати можливість виведення прізвищ і номерів груп студентів, які мають оцінки, рівні тільки 4 або 5.

class Student:

    def __init__(self, full_name="", group_number=0, progress=[]):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def __repr__(self):
        return repr(("Student: " + self.full_name + "  Group: " + self.group_number))

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_group_number(self, group_number):
        self.group_number = group_number

    def set_progress(self, progress):
        self.progress = progress

    def get_full_name(self):
        return self.full_name

    def get_group_number(self):
        return self.group_number

    def get_progress(self):
        return self.progress


st_size = 10
students = []
for i in range(st_size):
    st = Student()
    print("Введіть ім'я: ")
    st.full_name = input()
    print("Введіть номер групи: ")
    st.group_number = input()
    print("Введіть 5 оцінок: ")
    st.progress = []
    for i in range(5):
        score = int(input())
        st.progress.append(score)
    students.append(st)


students = sorted(students, key=lambda student: student.full_name)
print("Sorted students:")
for st in students:
    print(st)

print("bad students:")
bad_studs = [stu for stu in students if any(x in stu.progress for x in [0, 1, 2])]

if len(bad_studs) > 0:
    for st in bad_studs:
        print(st)
else:
    print("no matches were found.")