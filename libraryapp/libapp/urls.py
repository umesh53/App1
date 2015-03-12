from django.conf.urls import patterns, url
from libapp import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^register/$', CreateView.as_view(
		template_name='register.html',
		form_class=UserCreationForm,
		success_url='/libapp/users/')
	),
	url(r'^main/$', views.mainpage, name='mainpage'),
	url(r'^addpage/$', views.AddingBook, name='AddingBook'),
	url(r'^users/$', views.userspage, name='userspage'),
	url(r'^req_book/$', views.request_book, name='bookrequest'),
	url(r'^book_view/$', views.view_book, name='viewbooks'),
)