from django.shortcuts import render,get_object_or_404
from .models import Task
from .forms import AddTodoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def taskListView(request,template_name="home.html"):
    form = AddTodoForm(request.POST or None)
    if form.is_valid():
        task=form.save(commit=False)
        task.user = request.user
        task.save()
        form = AddTodoForm()
    tasks = Task.objects.filter(user=request.user).order_by("-date")
    context = {"tasks": tasks,"form": form}
    return render(request,template_name,context)

@login_required(login_url='login')
def editTask(request,id,template_name="edit.html"):
    task = get_object_or_404(Task,pk=id)
    form = AddTodoForm(request.POST or None,instance = task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tasks_list'))
    context = {"form": form}
    return render(request,template_name,context)

@login_required(login_url='login')
def deleteTask(request,id):
    task = get_object_or_404(Task,pk=id)
    task.delete()
    return HttpResponseRedirect(reverse("tasks_list"))