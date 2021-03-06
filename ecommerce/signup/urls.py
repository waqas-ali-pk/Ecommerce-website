from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^$', RedirectView.as_view(url='home/')),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),

]
