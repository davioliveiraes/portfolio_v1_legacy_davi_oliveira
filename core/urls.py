from django.urls import path
from .views import HomeTemplateView, contato

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("contato/", contato, name="contato"),
]
