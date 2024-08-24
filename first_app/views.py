from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import TaskSerializer, SubTaskCreateSerializer, TaskCreateSerializer, TaskDetailSerializer
from django.db.models import Count


#
# @api_view(['POST'])
# def task_create(request):
#     serializer = TaskSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# def task_filter_list(request):
#     status_filter = request.query_params.get('status')
#     deadline_filter = request.query_params.get('deadline')
#
#     tasks = Task.objects.all()
#
#     if status_filter:
#         tasks = tasks.filter(status=status_filter)
#
#     if deadline_filter:
#         tasks = tasks.filter(deadline__lte=deadline_filter)
#
#     paginator = PageNumberPagination()
#     paginator.page_size = 3
#     paginated_tasks = paginator.paginate_queryset(tasks, request)
#
#     serializer = TaskSerializer(paginated_tasks, many=True)
#     return paginator.get_paginated_response(serializer.data)
#
#
@api_view(['GET'])
def task_statistics(request):
    total_tasks = Task.objects.count()
    status_counts = Task.objects.values('status').annotate(count=Count('id'))
    overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()

    data = {'total_tasks': total_tasks, 'status_counts': status_counts, 'overdue_tasks': overdue_tasks}
    return Response(data)


# class SubTaskListCreateView(APIView):
#     def get(self, request):
#         subtasks = SubTask.objects.all()
#         serializer = SubTaskCreateSerializer(subtasks, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = SubTaskCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SubTaskDetailUpdateDeleteView(APIView):
#     def get(self, request, pk):
#         try:
#             subtask = SubTask.objects.get(pk=pk)
#         except SubTask.DoesNotExist:
#             return Response({'error': 'Subtask is not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = SubTaskCreateSerializer(subtask)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         try:
#             subtask = SubTask.objects.get(pk=pk)
#         except SubTask.DoesNotExist:
#             return Response({'error': 'Subtask is not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = SubTaskCreateSerializer(subtask, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         try:
#             subtask = SubTask.objects.get(pk=pk)
#         except SubTask.DoesNotExist:
#             return Response({'error': 'Subtask is not found'}, status=status.HTTP_404_NOT_FOUND)
#         subtask.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class TaskCursorPagination(CursorPagination):
    page_size = 2
    ordering = 'created_at'


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    pagination_class = TaskCursorPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    pagination_class = TaskCursorPagination


class SubTaskCursorPagination(CursorPagination):
    page_size = 2
    ordering = 'created_at'


class SubTaskListCreateAPIView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer
    pagination_class = SubTaskCursorPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']


class SubTaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer







