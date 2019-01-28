from django.shortcuts import render

from .models import Session, Myclass, Student, Student_subject, Subject, Term, GeneralResult, CurrentSession, CurrentTerm, GeneralResult, GeneratePin, SchoolLogo

from .forms import AddSessionForm, StudentForm, CurrentTermForm, CurrentSessionForm, CheckResultForm, NewsUpdateForm

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from django.http import HttpResponseRedirect, HttpResponse,JsonResponse

from django.contrib.auth.models import User

import random

import string

from random import choice 

from django.contrib.auth.decorators import login_required

from django.contrib import messages


from django.http import HttpResponse

from django.views.generic import View

from school.utils import render_to_pdf #created in step 4

from django.template.loader import get_template






# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('invoice.html')
#         context = {
#             "invoice_id": 123,
#             "customer_name": "John Cooper",
#             "amount": 1399.99,
#             "today": "Today",
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('administrator/check_result.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" %("12341231")
#             content = "inline; filename='%s'" %(filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" %(filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")




def term(request):
	current_term = CurrentTerm.objects.get(id=1)
	all_terms = Term.objects.all()
	

	# form = TermForm(request.POST or None)
	return render(request, 'administrator/term.html', {'current_term':current_term, 'all_terms':all_terms})
def add_term(request):
	detail = CurrentTerm.objects.get(id=1)
	if request.method == 'POST':
		form  = CurrentTermForm(request.POST or None, instance = detail)
		if form.is_valid():
			form.save()
			return redirect('administrator:term')
	else:
		form = CurrentTermForm(request.POST or None)
	context = {'form':form}
	return render(request, 'administrator/addterm.html',context)
	
@login_required(login_url='/accounts/login/')
def administrator(request):
	return render(request, 'administrator/base.html', {})

def session(request):
	current_session = CurrentSession.objects.get(id=1)
	session = Session.objects.all()
	context = {'session':session, 'current_session':current_session}
	return render(request, "administrator/session.html", context)

def add_session(request):
	current_session = CurrentSession.objects.get(id=1)
	if request.method == 'POST':
		form = AddSessionForm(request.POST or None, request.FILES or None)		
		if form.is_valid():

			ok = form.save(commit = False)
			ok.save()


			# myclass = ['kg1', 'kg2', 'kg3', 'pry1', 'pry2', 'pry3', 'pry4', 'pry5', 'jss1', 'jss2', 'jss3', 'sss1', 'sss2', 'sss3']
			# for i in myclass:
			# 	new = Myclass()
			# 	new.session = Session.objects.get(pk=ok.pk)
			# 	new.myclass = i
			# 	new.save() 

			return redirect('administrator:session')
	else:
		form = AddSessionForm(request.POST or None) 
	context = {'form':form,}
	return render(request, "administrator/addsession.html", context)


def change_current_session(request):
	if request.method == 'POST':
		form  = CurrentSessionForm(request.POST or None)
		if form.is_valid():

			select = form.save(commit=False)
			print(select.session)
			current_session = CurrentSession.objects.get(id=1)
			current_session.session = select.session
			current_session.save()
			return redirect('administrator:session')
	else:
		form = CurrentSessionForm(request.POST or None)
	context = {'form':form}
	return render(request, "administrator/change_current_session.html", context)


def add_student(request):
	if request.method == 'POST':
		form = StudentForm(request.POST or None, request.FILES or None)		
		if form.is_valid():
			ok = form.save(commit = False)
			ok.save()

			add_subject(ok.pk, ok)

			return redirect('administrator:register')
	else:
		form = StudentForm(request.POST or None) 
	context = {"form": form} 
	return render(request, "administrator/register.html", context)


def add_subject(pk, ok):

	kidergarten = ['kg1', 'kg2', 'kg3']
	primary = ['pry1', 'pry2', 'pry3', 'pry4', 'pry5']
	junoir_secondary = ['jss1', 'jss2', 'jss3']
	senoir_secondary = ['sss1', 'sss2', 'sss3']

	subject_code = ""

	current_student = Student.objects.get(pk=pk)

	if current_student.current_class in kidergarten:
		subject_code = "0"
	elif current_student.current_class in primary:
		subject_code = "1"
	elif current_student.current_class in junoir_secondary:
		subject_code = "2"
	else:
		subject_code = "3" 

	all_subject = Subject.objects.all()

	for subject in all_subject:

		if subject_code in list(subject.no):

			new = Student_subject()
			new.student = current_student
			new.subject = subject
			new.session = ok.current_session
			new.term = ok.current_term
			new.current_class = ok.current_class
			new.Registration_Number=ok.Registration_Number

			new.save()

		else:

			pass


	print("done adding subjects to students")


def add_result(request):
	session = request.POST.get('session')
	session2 = Session.objects.get(date=session)
	session_new = session2.id

	term = request.POST.get('term')
	term2 = Term.objects.get(term=term)
	term_new = term2.id

	myclass = request.POST.get('myclass')


	subject = request.POST.get('subject')
	subject2 = Subject.objects.get(subject_name=subject)
	subject_new = subject2.id

	# print(session_new, term_new, myclass, subject_new)
	qs = Student_subject.objects.filter(subject=subject_new, session=session_new, term=term_new, current_class=myclass).order_by('-average')
	# a=1
	# for i in qs:
	# 	stu = Student_subject.objects.get(id=i.id, subject=subject_new, session=session_new, term=term_new, current_class=myclass)
	# 	stu.position = a 
	# 	stu.save()
	# 	a+=1

	# 	print(stu, stu.position)


	context={'qs':qs, 'session':session, 'term':term, 'myclass':myclass, 'subject':subject}
	return render (request, 'administrator/addresult.html', context)

def query_result(request):
	term = Term.objects.all()
	session = Session.objects.all()
	myclass = Myclass.objects.all()
	subject = Subject.objects.all()
	context = {'session':session, 'term':term, 'myclass':myclass, 'subject':subject }
	return render (request, 'administrator/queryresult.html', context)


def add_student_result(request, pk):

	current_student = Student_subject.objects.get(pk = pk)

	myform = request.POST
	first_test = myform['first_test']
	second_test = myform['second_test']
	exam = myform['exam']

	current_student.first_test = first_test
	current_student.second_test = second_test
	current_student.exam = exam
	average = int(first_test) + int(second_test) + int(exam)
	average1 = average/100
	average_new = average1 * 100
	if average_new <=40:
		grade = 'F'
	elif average_new >= 80 and average_new <= 100:
		grade = 'A' 
	elif average_new >= 70 and average_new <= 79:
		grade = 'B'
	elif average_new >= 60 and average_new <= 69:
		grade = 'C'
	elif average_new >= 50 and average_new <= 59:
		grade = 'D'


	


	current_student.average = average_new
	current_student.grade = grade
	print(grade)
	print(current_student.average)
	print(int(first_test))
	print(int(second_test))
	print(int(exam))
	current_student.save()
	context = {'grade':grade, 'average_new':average_new}	
	return JsonResponse(context)
def query_general_result(request):
	current_session = CurrentSession.objects.get(id=1)
	term = CurrentTerm.objects.get(id=1)


	return render(request, 'administrator/query_general_result.html', {'current_session':current_session, 'term':term} )


def generate_Result(request):
	current_session = CurrentSession.objects.select_related('session').get(id=1)
	current_term  = CurrentTerm.objects.select_related('term').get(id=1) 
	current_class = request.POST.get('select_class')

	s = Session.objects.get(date=current_session.session)
	t = Term.objects.get(term=current_term.term)

	stu = Student.objects.filter(current_class=current_class, current_term=t.id, current_session=s.id)
	for i in stu:
		specific_sub = Student_subject.objects.filter(student=i.id)
		student = ''
		for c in specific_sub:
			student = c.student

		sub = Student_subject.objects.filter(student=i.id)
		final_total =  Student_subject.objects.filter(student=i.id).exclude(average=0).count()

		a=0
		for b in sub:
			a+=b.average
		
		test =  a 
		# print(test)
		tot = final_total * 100
		overall = (test/tot) * 100 
		i.average = a
		i.percentage=overall
		# print(i.average)
		# print(i.percentage)
		i.total_course = final_total
		i.save()
		
	generate = Student.objects.filter(current_session=s.id, current_term=t.id, current_class=current_class).order_by('-average')
	n=1
	for i in generate:
		try:

			if i.percentage <=40:
				grade = 'F'
			elif i.percentage>= 80 and i.percentage <= 100:
				grade = 'A' 
			elif i.percentage >= 70 and i.percentage <= 79:
				grade = 'B'
			elif i.percentage >= 60 and i.percentage <= 69:
				grade = 'C'
			elif i.percentage >= 50 and i.percentage <= 59:
				grade = 'D'
			gen = GeneralResult.objects.get(surname=i.surname, first_name=i.first_name, middle_name=i.middle_name, Registration_Number=i.Registration_Number, current_session=i.current_session, current_term=i.current_term, current_class=i.current_class)
			gen.position=n
			gen.average = i.average
			gen.percentage = i.percentage
			gen.total_subject = i.total_course
			gen.sex = i.Gender
			gen.grade = grade

			gen.save()
			n+=1
		except GeneralResult.DoesNotExist:
			gen = GeneralResult.objects.create(surname=i.surname, first_name=i.first_name, middle_name=i.middle_name, Registration_Number=i.Registration_Number, current_session=i.current_session, current_term=i.current_term, current_class=i.current_class, position=n, average=i.average)
			n+=1
	result = GeneralResult.objects.filter(current_session=s, current_term=t, current_class=current_class)
	context={'result':result, 't':t, 's':s}
	return render(request, 'administrator/generate_Result.html', context)


def check_result(request):	
	Registration_Number = request.POST.get('reg_number')
	pin = request.POST.get('pin')
	print(Registration_Number)
	print(pin)
	try:
		gen = GeneratePin.objects.get(Registration_Number=Registration_Number, pin=pin)
		result = GeneralResult.objects.get(Registration_Number=Registration_Number, current_session=gen.current_session, current_class=gen.current_class)
		print(result)
		print('ok')
	except GeneratePin.DoesNotExist:
		print('none')
	return render(request, 'administrator/check_result.html', {})



def get_your_copy(request):
	image = SchoolLogo.objects.all()
	reg = request.POST.get('reg')
	pin = request.POST.get('pin')
	gen = GeneratePin.objects.get(Registration_Number=reg, pin=pin)
	result = GeneralResult.objects.get(Registration_Number=gen.Registration_Number, current_session=gen.current_session, current_class=gen.current_class)
	s = Session.objects.get(date=gen.current_session)
	total_student = Student.objects.filter(current_class=gen.current_class).count()
	record = Student_subject.objects.filter(Registration_Number=gen.Registration_Number, session=s.id, term=1, current_class=gen.current_class).exclude(average=0)
	template = get_template('administrator/check_result.html')
	context={'gen':gen, 'result':result, 'record':record, 'total_student':total_student, 'image':image, 'reg':reg, 'pin':pin}
	html = template.render(context)
	pdf = render_to_pdf('administrator/check_result.html', context)
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')

		filename = "%s_article.pdf" %('post_title')
		content = "inline; filename=%s" %(filename)
		download = request.GET.get("download")
		if download:
			content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response
	return HttpResponse("Not found")




def student_result(request):
	image = SchoolLogo.objects.all()
	if request.method=='POST':
		form = CheckResultForm(request.POST or None)
		if form.is_valid():
			reg = form.cleaned_data.get('Registration_Number')
			pin = form.cleaned_data.get('Pin')
			term = request.POST.get('term')
			t = Term.objects.get(term=term)
			try:					
				# print(image)		
				gen = GeneratePin.objects.get(Registration_Number=reg, pin=pin)
				result = GeneralResult.objects.get(Registration_Number=gen.Registration_Number, current_session=gen.current_session, current_class=gen.current_class, current_term=term)
				s = Session.objects.get(date=gen.current_session)
				# t = Term.objects.get(term=current_term.term)
				total_student = Student.objects.filter(current_class=gen.current_class, current_session=s.id, current_term=t.id ).count()
				record = Student_subject.objects.filter(Registration_Number=gen.Registration_Number, session=s.id, term=t.id, current_class=gen.current_class).exclude(average=0)
				print(record)
				context={'gen':gen, 'result':result, 'record':record, 'total_student':total_student, 'image':image, 'reg':reg, 'pin':pin}
				return render(request, 'administrator/check_result.html', context)
			except GeneratePin.DoesNotExist:
				# messages.error(request, 'Invalid details')

				return HttpResponse('invalid details')
		
	else:
		form = CheckResultForm()
	return render(request, 'administrator/student_result.html', {'form':form, 'image':image})



# def student_result(request):
# 	image = SchoolLogo.objects.all()
# 	if request.method=='POST':
# 		form = CheckResultForm(request.POST or None)
# 		if form.is_valid():
# 			reg = form.cleaned_data.get('Registration_Number')
# 			pin = form.cleaned_data.get('Pin')
# 			try:		
				
# 				print(image)		
# 				gen = GeneratePin.objects.get(Registration_Number=reg, pin=pin)
# 				result = GeneralResult.objects.get(Registration_Number=gen.Registration_Number, current_session=gen.current_session, current_class=gen.current_class)
# 				s = Session.objects.get(date=gen.current_session)
# 				# t = Term.objects.get(term=current_term.term)
# 				total_student = Student.objects.filter(current_class=gen.current_class).count()
# 				record = Student_subject.objects.filter(Registration_Number=gen.Registration_Number, session=s.id, term=1, current_class=gen.current_class).exclude(average=0)
# 				print(record)
# 				return render(request, 'administrator/check_result.html', {'gen':gen, 'result':result, 'record':record, 'total_student':total_student, 'image':image})
# 			except GeneratePin.DoesNotExist:
# 				messages.error(request, 'Invalid details')

# 				return render(request, 'administrator/check_result.html', {'image':image})
		
# 	else:
# 		form = CheckResultForm()
# 	return render(request, 'administrator/student_result.html', {'form':form, 'image':image})



def generatepin(request):
	session = Session.objects.all()
	return render(request, 'administrator/generatepin.html', {'session':session})

def pin(request):
	current_session = request.POST.get('select_session')
	current_class = request.POST.get('select_class')
	session = Session.objects.get(date=current_session)
	student = Student.objects.filter(current_class=current_class, current_session=session.id)

	for i in student:
		print(i.id)
		allchar = string.ascii_letters + string.digits
		pin = ''.join(choice(allchar) for x in range(13))
		generate = GeneratePin.objects.get_or_create(Registration_Number=i.Registration_Number, current_session=session, current_class=current_class, pin=pin)
	return render(request, 'administrator/pin.html', {})

def NewsUpdate(request):
	if request.method == 'POST':
		form  = NewsUpdateForm(request.POST or None)
		if form.is_valid():
			form.save()
			return HttpResponse('done')
	else:
		form = NewsUpdateForm()
	context = {'form':form}
	return render(request, "administrator/news.html", context)
