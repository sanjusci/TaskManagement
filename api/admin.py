from django.contrib import admin
from api.user.model import UserProfile, ProfileAdmin
from api.project.model import Project, ProjectAdmin
from api.task.model import Task, TaskAdmin

# Register your models here.

admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
