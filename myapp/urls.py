from . import views
from django.urls import path
from django.contrib.auth import views as auth_views 

urlpatterns = [    
    path('secure/', views.secure, name='secure'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
]