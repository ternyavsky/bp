from django.db import models
from django.db.models import BigAutoField, DateTimeField
from django.utils.translation import gettext_lazy as _

# Create your models here.


class BaseModel(models.Model):
    id = BigAutoField(primary_key=True)

    created_at = DateTimeField(_("Дата создания"), auto_now_add=True, blank=True)
    updated_at = DateTimeField(_("Дата изменения"), auto_now=True, blank=True)

    class Meta:
        abstract = True
