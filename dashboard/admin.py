

# Register your models here.
from django.contrib import admin
from courses.models import Course, Category


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "price", "created_at")
    search_fields = ("title", "description")
    list_filter = ("categories",)


admin.site.register(Category)