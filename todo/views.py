from django.shortcuts import render
from .models import Tasks
from django.http import HttpResponseRedirect


def task_list(request):
    tasks = {
        'tasks': Tasks.objects.all()
    }
    return render(request, 'todo/task_list.html', tasks)


def create_task(request):
    new_task = request.POST.get('new_task')
    Tasks.objects.create(task=new_task)

    return HttpResponseRedirect('/todo')


def delete_task(request, id):
    Tasks.objects.get(id=id).delete()

    return HttpResponseRedirect('/todo')