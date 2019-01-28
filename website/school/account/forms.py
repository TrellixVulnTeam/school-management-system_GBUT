from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, CharField

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.shortcuts import render,redirect

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput( 
        attrs={'class':'form-control', 'placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput( 
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))


class StudentLoginForm(forms.Form):		
	Registration_Nubmer = forms.CharField(widget=forms.TextInput( 
	    attrs={'class':'form-control', 'placeholder':'Enter username'}))
	password = forms.CharField(widget=forms.PasswordInput( 
	    attrs={'class':'form-control', 'placeholder':'Enter Password'}))
