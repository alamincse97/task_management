from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import *
from .serializers import *


@api_view(['GET'])
def get_user_tasks(request):
    if request.method == 'GET':
        user = request.user
        tasks = Task.objects.filter(user=user, completed=False).order_by('priority_choice')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return JsonResponse({'message': 'Task deleted successfully.'})