from django.db import models
from django.utils import timezone

class feedback_model(models.Model):
    name            = models.CharField(max_length=100)
    email           = models.CharField(max_length=200, blank=True)
    feedback        = models.TextField()
    feedback_date   = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return self.name