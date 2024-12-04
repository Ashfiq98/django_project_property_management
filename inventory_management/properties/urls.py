from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.signup, name='signup'),
    path('registration-success/', views.registration_success, name='registration_success'),

]
