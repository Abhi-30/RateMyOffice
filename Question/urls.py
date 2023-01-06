from django.contrib import admin
from django.urls import path
from .views import getAllQuestion,getQuestion,AnswerQuestion,UpdateAnswer,getAllAnswer,Answer

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('getAllQuestion/', getAllQuestion.as_view(), name='get All Question'),
    path('getQuestion/<str:pk>/',getQuestion.as_view(),name="getQuestion"),
    path('postAnswer/',AnswerQuestion.as_view(),name="AnswerQuestion"),
    path('getAnswer/<str:pk>/',Answer.as_view(),name="Answer"),
    path('UpdateAnswer/<str:pk>/',UpdateAnswer.as_view(), name='UpdateAnswer'),
    path('getAllAnswers/', getAllAnswer.as_view(), name='getAllAnswer'),   
]