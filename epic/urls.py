from django.conf.urls import url
from .import views
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.image_today,name='image_Today'),
]
