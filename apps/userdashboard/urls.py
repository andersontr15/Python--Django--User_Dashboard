from django.conf.urls import patterns, url
from apps.userdashboard import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'register$', views.register, name="register"),
	url(r'login$', views.login, name="login"),
	url(r'dashboard$', views.dashboard, name="dashboard"),
	url(r'logout$', views.logout, name="logout"),
	url(r'new$', views.new, name="new"),
	url(r'delete_message/(?P<message_id>\d+)/$', views.delete_message, name="delete_message"),
	url(r'create$', views.create, name="create"),
	url(r'^users/(?P<user_id>\d+)/$', views.profile_page, name="profile_page"),
	url(r'comment/$', views.comment, name="comment"),
	url(r'message/(?P<user_id>\d+)/$', views.message, name="message"),
	url(r'^users/(?P<user_id>\d+)/delete$', views.delete, name="delete"),
	url(r'^poke/(?P<user_id>\d+)/$', views.poke, name="poke"),
	url(r'^users/(?P<user_id>\d+)/edit$', views.edit, name="edit"),
	url(r'^users/(?P<user_id>\d+)/update$', views.update, name="update"),
	url(r'delete_comment/(?P<comment_id>\d+)/$', views.delete_comment, name="delete_comment"),
)