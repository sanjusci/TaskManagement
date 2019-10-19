"""TaskManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.utils.translation import ugettext_lazy
from django.views.decorators.csrf import csrf_exempt

# Django Admin Text
from TaskManagement import settings
from api.project.view import ProjectList, ProjectDetails
from api.task.view import TaskList, TaskDetails
from api.user.view import Login, Home, Users, Logout
from rest_framework import routers

admin.autodiscover()
admin.site.site_header = ugettext_lazy('Task Management Administration')
admin.site.site_title = ugettext_lazy('Task management site admin')
router = routers.DefaultRouter()


def add_prefix(entity_url):
    """
    Function add_prefix
    This function is used to add prefix in the url.

    :param entity_url:
      An entity_url that contains entity url
    :param flag:
      A flag that contains boolean value, default is True.

    :return:
      Return url tuple.
    """
    return "{}{}".format(settings.URLS_PREFIX, entity_url)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', csrf_exempt(Home.as_view())),
    path(add_prefix('users/'), csrf_exempt(Users.as_view())),
    path(add_prefix('login/'), csrf_exempt(Login.as_view())),
    path(add_prefix('/logout/'), csrf_exempt(Logout.as_view())),
    path(add_prefix('projects/'), csrf_exempt(ProjectList.as_view())),
    path(add_prefix('project/<int:pk>/'), csrf_exempt(
        ProjectDetails.as_view())),
    path(add_prefix('project/<int:pid>/tasks/'), csrf_exempt(
        TaskList.as_view())),
    path(add_prefix('project/<int:pid>/task/<int:tk>/'), csrf_exempt(
        TaskDetails.as_view())),
]
