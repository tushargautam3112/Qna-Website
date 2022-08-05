"""questions URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('post_question', views.post_question, name='post_question'),
    path('post_que', views.post_que, name='post_que'),
    path('check_qna', views.check_qna, name='check_qna'),
    path('answers', views.answers, name='answers'),
    path('new_ans', views.new_ans, name='new_ans'),
]
