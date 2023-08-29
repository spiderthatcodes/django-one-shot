from django.shortcuts import render, get_object_or_404
from .models import TodoList


def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {
        'todo_list': todos,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todos = get_object_or_404(TodoList, id=id)
    context = {
        "todos": todos
    }
    return render(request, "todos/detail.html", context)
