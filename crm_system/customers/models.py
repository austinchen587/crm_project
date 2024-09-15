from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    wechat_id = models.CharField(max_length=100)
    initial_notes = models.TextField()

    last_edited = models.DateTimeField(null=True, blank=True)
    edit_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name