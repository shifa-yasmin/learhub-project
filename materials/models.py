

# Create your models here.
from django.db import models


class LearningMaterial(models.Model):
    class MaterialType(models.TextChoices):
        PDF = "pdf", "PDF"
        VIDEO = "video", "Video"
        LINK = "link", "External Link"

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="materials",
    )
    title = models.CharField(max_length=200)
    material_type = models.CharField(
        max_length=10,
        choices=MaterialType.choices,
    )
    resource_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title