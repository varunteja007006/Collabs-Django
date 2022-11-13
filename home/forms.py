from django.db.models import fields
from django.forms import ModelForm
from . models import feedback_model

class feedback_form(ModelForm):
    class Meta:
        model = feedback_model
        fields = ['name', 'email', 'feedback']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['feedback'].widget.attrs.update({'class': 'materialize-textarea',})