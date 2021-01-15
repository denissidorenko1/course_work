from django.shortcuts import render, redirect
from course_work import settings
from course_work.mainpage.models import *
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView



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
        print(number)
        info = request.POST.get('faculty_info')
        instance = Faculty.objects.create(faculty_name=name, faculty_number=number, faculty_info=info)
        instance.save()
        faculty = Faculty.objects.all()
        context = {"faculty": faculty}
        return render(request, 'createFaculty.html', context)


def deleteFaculty(request):
    if request.method == "POST":
        Fac = Faculty.objects.filter(faculty_number=request.POST.get("delete_faculty_by_number")).order_by('faculty_number').first()
        Fac.delete()
        print("trying to delete faculty")
        # faculty = Faculty.objects.all()
        # context = {"faculty": faculty}
        return redirect("http://127.0.0.1:8000/Faculty/")


class TeachingPlanView(APIView):
    def get(self, request):
        teaching_plan = TeachingPlan.objects.all()
        context = {"teaching_plan": teaching_plan}
        return render(request, 'TeachingPlan.html', context)

    def post(self,request):
        number = request.POST.get('teaching_plan_number')
        disciplines = request.POST.get('teaching_plan_disciplines')
        semester_count = request.POST.get('teaching_plan_semester_count')
        instance = TeachingPlan.objects.create(semester_count=semester_count, disciplines=disciplines, number=number)
        instance.save()
        teaching_plan = TeachingPlan.objects.all()
        context = {"teaching_plan": teaching_plan}
        return render(request, 'TeachingPlan.html', context)


def deleteTeachingPlan(request):
    if request.method == "POST":
        plan = TeachingPlan.objects.filter(number=request.POST.get("delete_teaching_plan_by_number")).order_by('number').first()
        plan.delete()
        print("trying to delete faculty")
        # faculty = Faculty.objects.all()
        # context = {"faculty": faculty}
        return redirect("http://127.0.0.1:8000/TeachingPlan/")