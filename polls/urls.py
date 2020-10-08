from django.urls import path

from . import views


app_name = 'polls'


urlpatterns = [
    path('question_crepate/', views.PollsCreate.as_view(), name='createview'),
    path('login/', views.Login.as_view(), name='login'),
    path('answer_create/', views.PollsCreateChoice.as_view(), name='createchoise'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
    # path('<str:slugok>/', views.post_detail, name='detail')
]
