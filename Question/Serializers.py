from django.db import models
from rest_framework import serializers
from .models import Question,User_Question_Answers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from UserAccount.models import Employee_Profile   

User = get_user_model()

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields =('_id','emp_id','question_text','choice_text1', 'choice_text2', 'choice_text3', 'choice_text4', 'choice_text5', 'choice_text6', 'choice_text7', 'comment', 'count', 'created_at', 'updated_at', 'Date')
        #'user'

class QuestAnswersSerializer(serializers.ModelSerializer):
    #emp_id = serializers.RelatedField(source='Employee_Profile', read_only=True)
    #_id = serializers.RelatedField(source='User_Question_Answer', read_only=True)
    #question = serializers.RelatedField(source='Question', read_only=True)
    class Meta:
        model = User_Question_Answers
        fields = ('_id','emp_id','question_id', 'answer', 'answer1','user','date', 'comment', 'rating', 'count', 'created_at', 'updated_at')
        #depth = 1

class QuestAnswersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Question_Answers
        fields = ('answer','emp_id','answer1','comment','rating','updated_at')
       # depth = 1