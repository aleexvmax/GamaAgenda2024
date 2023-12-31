from email.policy import default
from time import timezone
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

