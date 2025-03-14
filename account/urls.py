from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profileedit/', views.profile_edit, name='profile_edit')

    ]
