from .models import TestModel
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = TestModel
