from django.urls import path
from .views import *


urlpatterns = [
    # path('tasks/create/', task_create, name='task-create'),
    # path('tasks/filter/', task_filter_list, name='task_filter_list'),
    path('tasks/statistics/', task_statistics, name='task-statistics'),
    # path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    # path('subtasks/<int:pk>', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-update-or-delete'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-update-delete'),
    path('subtasks/', SubTaskListCreateAPIView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-update-delete'),
]