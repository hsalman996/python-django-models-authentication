from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index' ), name='logout'),
=======
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
>>>>>>> ef849d2981303584ef5853170061b8e7cadfedd4
]