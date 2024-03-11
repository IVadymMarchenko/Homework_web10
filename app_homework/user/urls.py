from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .forms import LoginForm

app_name = 'user'

urlpatterns = [
    path('login/',LoginView.as_view(template_name='user/login.html',form_class=LoginForm),name='login'),
    path('Registration/',views.RegisterView.as_view(),name='Registration'),
    path('logout/',LogoutView.as_view(template_name='user/logout.html'), name='logout')
    ]

