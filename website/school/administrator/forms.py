from django import forms
from .models import Session, Student, CurrentTerm, CurrentSession, News, GeneralResult, Gallery
from ckeditor.widgets import CKEditorWidget
#from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget
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

# class NewsUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model = NewsUpdate
# 		fields = ['title', 'body', 'status']
# 		widgets = {
# 		'body': CKEditorWidget()
# 		}

class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = ['title', 'body', 'status', 'timestamp']
		widgets = {
		'body': CKEditorWidget()
		}

	
class EditGeneralResultForm(forms.ModelForm):
	class Meta:
		model = GeneralResult
		fields = ['average', 'grade', 'percentage', 'total_subject', 'position', 'active']

class GalleryForm(forms.ModelForm):
	class Meta:
		model = Gallery
		fields = ['image', 'body']