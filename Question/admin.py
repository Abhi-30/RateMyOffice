from django.contrib import admin

# Register your models here.
from . models import Question,User_Question_Answers
 
admin.site.register(Question)
admin.site.register(User_Question_Answers)