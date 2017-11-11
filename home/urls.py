from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
	url(r'^login/$',views.loginkrdo.as_view(),name="loginkrdo"),
	url(r'^$',views.UserFormView.as_view(),name="user_form_view"),
    url(r'^home/$', views.homeview.as_view(), name='homepage' ),
    url(r'^addposts/$',views.postCreate.as_view(),name = 'addposts'),
    url(r'^home/(?P<pk>[0-9]+)/$',views.detailview.as_view(),name = 'detailview'),
    url(r'^logout/$',views.logoutkrdo,name='logoutkrdo'),
    url(r'^profile/(?P<id>[0-9]+)/$',views.profileupdate.as_view(),name='profile')
]