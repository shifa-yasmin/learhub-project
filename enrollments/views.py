from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.decorators.http import require_POST

from accounts.decorators import group_required
from courses.models import Course
from .models import Enrollment


# 1. Enroll student in a course
@group_required("Student")
@require_POST
def enroll_course(request, course_id):

    course = get_object_or_404(Course, id=course_id)

    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user,
        course=course,
    )

    if created:
        messages.success(request, "Successfully enrolled!")
    else:
        messages.info(request, "Already enrolled!")

    return redirect("courses:course_list")


# 2. Display student's enrolled courses
@group_required("Student")
def my_enrollments(request):

    enrollments = Enrollment.objects.filter(
        student=request.user
    ).select_related("course")

    return render(
        request,
        "enrollments/my_enrollments.html",
        {
            "enrollments": enrollments
        }
    )