from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from time import time
from django.utils.html import strip_tags
from ribbit_app.models import Ribbit


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))
    #gravatar_url = forms.ImageField(required=False)
    def is_valid(self):
        form = super(UserCreateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error ribbitText'})
        return form

    class Meta:
        fields = ['username','email', 'password1', 'password2']
        model = User


class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'password'}))

    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form


class RibbitForm(forms.ModelForm):
	content = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'ribbitText'}))
	pic = forms.ImageField(required=True)
	brightness = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Brightness: -100 to 100'}))
	
	def is_valid(self):
		form = super(RibbitForm, self).is_valid()
		for f in self.errors.iterkeys():
			if f != '__all__':
				self.fields[f].widget.attrs.update({'class': 'error ribbitText'})
		return form

	class Meta:
		model = Ribbit
		fields=('content', 'pic', 'brightness')
		exclude = ('user',)
