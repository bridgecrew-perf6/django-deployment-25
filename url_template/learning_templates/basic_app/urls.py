from django.urls import re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^other/$',views.other, name = 'other'),
    re_path(r'^relative_url_template/$',views.relative_url_template, name = 'relative_url_template'),
    
]