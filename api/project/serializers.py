__author__ = "Sanjeev Kumar"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019."

from rest_framework import serializers

from api.project.model import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for project."""

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id', 'created_timestamp')


class UpdateProjectSerializer(serializers.ModelSerializer):
    """Serializer for project."""

    class Meta:
        model = Project
        fields = (
            'issue_type',
            'summary',
            'description',
            'updated_timestamp',
        )
        read_only_fields = ('id', 'created_timestamp', 'name')
