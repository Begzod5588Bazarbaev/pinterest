from django.forms import ModelForm
from .models import *
from .models import *
from django.contrib.auth.forms import UserCreationForm

class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = (
            'title',
            'image',
            'detail',
            'category',
            'user',
        )

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('__all__')

class QuoteUserRegistrationForm(UserCreationForm):
    error_messages = 'Пароли не совпадают!'