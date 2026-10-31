from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="course_list"),

    path(
        "my-courses/",
        views.instructor_courses,
        name="instructor_courses",
    ),
    path(
        "create/",
        views.create_course,
        name="create_course",
    ),
]