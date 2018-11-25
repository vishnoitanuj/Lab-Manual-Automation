from django.conf.urls import url

from . import views


urlpatterns = [
	
	#home-page
	url(r'^$', views.home, name='home'),
	

	#blog and blog detail
	 url(r'^Assignment/$', views.AssignmentListView.as_view(), name='blog'),
	 url(r'^userlist/$', views.UserProfileListView.as_view(), name='user'),
	 url(r'^Assignment/(?P<pk>\d+)$', views.AssignmentDetailView.as_view(), name='blog-detail'),
	 url(r'^user/(?P<pk>\d+)$', views.UserProfileDetailView.as_view(), name='user-detail'),
	 
	 url(r'^Assignment/create$', views.AssignmentCreateView.as_view(), name='create'),



	 url(r'^shop/$', views.home, name='shop'),
	#  url(r'^shop/(?P<pk>\d+)$', views.ItemDetailView.as_view(), name='item-detail'),
	#  url(r'^shop/(?P<pk>\d+)/cart/$', views.CartCreate.as_view(), name='cart-add'), 
	#  url(r'^shop/(?P<pk>\d+)/comment/$', views.ItemCommentCreate.as_view(), name='item-comment'), 
	 

	 

	 url(r'^Assignment/update/(?P<pk>\d+)$', views.AssignmentUpdate.as_view(), name='update'),
	 url(r'^Assignment/delete/(?P<pk>\d+)$', views.AssignmentDelete.as_view(), name='delete'),
	
	 url(r'^Assignment/(?P<pk>\d+)/comment/$', views.AssignmentCommentCreate.as_view(), name='blog-comment'), 



	 
	 #user-shit
	 url(r'^register/$', views.register, name='register'),
	 url(r'^profile/$', views.profile, name='profile'),
	 url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	 url(r'^profile/edituser/$', views.edit_user_profile, name='edit_user_profile'),
	 
		 
]
