from django.contrib import admin
from django.urls import re_path as url
from API import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   url(r'^api/receta/$',views.RecetaViewSet.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)