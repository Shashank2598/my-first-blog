from django.conf.urls import url
from . import views

app_name = 'aboutme'
urlpatterns = [
    url(r'^$', views.mypage, name='mypage' ),
]