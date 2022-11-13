from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name='home'
urlpatterns = [
    path('', views.home, name='homepage'),
    path('login', views.login, name='loginpage'),

    path('password-reset', auth_views.PasswordResetView.as_view(template_name = 'password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('errorlogin', views.errorlogin, name='error_loginpage'),
    path('feedback', views.feedback, name='feedback-page'),
    path('user_module/',include(('user_module.urls','user_module'),namespace='user_module')),
]