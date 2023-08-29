from django.contrib import admin
from .models import TodoList, TodoItem


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id"
    )


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "due_date",
        "is_completed"
    )
