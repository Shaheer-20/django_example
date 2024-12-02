from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/index.html', {'tasks': tasks})


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'myapp/create.html')  # No 'task' passed here


def update(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('index')
    return render(request, 'myapp/update.html', {'task': task})

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('index')
