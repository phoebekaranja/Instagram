from django.conf.urls import url
from .import views
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.image_today,name='image_Today'),
    url(r'^search/', views.search_results, name='search_results'),
]
