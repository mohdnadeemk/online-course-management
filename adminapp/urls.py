from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.adminhome),
    path('courseentry/',views.courseentry),
    path('courselist1/',views.courselist1),
    path('studentlist/',views.studentlist),
    path("adminlogout/",views.adminlogout),
    path("batchentry/",views.batchentry),
    path("batchlist1/",views.batchlist1),
    path("editcourse/",views.editcourse),
    path('editbatch/',views.edit),
    path('delete_course/<int:courseid>/', views.delete_course, name='delete_course'),
    path('delete_student/<int:sno>/', views.delete_student, name='delete_student'),
]