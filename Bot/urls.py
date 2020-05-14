from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reply/$', views.bot_reply),
    url(r'^export/$', views.export_chat),
]

