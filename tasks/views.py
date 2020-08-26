from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class TaskForm(forms.Form):
    task = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Add new task..'}))

tasks = ["foo", "sd" ,"helo"]


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("tasks:index"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, "tasks/add.html", {
        "form" : form
    })