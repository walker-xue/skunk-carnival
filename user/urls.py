from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^index', views.index_page)
]
