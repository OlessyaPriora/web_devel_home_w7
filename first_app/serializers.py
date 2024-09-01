from rest_framework import serializers
from .models import *
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline']


class SubTaskCreateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, required=False)

    class Meta:
        model = SubTask
        fields = '__all__'
        read_only_fields = ['owner']
        # read_only_fields = ['created_at']


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

    def create(self, validated_data):
        name = validated_data.get('name')
        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("Категория с таким названием уже существует")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get('name')
        if name != instance.name and Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("Категория с таким названием уже существует")
        return super().update(instance, validated_data)


class TaskDetailSerializer(serializers.ModelSerializer):
    sub_tasks = SubTaskCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        exclude = ['created_at']


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['created_at']
        read_only_fields = ['owner']

    def validate_deadline(self, value: str) -> int:
        value = timezone.make_aware(value.replace(tzinfo=None), timezone.get_current_timezone())

        if value < timezone.now():
            raise serializers.ValidationError("Дедлайн не может быть в прошлом")
        return value












