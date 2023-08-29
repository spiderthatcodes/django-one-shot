from django.urls import path
from .views import todo_list_list


urlpatterns = [
    path("", todo_list_list, name='todo_list_list'),
]
