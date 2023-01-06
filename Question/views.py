# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.generics import GenericAPIView
#from rest_framework.status import status

# Create your views here.

#########################Get all question#############################################

class getAllQuestion(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = QuestionSerializer
    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

#######################################################################################3


##############################Get question#############################################

class getQuestion(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = QuestionSerializer
    def get(self, request, pk):
        question = Question.objects.get(_id=pk)
        serializer = QuestionSerializer(question, many=False)
        return Response(serializer.data)
#######################################################################################

###################################Post Answer################################################

class AnswerQuestion(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = QuestAnswersSerializer
    def post(self, request):
        print(request.data)
        x=request.data
        serializer = self.serializer_class(data=request.data)
        emp_id=Employee_Profile.objects.get(emp_id=x['emp_id'])
        question_id = Question.objects.get(_id=x['question_id'])
        if serializer.is_valid():
            serializer.validated_data.update({"emp_id":emp_id})
            serializer.validated_data.update({"question_id":question_id})
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

############################################Update Answer#########################################################

class UpdateAnswer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = QuestAnswersUpdateSerializer
    def put(self,request, pk):
        answer = User_Question_Answers.objects.get(_id=pk)
        serializer = QuestAnswersUpdateSerializer(instance=answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

####################################################################################################################


####################################################Get Answer#########################################################

class Answer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = QuestAnswersSerializer
    def get(self, request, pk):
        answer = User_Question_Answers.objects.get(_id=pk)
        serializer = QuestAnswersSerializer(answer, many=False)
        return Response(serializer.data)
##############################################################################################################################

############################################Get All Answer#########################################################

class getAllAnswer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = QuestAnswersSerializer
    def get(self, request):
        answer = User_Question_Answers.objects.all()
        serializer = QuestAnswersSerializer(answer, many=True)
        return Response(serializer.data)
#############################################################################################################
