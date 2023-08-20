from django.contrib import admin
from .models import TaskModel

@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['taskTitle', 'taskDescription', 'is_completed']
