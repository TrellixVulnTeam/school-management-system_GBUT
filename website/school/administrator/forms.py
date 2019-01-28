from django import forms
from .models import Session, Student, CurrentTerm, CurrentSession, NewsUpdate
from ckeditor.widgets import CKEditorWidget
class AddSessionForm(forms.ModelForm):
	class Meta:
		model = Session
		fields = ['date']

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['surname', 'first_name', 'middle_name', 'date_of_birth', 'email', 'Registration_Number', 'Phone', 'Address', 'Gender', 'current_class', 'current_session', 'current_term']

class CurrentTermForm(forms.ModelForm):
	class Meta:
		model = CurrentTerm
		fields = ['term']

class CurrentSessionForm(forms.ModelForm):
	class Meta:
		model = CurrentSession
		fields = ['session']

class CheckResultForm(forms.Form):
	Registration_Number = forms.CharField(max_length=100)
	Pin = forms.CharField(max_length=100)

class NewsUpdateForm(forms.ModelForm):
	class Meta:
		model = NewsUpdate
		fields = ['title', 'body']
		widgets = {
		'body': CKEditorWidget()
		}

	

