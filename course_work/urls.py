"""course_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from course_work.mainpage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    # path('Faculty/<str:pk>/', views.FacultyView.as_view()),
    path('Faculty/', views.FacultyView.as_view()),
    path('deleteFaculty/', views.deleteFaculty),
    path('TeachingPlan/', views.TeachingPlanView.as_view()),
    path('deleteTeachingPlan/', views.deleteTeachingPlan),
    path('Group/', views.GroupView.as_view()),
    path('deleteGroup/', views.deleteGroup),
    path('Students/', views.StudentView.as_view()),
    path('expellStudent/', views.expellStudent),
    path('deleteStudent/', views.deleteStudent),
    path('SubjectsOfGroup/<str:pk_group>/', views.SubjectView.as_view()),
    path('SubjectsOfGroup/', views.SubjectView.as_view()),
    path('RateStudent/<str:pk_group>/<str:semester>/<str:subject>/<str:fio>/', views.RateStudent.as_view())





]
