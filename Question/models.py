
# Create your models here.
from django.db import models
from UserAccount.models import Employee_Profile

# Create your models here.

class Question(models.Model):
    _id = models.AutoField(primary_key=True,editable=False)
    emp_id = models.ForeignKey(Employee_Profile, on_delete=models.SET_NULL,null = True)
    question_text = models.CharField(max_length=200,null=True, blank=True)
    choice_text1 = models.CharField(max_length=200, null=True, blank=True)
    choice_text2 = models.CharField(max_length=200, null=True, blank=True)
    choice_text3 = models.CharField(max_length=200, null=True, blank=True)
    choice_text4 = models.CharField(max_length=200, null=True, blank=True)
    choice_text5 = models.CharField(max_length=200, null=True, blank=True)
    choice_text6 = models.BooleanField(default=False, null=True, blank=True)
    choice_text7 = models.BooleanField(default=False, null=True, blank=True)
    comment = models.CharField(max_length=200,null=True, blank=True)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    Date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return str(self.question_text)
    
class User_Question_Answers(models.Model):
    _id = models.AutoField(primary_key=True,editable=False)
    emp_id = models.ForeignKey(Employee_Profile,on_delete=models.SET_NULL,null = True)
    question_id = models.ForeignKey(Question, on_delete=models.SET_NULL,null = True)
    user = models.CharField(max_length=200,default="Anonymous_User",blank=True)
    answer = models.CharField(max_length=200,null=True, blank=True)
    answer1 = models.BooleanField(default=False, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    comment = models.CharField(max_length=200,null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return  str(self.emp_id) +" "+ str(self.question_id) 
   # def employee_firstname(self):
   #     return self.emp_id.employee_firstname
       
