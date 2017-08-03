from django.conf.urls import url
from .import views

app_name = 'Aptitude'
urlpatterns = [
	
	url(r'^$', views.view_homepage, name='view_homepage'),
	url(r'^attendee_register/$', views.attendee_register, name='attendee_register'),
	url(r'^add_attendee/$', views.add_attendee, name='add_attendee'),
	url(r'^python_question/$', views.PythonQuestionView.as_view(), name='index'),
	url(r'^java_question/$', views.JavaQuestionView.as_view(), name='index'),
	url(r'^question/(?P<pk>[0-9]+)/', views.QuestionDetailView.as_view(), name='question'),
	# url(r'^language/$', views.view_language, name='view_language'),
	url(r'^attendee_list/$', views.view_attendee_list, name='view_attendee_list'),
	url(r'^delete_attendee/$', views.delete_attendee, name='delete_attendee'),

	url(r'^save_attendee_details/$', views.save_attendee_details, name='save_attendee_details'),
	]
	

    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	# url(r'^(?P<question_id>[0-9]+)/count/$', views.count, name='count'),
	# url(r'^(?P<question_id>[0-9]+)/next/$', views.get_next_id, name='next'),
	# url(r'^(?P<question_id>[0-9]+)/previous/$', views.get_prev_id, name='previous'),

	# url(r'^python_ques/$', views.IndexView.as_view(), name='index'),


	