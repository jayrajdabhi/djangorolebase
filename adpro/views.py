from django.shortcuts import render
from .decorators import unautenticated_user
from . models import Post
from django.urls import reverse_lazy
from .forms import PostForm
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
	return render(request,'home.html')

@unautenticated_user
def user1(request):
	return render(request,'user1.html')


class PostCreate(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'post_form.html'
	success_url = reverse_lazy('home')
