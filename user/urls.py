from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('123/login/', auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),

]

