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

class Group(models.Model):
    group_number = models.CharField("Номер группы", max_length=10, default="0000")
    #teaching_plan = models.IntegerField("Учебный план", default=-1)
    teaching_plan = models.ForeignKey(TeachingPlan, null=True, on_delete=models.SET_NULL)
    Faculty_FK = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.group_number

class Student(models.Model):
    #Group_id = models.IntegerField("Внешний ключ от класса Group", default=0)
    Group_id = models.ForeignKey(Group, null=True, on_delete= models.SET_NULL)
    #photo = models.ImageField("Фотка", width_field=640, height_field=480)
    name_surname = models.CharField("ФИО", default="Пупкин Вася Станиславович", max_length=50)
    birthday = models.CharField("ДР", default="01.01.1800", max_length=15)
    is_foreigner = models.BooleanField("Является ли иностранцем", default=0)
    is_expelled = models.BooleanField("Является ли отчисленным", default=0)

    def __str__(self):
        return self.name_surname

class Semester(models.Model):
    TeachingPlan_id = models.ForeignKey(TeachingPlan, null=True, on_delete=models.SET_NULL)

    semester_number = models.IntegerField("Номер семестра", default=0)
    start_date = models.CharField("Дата начала семестра", default="01.01.1800", max_length=10)
    stop_date = models.CharField("Дата окончания семестра", default="01.01.1800", max_length=10)

    def __str__(self):
        return self.semester_number


class Subject(models.Model):

    name = models.CharField("Название предмета", max_length=100)
    lecturer_name_surname = models.CharField("ФИО лектора", max_length=100)
    practice_name_surname = models.CharField("Фио преподавателя практики", max_length=100)
    grading_method = models.CharField("Метод оценивания", max_length=30, default="Стандартный")

    def __str__(self):
        return self.name


