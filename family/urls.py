from django.conf.urls import url
from . import views

app_name = 'family'
urlpatterns = [
    url(r'^$', views.familypage, name='familypage' ),
]