from django.contrib import admin

from .models import Session, Myclass, Subject, Student, Term,Student_subject, CurrentSession, CurrentTerm, GeneralResult, GeneratePin, SchoolLogo,News



admin.site.register(Myclass)
admin.site.register(Subject)

admin.site.register(CurrentSession)
admin.site.register(CurrentTerm)
admin.site.register(SchoolLogo)
admin.site.register(News)



class TermAdmin(admin.ModelAdmin):
	list_display = ['term', 'id']
class SessionAdmin(admin.ModelAdmin):
	list_display = ['date', 'id']

class Student_subjectAdmin(admin.ModelAdmin):
	list_display = ['student', 'Registration_Number', 'subject', 'session', 'term', 'current_class', 'first_test', 'second_test', 'exam' ,'average', 'grade']

class GeneralResultAdmin(admin.ModelAdmin):
	list_display = ['surname', 'average', 'position', 'percentage']
class StudentAdmin(admin.ModelAdmin):
	list_display = ['surname', 'first_name', 'average', 'Registration_Number', 'id', 'pin', 'current_class', 'current_session', 'current_term']

class GeneratePinAdmin(admin.ModelAdmin):
	list_display = ['Registration_Number', 'current_session', 'current_class', 'pin']

admin.site.register(GeneratePin, GeneratePinAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(GeneralResult, GeneralResultAdmin)
admin.site.register(Term, TermAdmin)	
admin.site.register(Student_subject, Student_subjectAdmin)
admin.site.register(Session, SessionAdmin)