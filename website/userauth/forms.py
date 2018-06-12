from django import forms
from django.contrib.auth.models import User


class Register(forms.Form):
	first_name=forms.CharField(label="firstname",max_length=20,required=False,help_text='optional')
	last_name=forms.CharField(label="lastname",max_length=20,required=False,help_text='optional')
	username=forms.CharField(label="username",max_length=40,required=True)
	password1=forms.CharField(label="password",max_length=20,required=True,widget=forms.PasswordInput)
	password2=forms.CharField(label="confirm password",max_length=20,required=True,widget=forms.PasswordInput)
	emailid=forms.CharField(label="emailid",max_length=40,required=True)
	bio=forms.CharField(label="user bio",max_length=20,required=True,widget=forms.Textarea)
	date_of_birth=forms.CharField(label="date of birth",max_length=20,required=True,widget=forms.DateInput(attrs={'type':'date'}))

	class meta(object):
		"""docstring for meta"""
		model=Userfields=('username','first_name','last_name','password1','password2','email_id','bio','date_of_birth')
	def clean_username(self):
		#only one username for person
		user = self.cleaned_data.get('username').lower()
		check = User.objects.filter(username=user)
		if check.count() > 0:
			raise forms.ValidationError(' the username is already taken')
		else:
			return user

	def clean_password2(self):
		# check if bot passwords are equal
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Please enter same passwords both the times')
		if not(password1) and not(password2):
			raise forms.ValidationError('Please fill the password fields')
		if len(password1) < 8:
			raise forms.ValidationError('The password must be 8 chars ')
		return True

	def clean_emailid(self):
		# check if email is unique
		email = self.cleaned_data.get('emailid')
		check = User.objects.filter(email=email)
		if check.count() > 0:
			raise forms.ValidationError('The email already exists')
		return email

	def save(self):
		#saves the data to database

		user = User.objects.create_user(
			username=self.cleaned_data.get('username'),
			password=self.cleaned_data.get('password1'),
			email=self.cleaned_data.get('emailid'),
			first_name=self.cleaned_data.get('first_name'),
			last_name=self.cleaned_data.get('last_name')
		)