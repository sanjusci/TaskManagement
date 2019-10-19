from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):

    created_timestamp = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False
    )
    updated_timestamp = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_requests_created"
    )
    updated_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_requests_updated"
    )
    # Entry will never be deleted its is_deleted status will be updated
    is_deleted = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        abstract = True
