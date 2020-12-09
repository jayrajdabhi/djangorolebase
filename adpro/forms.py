from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Post

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = '__all__'

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'