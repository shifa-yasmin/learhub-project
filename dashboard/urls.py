from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_home, name="dashboard_home"),
    path("admin/",views.admin_dashboard,name="admin_dashboard"),
    path("instructor/",views.instructor_dashboard,name="instructor_dashboard",),
    path("student/", views.student_dashboard,name="student_dashboard",),
]