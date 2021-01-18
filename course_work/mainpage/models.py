from django.db import models

class Faculty(models.Model):
    faculty_name = models.CharField("Название факультета", max_length=10, null=True)
    faculty_number = models.IntegerField("Номер факультета", default=0)
    faculty_info = models.CharField("Информация о факультете", max_length=200, null=True)

    def __str__(self):
        return self.faculty_name



class TeachingPlan(models.Model):
    semester_count = models.IntegerField("Количество семестров", default=0)
    disciplines = models.CharField("Тут переделать", max_length=200)
    number = models.CharField("Номер учебного плана", max_length=30, null=True)

    def __str__(self):
        return self.id


class Semester(models.Model):
    TeachingPlan_id = models.CharField("Номер учебного плана", max_length=30, null=True)
    semester_number = models.IntegerField("Номер семестра", default=0)

    def __str__(self):
        return self.semester_number

class Student(models.Model):
    Group_num = models.CharField("Номер группы", max_length=10, default="0000")
    name_surname = models.CharField("ФИО", default="Пупкин Вася Станиславович", max_length=50)
    birthday = models.DateField()
    is_foreigner = models.BooleanField("Является ли иностранцем", null=True)
    is_expelled = models.BooleanField("Является ли отчисленным", null=True)

    def __str__(self):
        return self.name_surname


# Связующая таблица между студентом и семестром
class Subject(models.Model):
    Student_FIO = models.CharField("ФИО", default="Пупкин Вася Станиславович", max_length=50)
    Semester_number = models.IntegerField("Номер семестра", default=0, null=True) # теперь не является внешним ключом
    grade = models.CharField("Оценка", max_length=30, null=True)
    group = models.CharField("Номер группы", max_length=10, default="0000")
    name = models.CharField("Название предмета", max_length=100)
    teacher_name_surname = models.CharField("ФИО лектора", max_length=100)
    def __str__(self):
        return self.name

class Group(models.Model):
    group_number = models.CharField("Номер группы", max_length=10, default="0000")
    teaching_plan = models.CharField("Номер учебного плана", max_length=30, null=True)
    Faculty_FK = models.IntegerField("Номер факультета", default=0)

    def __str__(self):
         return self.group_number

