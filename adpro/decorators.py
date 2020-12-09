from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from .models import CustomUser


def unautenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			group = None
			print('>>>>>>>>>>>>>>>>>',request.user.is_admin)
			if request.user.is_superuser == True:
				groupadmin = Group.objects.get(name='superuser')
				groupadmin.user_set.add(request.user)
				return render(request, 'superuser.html')
			if request.user.is_admin == True:
				groupadmin = Group.objects.get(name='admin')
				groupadmin.user_set.add(request.user)
				return render(request, 'admin.html')
			if request.user.is_user == True:
				groupadmin = Group.objects.get(name='user')
				groupadmin.user_set.add(request.user)
				return render(request, 'user.html')
			return view_func(request, *args, **kwargs)
		else:
			return render(request, 'unauthenticated.html')
	return wrapper_func

