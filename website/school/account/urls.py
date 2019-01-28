from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import login, logout
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from . import views
from django.contrib.auth import views as auth_views

 

from django.contrib.auth.views import PasswordResetView

from django.urls import path


app_name = "account"
urlpatterns = [
	# path('reset_password/', views.reset_password, name='test'),
	# path('reset_password_confirm/', views.reset_password_confirm, name='reset_password_confirm'),
	# path('change_password/', views.change_password, name='change_password'),
	# path('change_password_confirm/', views.change_password_confirm, name='change_password_confirm'),
	# path('<slug:pk>', views.change_password_code, name='change_password_code'),
	# path('change_password_success/', views.change_password_success, name='change_password_success'),
	# path('edit_profile/', views.edit_profile, name='edit_profile'),
	# path('profile/', views.profile, name='profile'),


	path('login/', views.login_page, name='login'),
	path('logout/', views.logout_page, name='logout'),
	path('logged_out/', views.logged_out, name='logged_out'),
	
	# path('register/', views.register, name='register'),
	# path('register_success/', views.registration_success, name='registration_success'),




] 







