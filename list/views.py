from django.shortcuts import render, redirect

from list.forms import TaskForm
from list.models import Task


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    ctx = {
        'tasks': Task.objects.all(),
        'form': TaskForm()
    }

    return render(request, 'list/index.html', ctx)


def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('index')

