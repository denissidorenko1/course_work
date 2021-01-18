from django.shortcuts import render, redirect
from course_work import settings
from course_work.mainpage.models import *
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponseRedirect, HttpResponse


def first_page(request):
    return render(request, 'first_page.html')


class FacultyView(APIView):
    def get(self, request):
        faculty = Faculty.objects.all()
        context = {"faculty": faculty}
        return render(request, 'createFaculty.html', context)

    def post(self,request):
        number = request.POST.get('faculty_number')
        name = request.POST.get('faculty_name')
        info = request.POST.get('faculty_info')
        try:
            get_by_number = Faculty.objects.get(faculty_number=number)
        except Faculty.DoesNotExist:
            instance = Faculty.objects.create(faculty_name=name, faculty_number=number, faculty_info=info)
            instance.save()
            faculty = Faculty.objects.all()
            context = {"faculty": faculty}
            return render(request, 'createFaculty.html', context)
        else:
            return HttpResponse("Такой факультет уже существует. Нельзя добавлять факультеты с одинаковым номером")


def deleteFaculty(request):
    if request.method == "POST":
        delete_number = request.POST.get("delete_faculty_by_number")
        try:
            plan = Faculty.objects.get(faculty_number=delete_number)
        except AttributeError:
            return HttpResponse("Нет факультета с указанным номером ")
        except Faculty.DoesNotExist:
            return HttpResponse("Нет факультета с указанным номером ")
        try:
            group = Group.objects.get(Faculty_FK=delete_number)
        except Group.DoesNotExist:
            plan.delete()
            return redirect("http://127.0.0.1:8000/Faculty/")
        except Group.MultipleObjectsReturned:
            used_by_group = "Несколько групп обучаются на данном факультете, удаление невозможно"
            return HttpResponse(used_by_group)
        else:
            used_by_group = str("Группа №"+str(group)+" обучается на данном факультете, удаление невозможно")
            return HttpResponse(used_by_group)
    # if request.method == "POST":
    #     Fac = Faculty.objects.filter(faculty_number=request.POST.get("delete_faculty_by_number")).order_by('faculty_number').first()
    #     Fac.delete()
    #     print("trying to delete faculty")
        # return redirect("http://127.0.0.1:8000/Faculty/")


class TeachingPlanView(APIView):
    def get(self, request):
        teaching_plan = TeachingPlan.objects.all()
        context = {"teaching_plan": teaching_plan}
        return render(request, 'TeachingPlan.html', context)

    def post(self,request):
        number = request.POST.get('teaching_plan_number')
        disciplines = request.POST.get('teaching_plan_disciplines')
        semester_count = request.POST.get('teaching_plan_semester_count')
        try:
            get_by_number = TeachingPlan.objects.get(number=number)
        except TeachingPlan.DoesNotExist:
            instance = TeachingPlan.objects.create(semester_count=semester_count, disciplines=disciplines, number=number)
            instance.save()
            teaching_plan = TeachingPlan.objects.all()
            context = {"teaching_plan": teaching_plan}
            return render(request, 'TeachingPlan.html', context)
        else:
            return HttpResponse("Учебный план с таким номером уже существует. Невозможно добавление нового учебного плана с таким номером")


# ! добавить блокировку удаления учебного плана, добавить возможность изменения учебного плана
def deleteTeachingPlan(request):
    if request.method == "POST":
        delete_number = request.POST.get("delete_teaching_plan_by_number")
        try:
            plan = TeachingPlan.objects.get(number=delete_number)
        except AttributeError:
            return HttpResponse("Нет учебного плана с указанным номером ")
        except TeachingPlan.DoesNotExist:
            return HttpResponse("Нет учебного плана с указанным номером ")
        try:
            group = Group.objects.get(teaching_plan=delete_number)
        except Group.DoesNotExist:
            plan.delete()
            return redirect("http://127.0.0.1:8000/TeachingPlan/")
        except Group.MultipleObjectsReturned:
            used_by_group = str("Данный план используется у нескольких групп, удаление невозможно")
            return HttpResponse(used_by_group)
        else:
            used_by_group = str("Данный план используется у группы №"+str(group)+" , удаление невозможно")
            return HttpResponse(used_by_group)



# Класс, ответственный за обработку запросов на добавление/удаление учебных групп
class GroupView(APIView):
    def get(self, request):
        group = Group.objects.all()
        context = {"group": group}
        return render(request, 'Group.html', context)

    def post(self,request):
        group_number = request.POST.get('group_number')
        teaching_plan_fk = request.POST.get('teaching_plan')
        faculty_fk = request.POST.get('Faculty_FK')

        try:
            plan_exists = TeachingPlan.objects.get(number=teaching_plan_fk)
        except TeachingPlan.DoesNotExist:
            print("Teaching plan does not exist")
            return HttpResponse("Учебного плана с таким названием не существует. Выберите корректный учебный план")

        try:
            faculty_exists = Faculty.objects.get(faculty_number=faculty_fk)
        except Faculty.DoesNotExist:
            print("Faculty does not exist")
            return HttpResponse("Факультета с таким названием не существует. Выберите корректный номер факультета")

        try:
            get_by_number = Group.objects.get(group_number=group_number)
        except Group.DoesNotExist:
            instance = Group.objects.create(group_number=group_number, teaching_plan=teaching_plan_fk, Faculty_FK=faculty_fk)
            instance.save()
            group = Group.objects.all()
            context = {"group": group}
            return render(request, 'Group.html', context)
        else:
            return HttpResponse("Группа с таким номером уже существует. Невозможно добавление новой группы с таким номером")

def deleteGroup(request):
    if request.method == "POST":
        plan = Group.objects.filter(group_number=request.POST.get("delete_group_by_number")).order_by('group_number').first()
        plan.delete()
        return redirect("http://127.0.0.1:8000/Group/")



# Студент
class StudentView(APIView):
    def get(self, request):
        student = Student.objects.all()
        context = {"student": student}
        return render(request, 'Student.html', context)

    def post(self,request):
        group = request.POST.get('Group_num')
        fio = request.POST.get('name_surname')
        birthday = request.POST.get('birthday')
        is_foreigner = bool(request.POST.get('is_foreigner'))
        is_expelled = False

        try:
            get_by_number = Student.objects.get(name_surname=fio)
        except Student.DoesNotExist:
            instance = Student.objects.create(Group_num=group, name_surname=fio, birthday=birthday,
                                              is_foreigner=is_foreigner, is_expelled=is_expelled)
            instance.save()
            student = Student.objects.all()
            context = {"student": student}
            return render(request, 'Student.html', context)
        else:
            return HttpResponse("Студент с таким ФИО уже существует. Добавление запрещено")


def deleteStudent(request):
    pass
    # if request.method == "POST":
    #     delete_student = request.POST.get("delete_teaching_plan_by_number")
    #     try:
    #         plan = TeachingPlan.objects.get(number=delete_number)
    #     except AttributeError:
    #         return HttpResponse("Нет учебного плана с указанным номером ")
    #     except TeachingPlan.DoesNotExist:
    #         return HttpResponse("Нет учебного плана с указанным номером ")
    #     try:
    #         group = Group.objects.get(teaching_plan=delete_number)
    #     except Group.DoesNotExist:
    #         plan.delete()
    #         return redirect("http://127.0.0.1:8000/TeachingPlan/")
    #     except Group.MultipleObjectsReturned:
    #         used_by_group = str("Данный план используется у нескольких групп, удаление невозможно")
    #         return HttpResponse(used_by_group)
    #     else:
    #         used_by_group = str("Данный план используется у группы №"+str(group)+" , удаление невозможно")
    #         return HttpResponse(used_by_group)


def expellStudent(request):
    if request.method == "POST":
        fio = request.POST.get("expell_student_by_name_surname")
        print(fio)
        try:
            student_instance = Student.objects.get(name_surname__istartswith=fio)
        except Student.DoesNotExist:
            return HttpResponse("Студента не существует. Отчислить несуществующего студента невозможно")
        else:
            student_instance.is_expelled = True
            student_instance.save()
            return redirect("http://127.0.0.1:8000/Students/")


class SubjectView(APIView):
    def get(self, request, pk_group):
        if request.method == "GET":
            try:
                subjects = Subject.objects.filter(group__startswith=pk_group)
            except Subject.DoesNotExist:
                return HttpResponse("Такой предмет не существует")
                #return render(request, 'Subject.html')
            else:

                context = {"subjects": subjects}
                return render(request, 'Subject.html', context)

    def post(self,request, pk_group):
        #group = request.POST.get("group")
        group = pk_group
        semester_number = request.POST.get("Semester_number")
        grade = "Незачет"
        name = request.POST.get("name")
        teacher_name_surname = request.POST.get("teacher_name_surname")
        print(group)
        #Добавить защиту от DoesNotExist
        #try:
        try:
            students_count = Student.objects.filter(Group_num=group)
        except Student.DoesNotExist:
            return HttpResponse("Такой группы не существует. А должна существовать. Если вы видете это сообщение, то дело плохо")
        #except Student.MultipleObjectsReturned:
        print(students_count)
        AllOK = False
        try:
            check_for_repeation = Subject.objects.get(group=group, name=name, Semester_number=semester_number)
            print(check_for_repeation)
        except Subject.DoesNotExist:
            AllOK = True
        except Subject.MultipleObjectsReturned:
            AllOK = False
        if AllOK:
            for stud in students_count:
                print(stud)
                instance = Subject.objects.create(Student_FIO=str(stud), Semester_number=semester_number,
                    grade=grade, group=group, name=name, teacher_name_surname=teacher_name_surname)
                instance.save()
        else:
            return HttpResponse("Похоже, вы пытаетесь добавить повторяющийся предмет")
        try:
            subjects = Subject.objects.filter(group__startswith=pk_group)
        except Subject.DoesNotExist:
            return HttpResponse("Такой предмет не существует")
            #return render(request, 'Subject.html')
        else:

            context = {"subjects": subjects}
            return render(request, 'Subject.html', context)
        #return HttpResponse("Success")


class RateStudent(APIView):
    def get(self, request, pk_group, semester, subject, fio):
        try:
            subjects = Subject.objects.filter(Student_FIO=fio, group=pk_group, Semester_number=semester, name=subject)
        except Subject.DoesNotExist:
            print("Не существует")
        else:
            context = {"subjects": subjects}
            return render(request, "SubjectOfStudent.html", context)

    def post(self, request, pk_group, semester, subject, fio):
        pass