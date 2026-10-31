from django import forms
from django.forms import inlineformset_factory

from .models import Course
from materials.models import LearningMaterial
from materials.forms import LearningMaterialForm


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course

        fields = [
            "title",
            "description",
            "categories",
            "price",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Enter course title"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Enter course description"}
            ),
            "price": forms.NumberInput(
                attrs={"placeholder": "Enter course price"}
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]

        if len(title.strip()) < 5:
            raise forms.ValidationError(
                "Course title must contain at least 5 characters."
            )

        return title.strip()

    def clean_description(self):
        description = self.cleaned_data["description"]

        if len(description.strip()) < 20:
            raise forms.ValidationError(
                "Description must contain at least 20 characters."
            )

        return description.strip()

    def clean_price(self):
        price = self.cleaned_data["price"]

        if price < 0:
            raise forms.ValidationError(
                "Course price cannot be negative."
            )

        return price


# Create formset outside the CourseForm class
MaterialFormSet = inlineformset_factory(
    Course,
    LearningMaterial,
    form=LearningMaterialForm,
    extra=3,
    can_delete=True
)