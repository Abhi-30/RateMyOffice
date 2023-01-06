from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import *
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication

from rest_framework import generics

from rest_framework.authtoken.models import Token
from rest_framework import status 
from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
    HTTP_200_OK
)
from rest_framework.generics import GenericAPIView
#from social_django.utils import psa
#from requests.exceptions import HTTPError
from .emails import *

from .Serializers import *  

#########################Class based view to register user#############################################
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = EmployeeProfileRegisterSerializer
  
  def post(self, request, format='json'):
        print(request.data)
        role = str(request.data.get('user_type'))
        print(role)
        serializer = self.serializer_class(data=request.data)       
        
        if serializer.is_valid():
            serializer.update(is_service_provider=True)
            serializer.save()
            send_otp_via_email(serializer.data['employee_email'])
            return Response(serializer.data)
            #if role == 'Admin':
            #    print(" admin area ")
                #testmodel_object = self.get_object(request)
                #print(testmodel_object)
                #testmodel_object['is_superuser'] = 'True'
            #    serializer = EmployeeProfileUpdateSerializer(testmodel_object, data=request.data, partial=True)
            #    if serializer.is_valid():
            #        serializer.save()
            #        return Response(status=HTTP_200_OK, data=serializer.data)
            #    return Response({"error": "Something went wrong "},status=HTTP_400_BAD_REQUEST) 
            #if user:
              #  token = Token.objects.create(user=user)
               # json = serializer.data
                #json['token'] = token.key
                #return Response(json, status=status.HTTP_201_CREATED)
            #else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
##############################################################################################################


############################################ Verify OTP ###################################################################
class VerifyOTP(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        employee_email = request.data.get("employee_email")
        otp = request.data.get("otp")
        
        if employee_email is None or otp is None:
            return Response({'error': 'Please provide both employee_email and otp'},
                            status=HTTP_400_BAD_REQUEST)
        print (employee_email,otp)
        
        emp = Employee_Profile.objects.filter(Q(employee_email=employee_email) & Q(otp=otp))
        print(emp)
        if emp:
            emp.update(is_verified=True)
            return Response({'message': 'OTP verified successfully'},
                            status=HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
            
################################################################################################



###################################Login view##################################################################

class EmployeeLogin(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        employee_email = request.data.get("employee_email")
        password = request.data.get("password")
        if employee_email is None or password is None:
            return Response({'error': 'Please provide both employee_email and password'},
                            status=HTTP_400_BAD_REQUEST)
        print (employee_email,password)
        #emp = Employee_Profile.objects.filter(Q(employee_email=employee_email) & Q(password=password))
        user = authenticate(employee_email=employee_email,password=password)
        print(user)
       # token, _ = Token.objects.get_or_create(user=user)
        if user is None:
                    return Response({'error': 'Invalid Credentials'},
                                    status=HTTP_404_NOT_FOUND)
        else:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},
                    status=HTTP_200_OK)    
##################################################################################################################     

##################################Change Password View###########################################################
class ChangePasswordView(GenericAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = Employee_Profile
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
        else:
            return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)
        
########################################################################################################  

###############################Update User Details View####################################################
class EmployeeUpdate(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get_object(self, request):
        email = request.data.get("employee_email")
        return Employee_Profile.objects.get(employee_email=email)

    def patch(self, request):
        testmodel_object = self.get_object(request)
        print(testmodel_object)
        print(request.data)
        serializer = EmployeeProfileUpdateSerializer(testmodel_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_200_OK, data=serializer.data)
        return Response({"error":(serializer.errors)},status=HTTP_400_BAD_REQUEST)
#############################################################################################################

############################################ logout view #####################################################
class Logout(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get(self, request, format=None):
        # simply delete the token to force a login
        self.request.user.auth_token.delete()
        return Response({'message': 'Logout Success'}, status=HTTP_200_OK)
###################################################################################################################
                                                          
#########################################employee detail############################################################

# Get Employee Details View
class getEmployee(APIView):
   # permission_classes=[IsAuthenticated]
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = EmployeeProfileSerializer

    def get(self, request):
        user = self.request.user
        profile = Employee_Profile.objects.filter(employee_email=user)
        serializer = EmployeeProfileSerializer(profile, many=True)
        return Response({'employee': serializer.data}, status=HTTP_200_OK)

#############################################################################################################

############################################# Show all employee role ###############################################################################

class getEmployeeRole(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = EmployeeRoleSerializer

    def get(self, request):
        user = self.request.user
        profile = Employee_Role.objects.all()
        serializer = EmployeeRoleSerializer(profile, many=True)
        
        return Response({'employee role': serializer.data}, status=HTTP_200_OK)

#######################################################################################################################

#################################### All employee details ###################################################################################

class getAllemployee(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = EmployeeProfileSerializer

    def get(self, request):
        user = self.request.user
        profile = Employee_Profile.objects.all()
        serializer = EmployeeProfileSerializer(profile, many=True)
        return Response({'employee': serializer.data}, status=HTTP_200_OK)
###################################################################################################################################


####################################### Fill the details of Service Provider ####################################################################
class RegisterServiceProviderAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get_object(self, request):
        emp_id = request.data.get("emp_id")
        return Employee_Profile.objects.get(emp_id=emp_id)

    def patch(self, request):
        testmodel_object = self.get_object(request)
        print(testmodel_object)
        print(request.data)
        serializer = RegisterServiceProvider(testmodel_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_200_OK, data=serializer.data)
        return Response({"error":(serializer.errors)},status=HTTP_400_BAD_REQUEST)
    
###############################################################################################################################################

########################## Add Services for Service Provider #############################################################################################
class AddServices(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def post(self, request):
        serializer = AddServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#######################################################################################################################


###################################  Show All Services ##############################################################################
class Showallservices(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = showallServiceSerializer

    def get(self, request):
        user = self.request.user
        profile = Employee_Services.objects.all()
        serializer = showallServiceSerializer(profile, many=True)
        return Response({'services': serializer.data}, status=HTTP_200_OK)
    
###############################################################################################################


########################### Show Service of Particular Service Provider ##############################################################################################
class ShowService(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = showallServiceSerializer
    
    def get(self, request):
        user = self.request.user
        profile = Employee_Services.objects.filter(employee_profile=user)
        serializer = showallServiceSerializer(profile, many=True)
        return Response({'services': serializer.data}, status=HTTP_200_OK)
#######################################################################################################################
########################## Edit Service#########################################################################################

class EditService(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get_object(self, request):
        service_id = request.data.get("service_id")
        return Employee_Services.objects.get(Service_Id=service_id)

    def patch(self, request):
        testmodel_object = self.get_object(request)
        print(testmodel_object)
        print(request.data)
        serializer = EmployeeServiceUpdateSerializer(testmodel_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_200_OK, data=serializer.data)
        return Response({"error":(serializer.errors)},status=HTTP_400_BAD_REQUEST)
#################################################################################################################