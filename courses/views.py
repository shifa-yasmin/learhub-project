from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction

from accounts.decorators import group_required
from .models import Course
from .forms import CourseForm, MaterialFormSet


# 1. Display all courses for students
@group_required("Student")
def course_list(request):

    from enrollments.models import Enrollment

    courses = Course.objects.all()

    # Get courses in which the current student is already enrolled
    enrolled_course_ids = set(
        Enrollment.objects.filter(
            student=request.user
        ).values_list("course_id", flat=True)
    )

    return render(
        request,
        "courses/course_list.html",
        {
            "courses": courses,
            "enrolled_course_ids": enrolled_course_ids,
        },
    )


# 2. Display courses created by the logged-in instructor
@group_required("Instructor")
def instructor_courses(request):

    courses = Course.objects.filter(
        instructor=request.user
    )

    return render(
        request,
        "courses/instructor_courses.html",
        {
            "courses": courses,
        },
    )


# 3. Create a course with learning materials
@login_required
@permission_required("courses.add_course", raise_exception=True)
def create_course(request):

    if request.method == "POST":

        course_form = CourseForm(request.POST)
        material_formset = MaterialFormSet(request.POST)

        if course_form.is_valid() and material_formset.is_valid():

            with transaction.atomic():

                # Save course without committing first
                course = course_form.save(commit=False)

                # Assign the logged-in instructor
                course.instructor = request.user

                # Save course
                course.save()

                # Save many-to-many categories
                course_form.save_m2m()

                # Connect learning materials to the course
                material_formset.instance = course

                # Save learning materials
                material_formset.save()

            messages.success(
                request,
                "Course and learning materials created successfully!"
            )

            return redirect("courses:instructor_courses")

        else:
            messages.error(
                request,
                "Please correct the errors in the form."
            )

    else:

        course_form = CourseForm()
        material_formset = MaterialFormSet()

    return render(
        request,
        "courses/course_form.html",
        {
            "form": course_form,
            "formset": material_formset,
        },
    )