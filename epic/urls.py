from django.conf.urls import url
from .import views
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.image_today,name='image_Today'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^images/(\d+)',views.Image,name ='image'),
    url(r'^category/(\w+)',views.category_image,name='category_list'),
    url(r'^location/(\w+)',views.location_image,name='location_list'),
]
