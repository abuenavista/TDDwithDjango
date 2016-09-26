from django.db import models

# Create your models here.
class Item(models.Model):		#I am inheriting from models.Model class
	#pass
	text = models.TextField(default='')	#means we will have a model in db that is a TextField with a default value