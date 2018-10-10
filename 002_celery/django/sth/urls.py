from django.urls import path

from sth import views

urlpatterns = [
    path('task/', views.some_view),
]
