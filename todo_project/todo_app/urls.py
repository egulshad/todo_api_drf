from django.urls import path
from . import views
from .views import TaskListCreateView, TaskDetailView, MarkAsCompleted

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', MarkAsCompleted.as_view(), name='task-complete'),
    # path('', views.index, name="index"),
    # path('about/', views.about, name="about"),
    # path('create/', views.create, name="create"),
    # path('delete/<Todos_id>', views.delete, name="delete"),
    # path('yes_finish/<Todos_id>', views.yes_finish, name="yes_finish"),
    # path('no_finish/<Todos_id>', views.no_finish, name="no_finish"),
    # path('update/<Todos_id>', views.update, name="update"),
]