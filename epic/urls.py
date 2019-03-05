from django.conf.urls import url
from .import views
 url('^$',views.welcome,name = 'welcome'),
]
