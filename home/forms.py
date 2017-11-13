from django import forms
from .models import Profile,post
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','email','password']

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','password']	

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name','bio','photo']

class AddPostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'category', 'by', 'pic','description']
        widgets = {
            'description': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }