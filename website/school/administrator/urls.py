from . import views

from django.urls import path

from administrator import views as GeneratePDF

app_name = "administrator"

urlpatterns = [

	path('', views.administrator, name='administrator'),
	path('session/', views.session, name='session'),
	path('add_session/', views.add_session, name='add_session'),
	path('register/', views.add_student, name='register'),
	path('add_result/', views.add_result, name='add_result'),
	path('query_result/', views.query_result, name='query_result'),
	path('query_general_result/', views.query_general_result, name='query_general_result'),
	path('generate_average/', views.generate_average, name='generate_Result'),
	path('generate_result/', views.generate_result, name='generate_result'),
	path('add_student_result/<slug:pk>/', views.add_student_result, name='add_student_result'),
	path('term/', views.term, name='term'),
	path('addterm/', views.add_term, name='add_term'),
	path('pin/', views.pin, name='pin'),
	path('change_current_session/', views.change_current_session, name='change_current_session'),
	path('check_result/', views.check_result, name='check_result'),
	path('student_result/', views.student_result, name='student_result'),
	path('generatepin/', views.generatepin, name='generatepin'),
	path('pdf/', views.get_your_copy, name='get_your_copy'),
	path('updatenews/', views.NewsUpdate, name='news_update'),
	path('generate_course/', views.generate_course, name='generate_course'),
	path('promote/', views.QueryPromoteStudent, name='promote'),
	path('promote_student/', views.PromoteStudent, name='promote_student'),
	path('query_student/', views.query_student, name='query_student'),
	path('students/', views.students, name='students'),
	path('edit_student/<slug:id>/', views.edit_student, name='edit_student'),
	path('news/', views.news, name='news'),
	path('news/<slug:slug>/', views.newsdetails, name='newsdetails'),
	path('deletenews/<slug:slug>/', views.deletenews, name='deletenews'),
	path('editnews/<slug:slug>/', views.editnews, name='editnews'),

	path('query_student_term/', views.query_student_term, name='query_student_term'),
	path('change_student_term/', views.change_student_term, name='change_student_term'),
	path('select_student/', views.select_student, name='select_student'),




]