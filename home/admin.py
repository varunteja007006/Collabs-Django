from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import Group
from . import models

admin.site.unregister(Group)
admin.site.site_header="Collabs"
admin.site.register(models.feedback_model)
