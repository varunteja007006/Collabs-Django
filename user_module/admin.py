from django.contrib import admin
from . import models

admin.site.register(models.profile_model)
admin.site.register(models.project_model)
admin.site.register(models.skill_model)
admin.site.register(models.user_bookmark_model)