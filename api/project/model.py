
__author__ = "Sanjeev Kumar"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019."

from django.db import models
from django.contrib import admin

from api.model import BaseModel


class Project(BaseModel):

    TASK = 'TK'
    BUG = 'BG'
    EPIC = 'EC'
    STORY = 'SY'

    ISSUE_TYPE = [
        (TASK, 'Task'),
        (BUG, 'Bug'),
        (EPIC, 'Epic'),
        (STORY, 'Story'),
    ]
    issue_type = models.CharField(
        max_length=2,
        choices=ISSUE_TYPE,
        default=STORY,
    )
    name = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False
    )
    summary = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    image = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    description = models.CharField(max_length=150)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'summary', 'description', 'issue_type',
                    'updated_timestamp', 'updated_by', 'is_active',
                    'is_deleted')
    list_display_links = ('id',)
    list_filter = ('is_active',)
