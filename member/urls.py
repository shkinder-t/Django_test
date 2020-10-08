from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('', views.CreateUserView.as_view(), name='registration'),
    path('acc', views.Newview.as_view(), name='newregistration'),
]