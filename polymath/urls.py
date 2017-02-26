from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^assignment$', views.assignment, name='assignment'),
    url(r'^assignment/submit$', views.submit_answer, name='submit_answer'),
    url(r'^$', views.index, name='index'),
]