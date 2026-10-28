

# Register your models here.
from django.contrib import admin
from .models import LearningMaterial


@admin.register(LearningMaterial)
class LearningMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "course",
        "material_type",
        "uploaded_at",
    )
    list_filter = ("material_type",)
    search_fields = ("title", "course__title")