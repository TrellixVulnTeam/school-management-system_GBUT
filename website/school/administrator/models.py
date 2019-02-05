from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify


class Session(models.Model):

	date = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.date
class CurrentSession(models.Model):
	session = models.ForeignKey(Session, on_delete=models.CASCADE)
	# def __str__(self):
	# 	return self.session

class Myclass(models.Model):

	myclass = models.CharField(max_length=20)
	session = models.ForeignKey(Session, on_delete=models.CASCADE)

	def __str__(self):
		return self.myclass

class Term(models.Model):

	class_term = (
		('1st term', '1st term'),
		('2nd term', '2nd term'),
		('3rd term', '3rd term'),)
	term = models.CharField(max_length=20, choices=class_term)
		
	def __str__(self):
		return self.term
class CurrentTerm(models.Model):
	term = models.ForeignKey(Term, on_delete=models.CASCADE)

class Student(models.Model):

	class_student = (
		('kg1', 'kg1'),
		('kg2', 'kg2'),
		('kg3', 'kg3'),
		('pry1', 'pry1'),
		('pry2', 'pry2'),
		('pry3', 'pry3'),
		('pry4', 'pry4'),
		('pry5', 'pry5'),
		('jss1', 'jss1'),
		('jss2', 'jss2'),
		('jss3', 'jss3'),
		('sss1', 'sss1'),
		('sss2', 'sss2'),
		('sss3', 'sss3'),

		)

	gen=(('M', 'Male'),('F', 'Female'))
	surname = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50, blank = True)
	Registration_Number = models.CharField(max_length=12, unique=True)
	Phone=models.CharField(max_length=30, default='+234')
	Address = models.CharField(max_length=600)
	Gender = models.CharField(max_length=1, choices=gen)
	Father_Name = models.CharField(max_length=220)
	Mother_Name = models.CharField(max_length=220)	
	date_of_birth  = models.DateField()
	email = models.EmailField(unique=True)
	Passport = models.FileField(blank=True)
	current_class = models.CharField(max_length=5, choices=class_student, default="")
	current_session = models.ForeignKey(Session, on_delete=models.CASCADE, default=1)
	current_term = models.ForeignKey(Term, on_delete=models.CASCADE, default=1)
	average = models.PositiveIntegerField(default=0)
	percentage = models.PositiveIntegerField(default='0')
	pin = models.CharField(max_length=100, default='')
	total_course  = models.PositiveIntegerField(default=0)



	def __str__(self):
		return self.Registration_Number







class Subject(models.Model):
	
	subject_name = models.CharField(max_length=20)
	# session = models.ForeignKey(Session, on_delete=models.CASCADE, default='')
	no = models.CharField(max_length = 5, default="0")





	def __str__(self):
		return self.subject_name


class Student_subject(models.Model):

	student = models.ForeignKey(Student, on_delete = models.CASCADE, default=0)
	Registration_Number = models.CharField(max_length=50)
	subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
	session = models.ForeignKey(Session, on_delete=models.CASCADE, default=1)
	term = models.ForeignKey(Term, on_delete=models.CASCADE, default=1)
	current_class = models.CharField(max_length=5, default="")
	first_test = models.PositiveIntegerField(default=0)
	second_test = models.PositiveIntegerField(default=0)
	exam = models.PositiveIntegerField(default=0)
	average = models.PositiveIntegerField(default=0)
	# position = models.CharField(max_length=1000, blank=True)
	grade = models.CharField(max_length=1, blank=True)

	def __str__(self):
		return self.student.surname + " " +self.subject.subject_name

class GeneralResult(models.Model):
	# qs = models.ForeignKey(Student, on_delete=models.CASCADE, default=10)
	surname = models.CharField(max_length=200, default="")
	first_name = models.CharField(max_length=200, default="")
	middle_name = models.CharField(max_length=200, default="")
	sex = models.CharField(max_length=10, default='')
	Registration_Number = models.CharField(max_length=200, default="")
	current_session = models.CharField(max_length=200, default="")
	current_term = models.CharField(max_length=200, default="")
	current_class = models.CharField(max_length=5, default="")
	average = models.PositiveIntegerField(default=0)
	grade = models.CharField(max_length=3, default='')
	position = models.CharField(max_length=500, default='')
	total_subject = models.CharField(max_length=30, default='')
	percentage = models.CharField(max_length=3, default='') 
	active =  models.BooleanField(default=True)
	def __str__(self):
		return self.surname 


class GeneratePin(models.Model):
	Registration_Number = models.CharField(max_length=50)
	current_session = models.CharField(max_length=50)
	current_class = models.CharField(max_length=10, default='')
	pin = models.CharField(max_length=50, unique=True)
	
	def __str__(self):
		return self.Registration_Number


class SchoolLogo(models.Model):
	image = models.FileField()



class News(models.Model):
	choices = (('published', 'published'), 
		('draft', 'draft')
		)
	title = models.CharField(max_length=50)
	body = models.TextField()
	status = models.CharField(max_length=15, choices=choices, default='published')
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	slug = models.SlugField()
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super (News, self).save(*args, **kwargs)
	def __str__(self):
		return self.slug

