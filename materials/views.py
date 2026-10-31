from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from accounts.decorators import group_required
from courses.models import Course
from enrollments.models import Enrollment
from .models import LearningMaterial


@group_required("Student")
def course_materials(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course,
    ).exists()

    if not enrolled:
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

    materials = LearningMaterial.objects.filter(course=course)

    return render(
        request,
        "materials/course_materials.html",
        {
            "course": course,
            "materials": materials,
        },
    )