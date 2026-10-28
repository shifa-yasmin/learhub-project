from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from .forms import RegistationForm

@require_http_methods(["GET","POST"])
def register(request):
    if request.method=="POST":
        form=RegistationForm(request.POST)
    if form.is_valid():
        user=form.save()
        student_group=Group.objects.get(name="Student")
        user.groups.add(student_group)

        login(request,user)
        messages.success(request,"Registration successful")
        return redirect("dashboard_home")
    else:
        form=RegistationForm()
    return render(request,"accounts/register.html",{"form":form})
