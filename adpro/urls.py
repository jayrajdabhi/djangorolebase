from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user1', views.user1, name='user1'),
    path('post/create', views.PostCreate.as_view(), name= 'createpost'),
]
