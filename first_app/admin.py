from django.contrib import admin
from first_app.models import *


class SubTaskInline(admin.StackedInline):
    model = SubTask
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'description', 'deadline')
    search_fields = ('title', 'status')
    list_filter = ('title', 'categories')
    ordering = ('title', '-deadline')
    list_per_page = 5
    inlines = [SubTaskInline]


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'deadline', 'created_at')
    search_fields = ('title', 'status')
    list_filter = ('title',)
    ordering = ('title', '-deadline',)
    list_per_page = 5


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('-name',)

