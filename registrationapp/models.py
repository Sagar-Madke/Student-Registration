from django.db import models
from django.utils import timezone

class Register(models.Model):
	reg_no = models.AutoField(primary_key = True)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	dob = models.DateField(default=timezone.now, null=True)
	email = models.EmailField(max_length=254, null=True)

	
class Gallary(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	upload_image = models.FileField(upload_to='uploads/%Y/%m/%d/')


	"""def	__str__(self):
		return	self.name"""


	