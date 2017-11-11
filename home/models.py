from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
	title = models.CharField(max_length=100)
	category = models.CharField(max_length = 25)
	by = models.CharField(max_length=25)
	description = models.CharField(max_length = 5000)
	pic = models.FileField()
	timestamp = models.DateTimeField( auto_now=False, auto_now_add = True )

	def get_absolute_url(self):
		return reverse('home:detailview',kwargs = {'pk':self.id})

class Comment(models.Model):
	Post = models.ForeignKey(post,on_delete=models.CASCADE,default = 17)
	name = models.TextField(max_length = 100,default= 'shashank')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.FileField()


