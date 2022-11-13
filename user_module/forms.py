from django.db.models import fields
from django.forms import ModelForm

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import project_model, skill_model, profile_model, user_bookmark_model 

class project_form(ModelForm):
    class Meta:
        model   = project_model
        fields  = ['project_name', 'project_description', 'project_git_link', 'user']
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project_description'].widget.attrs.update({'class': 'materialize-textarea',})

class skill_form(ModelForm):
    class Meta:
        model    = skill_model
        fields   = ['skill_name', 'skill_description', 'skill_link', 'user']
        exclude  = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skill_description'].widget.attrs.update({'class': 'materialize-textarea',})

class profile_form(ModelForm):
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='IN'))

    class Meta:
        model   = profile_model
        fields  = ["user", "email", "profile_pic", "biography", "phone_number", "github", "discord", "college_name", "degree_name", "course_name",
                    "year_of_joining", "ongoing_course_semester"]
        exclude = ["user", "email"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['biography'].widget.attrs.update({'class': 'materialize-textarea',})

class user_bookmark_form(ModelForm):
    class Meta:
        model   = user_bookmark_model
        fields  = ['bookmark_name', 'bookmark_id' , 'bookmark_type', 'user']
        exclude = ['bookmark_name', 'bookmark_id' , 'bookmark_type', 'user']






