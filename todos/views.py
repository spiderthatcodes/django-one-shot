from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList
from .forms import TodoForm


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


def todo_list_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list_list')
    else:
        form = TodoForm()

    context = {
        "form": form,
    }

    return render(request, "todos/create.html", context)


def todo_list_update(request, id):
    list = TodoList.objects.get(id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id)

    else:
        form = TodoForm()
        context = {
            'form': form,
            'list': list
        }

        return render(request, 'todos/edit.html', context)


def todo_list_delete(request, id):
    list = TodoList.objects.get(id=id)
    if request.method == "POST":
        list.delete()
        return redirect('todo_list_list')

    context = {
        "list": list,
    }

    return render(request, 'todos/delete.html', context)
