from django import forms
from .models import LearningMaterial


class LearningMaterialForm(forms.ModelForm):

    class Meta:
        model = LearningMaterial

        fields = [
            "title",
            "material_type",
            "resource_url",
        ]