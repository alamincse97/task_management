from django.urls import path,include


urlpatterns = [
    path('api/user_tasks/', get_user_tasks, name='get_user_tasks'),
    path('api/delete_task/<int:task_id>/', delete_task, name='delete_task'),
    
]