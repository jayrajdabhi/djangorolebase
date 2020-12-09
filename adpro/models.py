from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
# Create your models here.
class CustomUser(AbstractUser):
	is_superuser = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_user = models.BooleanField(default=True)



class Post(models.Model):
	name = models.CharField(max_length=256)
	content = models.TextField()

	def __str__(self):
		return self.name