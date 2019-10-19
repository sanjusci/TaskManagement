__author__ = "Sanjeev Kumar"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019."

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from api.model import BaseModel
from api.project.model import Project


class Task(BaseModel):

    IN_DEVELOPMENT = 'DT'
    TODO = 'TO'
    IN_REVIEW = 'RW'
    IN_QA = 'QA'
    COMPLETED = 'CD'

    STATUS = [
        (TODO, 'Todo'),
        (IN_DEVELOPMENT, 'Development'),
        (IN_REVIEW, 'Review'),
        (IN_QA, 'Ready for QA'),
        (COMPLETED, 'Done'),
    ]

    assignee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    description = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    pid = models.OneToOneField(
        Project,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=TODO,
    )


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'start_date', 'end_date',
                    'status', 'updated_timestamp', 'updated_by', 'is_active',
                    'is_deleted', 'assignee')
    list_display_links = ('id',)
    list_filter = ('is_active', 'status')
