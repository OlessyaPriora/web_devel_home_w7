from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import TaskSerializer
from django.db.models import Count



def greet(request, name):
    return HttpResponse(f"<h1>Hello, {name}!</h1>")


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def task_filter_list(request):
    status_filter = request.query_params.get('status')
    deadline_filter = request.query_params.get('deadline')

    tasks = Task.objects.all()

    if status_filter:
        tasks = tasks.filter(status=status_filter)

    if deadline_filter:
        tasks = tasks.filter(deadline__lte=deadline_filter)

    paginator = PageNumberPagination()
    paginator.page_size = 3
    paginated_tasks = paginator.paginate_queryset(tasks, request)

    serializer = TaskSerializer(paginated_tasks, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def task_statistics(request):
    total_tasks = Task.objects.count()
    status_counts = Task.objects.values('status').annotate(count=Count('id'))
    overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()

    data = {'total_tasks': total_tasks, 'status_counts': status_counts, 'overdue_tasks': overdue_tasks}
    return Response(data)


