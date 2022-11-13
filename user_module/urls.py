from django.urls import path,include

from . import views

app_name='user_module'

urlpatterns = [
    path('skills', views.skills, name='skills-page'),
    path('projects', views.projects, name='projects-page'),
    path('profile', views.profile, name='profile-page'),
    path('logout', views.logout_page, name='logout-page'),
    path('projects/<int:pk>/', views.projects_detailview, name='projects-detail-page'),
    path('skills/<int:pk>/', views.skills_detailview, name='skills-detail-page'),

#project detailview redirection to other pages through nav bar
    path('projects/<int:pk>/projects', views.project_to_project_redirect, name='project-to-project-redirect'),
    path('projects/<int:pk>/skills', views.project_to_skill_redirect, name='project-to-skill-redirect'),
    path('projects/<int:pk>/profile', views.project_to_profile_redirect, name='project-to-profile-redirect'),
    path('projects/<int:pk>/logout', views.project_to_logout_redirect, name='project-to-logout-redirect'),

#skill detailview redirection to other pages through nav bar
    path('skills/<int:pk>/projects', views.skill_to_project_redirect, name='skill-to-project-redirect'),
    path('skills/<int:pk>/skills', views.skill_to_skill_redirect, name='skill-to-skill-redirect'),
    path('skills/<int:pk>/profile', views.skill_to_profile_redirect, name='skill-to-profile-redirect'),
    path('skills/<int:pk>/logout', views.skill_to_logout_redirect, name='skill-to-logout-redirect'),

] 