__author__ = "Sanjeev Kumar"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019."

from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

from api.model import BaseModel


class UserProfile(BaseModel):

    user = models.OneToOneField(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    phone = models.BigIntegerField(
        unique=True
    )
    address = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    image = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    state = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    pincode = models.CharField(
        max_length=8,
        null=True,
        blank=True
    )

    def __str__(self):
        """."""
        return '%s %s' % (self.user.username, self.user)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'address', 'city', 'state',
                    'updated_timestamp', 'updated_by', 'is_active',
                    'is_deleted')
    list_display_links = ('id',)
    list_filter = ('is_active',)
