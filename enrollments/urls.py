from django.urls import path
from . import views

app_name = "enrollments"

urlpatterns = [
    path(
        "<int:course_id>/enroll/",
        views.enroll_course,
        name="enroll_course"
    ),

    path(
        "my-enrollments/",
        views.my_enrollments,
        name="my_enrollments"
    ),
]