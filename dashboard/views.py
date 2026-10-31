from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from accounts.decorators import group_required


@login_required
def dashboard_home(request):
    user = request.user

    if user.is_superuser or user.groups.filter(name="Admin").exists():
        return redirect("admin_dashboard")

    if user.groups.filter(name="Instructor").exists():
        return redirect("instructor_dashboard")

    if user.groups.filter(name="Student").exists():
        return redirect("student_dashboard")

    raise PermissionDenied


@group_required("Admin")
def admin_dashboard(request):
    return render(request, "dashboard/admin.html")


@group_required("Instructor")
def instructor_dashboard(request):
    return render(request, "dashboard/instructor.html")


@group_required("Student")
def student_dashboard(request):
    return render(request, "dashboard/student.html")