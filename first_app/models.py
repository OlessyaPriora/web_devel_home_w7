from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return f'Название категории: {self.name}'


class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=100, verbose_name='Название задачи', unique_for_date='created_at')
    description = models.TextField(null=True, blank=True, verbose_name='Описание задачи')
    categories = models.ManyToManyField('Category', related_name='tasks', verbose_name='Категории задачи')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус задачи')
    deadline = models.DateTimeField(verbose_name='Дата и время дедлайн')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f'Название задачи: {self.title}, Категории задачи: {self.categories}'


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=100, verbose_name='Название подзадачи')
    description = models.TextField(null=True, blank=True, verbose_name='Описание подзадачи')
    task = models.ForeignKey('Task', related_name='subtasks', on_delete=models.CASCADE, verbose_name='Основная задача')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус задачи')
    deadline = models.DateTimeField(verbose_name='Дата и время дедлайн')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f'Название подзадачи: {self.title}, Дата и время дедлайн: {self.deadline}'