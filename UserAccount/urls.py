
from django.contrib import admin
from django.urls import path,re_path,include
from .views import RegisterUserAPIView,EmployeeLogin,ChangePasswordView,EmployeeUpdate,Logout,getEmployee,getEmployeeRole,getAllemployee,VerifyOTP,AddServices,Showallservices,ShowService,EditService,RegisterServiceProviderAPIView
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic import TemplateView

 
#from user.api.viewsets import userviewsets
#from rest_framework import routers
 
#router = routers.DefaultRouter()
#router.register('user', userviewsets, base_name ='user_api')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('register/',RegisterUserAPIView.as_view()),
    path('verify/', VerifyOTP.as_view(), name='Verify User API'),
    path('login/', EmployeeLogin.as_view(), name='Login API'),
    path('logout/', Logout.as_view(), name='Logout API'),
    path('updateregister/',EmployeeUpdate.as_view(), name='Update User Details'),
    path('forgotpassword/', ChangePasswordView.as_view(), name='Change User Password'),
    path('getemployee/', getEmployee.as_view(), name='get Current Employee Details'),
    path('getallemployee/', getAllemployee.as_view(), name='get all Employee Details'),
    path('getemployeerole/',getEmployeeRole.as_view(), name='get all Employee Roles'),
   # re_path('api/register-by-access-token/' + r'social/(?P<backend>[^/]+)/$',registers_by_access_token.as_view(), name='RegisterByAccessToken'),
   # path('api/authentication-test/', authentications_test.as_view(), name='AuthenticationTest'),
   # path('home',TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('accounts/', include('allauth.urls')),
    
    path('serviceprovider_register/',RegisterServiceProviderAPIView.as_view(), name='Register Service Provider'),
    
    path('addservice/',AddServices.as_view(), name='Add Service'),
    path('showallservices/',Showallservices.as_view(), name='Show All Services'),
    path('showservice/',ShowService.as_view(), name='Show Service'),
    path('editservice/',EditService.as_view(), name='Edit Service'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)