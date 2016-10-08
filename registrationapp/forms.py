from django	import forms
from .models import	Register
from .models import Gallary

class RegisterForm(forms.ModelForm):
	class Meta:
		model =	Register
		fields = ('reg_no',	'name', 'address', 'dob', )

class GallaryForm(forms.ModelForm):
	class Meta:
		model =	Gallary
		fields = ('title',	'description', 'upload_image')