from django.db import models
from django.forms.fields import CharField, ImageField
from django.utils.translation import activate
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from PIL import Image

class project_model(models.Model):
    user = models.CharField(max_length=250)
    project_name        = models.CharField(max_length=250)
    project_description = models.TextField()
    project_git_link    =  models.CharField(max_length=250, blank=True)
    project_date        = models.DateTimeField(default=timezone.localtime)
    def __str__(self):
        return self.project_name

class skill_model(models.Model):
    user = models.CharField(max_length=250)
    skill_name        = models.CharField(max_length=250)
    skill_description = models.TextField()
    skill_link        =  models.CharField(max_length=250, blank=True)
    skill_date        = models.DateTimeField(default=timezone.localtime)
    def __str__(self):
        return self.skill_name

class profile_model(models.Model):
    user     = models.CharField(unique=True, max_length=250)
    email    = models.CharField(unique=True, max_length=250)
    biography       = models.TextField(blank=True)
    phone_number    = PhoneNumberField(blank=True)
    github          = models.CharField(max_length=250, blank=True)
    discord         = models.CharField(max_length=250, blank=True)   

    college_name                = models.CharField(max_length=250, blank=True)
    degree_name                 = models.CharField(max_length=150, blank=True)
    course_name                 = models.CharField(max_length=150, blank=True)
    year_of_joining             = models.CharField(max_length=5, blank=True)
    ongoing_course_semester     = models.CharField(max_length=10, blank=True)
    profile_pic                 = models.ImageField(upload_to='profile_pics', default='default.jpg')
    def __str__(self):
        return self.user
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_pic.path)
        if img.width>300 or img.height>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class user_bookmark_model(models.Model):
    user = models.CharField(max_length=200)
    bookmark_id             = models.IntegerField()
    bookmark_name           = models.CharField(max_length=250)
    Bookmark_Type_Choices   = [ ('Skill','Skill'), ('Project','Project')]
    bookmark_type           = models.CharField(max_length=50,choices=Bookmark_Type_Choices)
    bookmark_date           = models.DateTimeField(default=timezone.localtime)
    def __str__(self):
        return self.bookmark_name