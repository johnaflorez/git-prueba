from django.conf.urls import url
from django.contrib.auth import views

from .views import signup, UserUpdateView

app_name = 'accounts'
urlpatterns = [
    # Registro, Login y Logout de usuarios
    url(r'^signup/$', signup, name='signup'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^settings/account/$', UserUpdateView.as_view(), name='my_account'),
]
