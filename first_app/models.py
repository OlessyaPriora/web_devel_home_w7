from django.db import models
from rest_framework.authtoken.admin import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = ('name',)


class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=100, unique=True, verbose_name='Название задачи')#unigue_for_date='created_at'
    description = models.TextField(null=True, blank=True, verbose_name='Описание задачи')
    categories = models.ManyToManyField('Category', related_name='tasks', verbose_name='Категории задачи')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус задачи')
    deadline = models.DateTimeField(verbose_name='Дата и время дедлайн')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = 'Task'
        unique_together = ('title',)


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=100, unique=True, verbose_name='Название подзадачи')
    description = models.TextField(null=True, blank=True, verbose_name='Описание подзадачи')
    task = models.ForeignKey('Task', related_name='subtasks', on_delete=models.CASCADE, verbose_name='Основная задача')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус задачи')
    deadline = models.DateTimeField(verbose_name='Дата и время дедлайн')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subtasks', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'SubTask'
        unique_together = ('title',)



