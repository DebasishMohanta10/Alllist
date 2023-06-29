from django.urls import path
from . import views
urlpatterns = [
    path("",views.taskListView,name="tasks_list"),
    path("<int:id>/edit/",views.editTask,name="edit_task"),
    path("<int:id>/delete/",views.deleteTask,name="delete_task"),
]
