from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Employee_Profile,Employee_Role,Employee_Services
from django.contrib.auth import get_user_model
User = get_user_model()

#Serializer to Get User Details using Django Token Authentication
#class UserSerializer(serializers.ModelSerializer):
#  class Meta:
#    model = User
#    fields = ["id", "username","password", "email"]
    #"first_name", "last_name", 
    
    

class EmployeeRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Role
        fields ='__all__'

    
#Serializer to Register User
class EmployeeProfileSerializer(serializers.ModelSerializer):
    # initialize fields
    #employee_photo=Base64ImageField(max_length=None, use_url=True, required=False, allow_null=True)
    class Meta:
        model = Employee_Profile
        # fields="__all__"
        exclude = ('password',)


class AddServicesSerializer(serializers.ModelSerializer):
    # initialize fields
    employee_profile = serializers.PrimaryKeyRelatedField(queryset=Employee_Profile.objects.all())
    #employee_photo=Base64ImageField(max_length=None, use_url=True, required=False, allow_null=True)
    class Meta:
        model = Employee_Services
        fields=('Service_Name','Service_Description','employee_profile',)
    

class showallServiceSerializer(serializers.ModelSerializer):
    # initialize fields
    #employee_photo=Base64ImageField(max_length=None, use_url=True, required=False, allow_null=True)
    class Meta:
        model = Employee_Services
        fields='__all__'
        

class EmployeeServiceUpdateSerializer(serializers.ModelSerializer):
    # initialize fields
    class Meta:
        model = Employee_Services
        fields=('Service_Name','Service_Description',)


class EmployeeProfileRegisterSerializer(serializers.ModelSerializer):
    # initialize fields
    password = serializers.CharField(required=True, write_only=True)
    #is_superuser = serializers.BooleanField(required=False,default=False)
    #employee_photo=Base64ImageField(max_length=None, use_url=True, required=False, allow_null=True)
    class Meta:
        model = Employee_Profile
        fields = ["employee_email","password","user_type",]
        #exclude = ('user_permissions', 'is_superuser', 'last_login')

    def create(self, validated_data):
       
        user = Employee_Profile(
            employee_email=validated_data.get('employee_email'),
            employee_firstname=validated_data.get('employee_firstname'),
           # employee_lastname=validated_data.get('employee_lastname'),
           # employee_officephoneno=validated_data.get('employee_officephoneno'),
           # employee_mobileno=validated_data.get('employee_mobileno'),
            #employee_rfid=validated_data.get('employee_rfid'),
           # employee_country=validated_data.get('employee_country'),
            #employee_province=validated_data.get('employee_province'),
           # employee_city=validated_data.get('employee_city'),
           # employee_district=validated_data.get('employee_district'),
           # employee_subdistrict=validated_data.get('employee_subdistrict'),
           # employee_street=validated_data.get('employee_street'),
            #employee_unitno=validated_data.get('employee_unitno'),
           # employee_zipcode=validated_data.get('employee_zipcode'),
           # employee_ok_name=validated_data.get('employee_ok_name'),
           # employee_nok_contactno=validated_data.get('employee_nok_contactno'),   
           # employee_nok_email=validated_data.get('employee_nok_email'),
           # created_by=validated_data.get('created_by'),
           # updated_by=validated_data.get('updated_by'),
           # employee_role=validated_data.get('employee_role'),
            user_type=validated_data.get('user_type'),
           # is_superuser=validated_data.get('is_superuser'),
           # is_officier=validated_data.get('is_officier'),
           # is_serviceprovider=validated_data.get('is_serviceprovider'),
           # employee_photo=validated_data.get('employee_photo'),
            #Partner_Govt_Id=validated_data.get('Partner_Govt_Id'),
           # Partner_No_Of_Deposits=validated_data.get('Partner_No_Of_Deposits'),
           # Partner_QRCode=validated_data.get('Partner_QRCode'),
           # Partner_DOB=validated_data.get('Partner_DOB'),
           # Partner_Gender=validated_data.get('Partner_Gender'),
           # is_active=True
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class RegisterServiceProvider(serializers.ModelSerializer):
    
    class Meta:
        model = Employee_Profile
        fields = ["serviceprovider_name","website","No_of_employees","founding_year","tagline","Description",
                  "Logo","video_links","Contact_phone","Country","City","Zipcode","State","phone_no",]



class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)
    class Meta:
        model = Employee_Profile
        fields = ["employee_email","is_verified"]
  
class EmployeeProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Profile
        fields=("employee_email","user_type")

class ChangePasswordSerializer(serializers.Serializer):
    model = Employee_Profile
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    