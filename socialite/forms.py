from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Home_page_post,user_profile,Post,Comment

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password mismatch")
        else:
            return confirm_password

class Home_page_post_form(forms.ModelForm):
    content2=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Say how you feel'}), label='')

    class Meta:
        model=Post
        fields = {
            'content2'
        }

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=(
            'title',
            'image',
            'content',
        )


class UserLoginForm(forms.Form):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class Profile_edit_form(forms.ModelForm):
    GENDER_CHOICES = (
        ('male', 'Male'),('female', 'Female'),
    )

    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    dob=forms.DateField(widget=forms.DateInput)
    class Meta:
        model=user_profile
        exclude=('user',)

class User_edit_form(forms.ModelForm):
    class Meta:
        model=User
        fields=(
            'first_name',
            'last_name',
            'email',
        )

class CommentForm(forms.ModelForm):
    content=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add your comment..'}),label='Comment')
    class Meta:
        model=Comment
        fields=('content',)