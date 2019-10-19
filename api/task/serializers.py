__author__ = "Sanjeev Kumar"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019."

from rest_framework import serializers

from api.task.model import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'created_timestamp')


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'assignee',
            'description',
            'start_date',
            'end_date',
        )
        read_only_fields = ('id', 'pid', 'created_timestamp', 'name')
