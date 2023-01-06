from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
#from django.conf import settings
#User = settings.AUTH_USER_MODEL

#import uuid
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

from django.core.validators import RegexValidator

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, employee_email, password=None,*args,**kwargs):
        """create a new user profile"""

        if not employee_email:
            raise ValueError("user most have an email address")
        employee_email = self.normalize_email(employee_email)
        user = self.model(employee_email=employee_email,)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, employee_email, password):
        """create and save new super user with given dertails"""
        user = self.create_user(employee_email, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
USER_ROLE = (
    #('User', 'User'),
    #('Admin','Admin'),
    ('Service_Provider','Service_Provider'),
    ('Officer','Officer'),
)

NO_OF_EMPLOYEE = ( 
                  ('0-10','0-10'),
                  ('10-50','10-50'),
                  ('50-250','50-250'),
                  ('250-500','250-500'),
                  ('500-1000','500-1000'),
)

class Employee_Role(models.Model):
   # role_id = models.AutoField(primary_key=True,editable=False)
    emp_type = models.CharField(primary_key=True,max_length=200,null=False,blank=False)
    user_type1=models.CharField(max_length=20, choices=USER_ROLE,default='User')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.emp_type)

#abc
class Employee_Profile(AbstractBaseUser,PermissionsMixin):
    #phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    #models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    emp_id = models.AutoField(primary_key=True,editable=False)
    #employee_photo = models.ImageField(upload_to="employee_photo", default='media/employee_photo/defaultimage.jpg')
    employee_role=models.ForeignKey(Employee_Role,null=True,blank=True,on_delete=models.PROTECT)
    user_type=models.CharField(max_length=20, choices=USER_ROLE)
    employee_email=models.EmailField(max_length=200,null=True,blank=True,unique=True)
    employee_firstname=models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)
    
    # Company details fields
    serviceprovider_name = models.CharField(max_length=100,null=True,blank=True)
    website = models.CharField(max_length=100,null=True,blank=True)
    No_of_employees = models.CharField(max_length=100,choices=NO_OF_EMPLOYEE,null=True,blank=True)
    founding_year = models.CharField(max_length=100,null=True,blank=True)
    tagline = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=200,null=True,blank=True)
    Logo = models.ImageField(upload_to="Company", default='media/Company/defaultimage.jpg')
    video_links = models.CharField(max_length=200,null=True,blank=True)
    Contact_phone = models.CharField(max_length=100,null=True,blank=True)
    
    # Location details fields
    Country = models.CharField(max_length=100,null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    City = models.CharField(max_length=100,null=True,blank=True)
    Zipcode = models.CharField(max_length=100,null=True,blank=True)
    phone_no = models.CharField(max_length=100,null=True,blank=True)
    
    #Approved by administrator
    approved_by_admin = models.BooleanField(default=False)
    approved_by_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_active=models.BooleanField(default=True,null=True) 
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False,blank=True)
    is_staff = models.BooleanField(default=True)
    is_officer = models.BooleanField(default=False)
    is_service_provider = models.BooleanField(default=False)
    
    
    #Social media links ----------
    LinkedIn = models.CharField(max_length=100,null=True,blank=True)
    facebook = models.CharField(max_length=100,null=True,blank=True)
    certificate = models.ImageField(upload_to='images/',null=True,blank=True)
    reviews=models.CharField(max_length=100,null=True,blank=True)
    
    
    # Foreign keys 
    
    
    
   # employee_lastname=models.CharField(max_length=100,null=True,blank=True)
   # employee_officephoneno=models.CharField(max_length=100,null=True,blank=True)
   # employee_mobileno=models.CharField(max_length=100,null=True,blank=True)
    #employee_rfid=models.CharField(max_length=100,null=True,blank=True)
   # employee_country=models.CharField(max_length=100,null=True,blank=True)
    #employee_province=models.CharField(max_length=100,null=True,blank=True)
   # employee_city=models.CharField(max_length=100,null=True,blank=True)
   # employee_district=models.CharField(max_length=100,null=True,blank=True)
   # employee_subdistrict=models.CharField(max_length=100,null=True,blank=True)
   # employee_street=models.CharField(max_length=100,null=True,blank=True)
   # employee_unitno=models.CharField(max_length=100,null=True,blank=True)
   # employee_zipcode=models.CharField(max_length=100,null=True,blank=True)
    #employee_ok_name=models.CharField(max_length=100,null=True,blank=True)
    #employee_nok_contactno=models.CharField(max_length=100,null=True,blank=True)
    #employee_nok_email=models.CharField(max_length=100,null=True,blank=True)
   # created_at=models.DateTimeField(auto_now_add=True, null=True)
   # created_by=models.CharField(max_length=100,null=True,blank=True)
   # updated_at=models.DateTimeField(auto_now_add=True,null=True)
   # updated_by=models.CharField(max_length=100,null=True,blank=True)
   
   # isdeleted=models.BooleanField(default=False,null=True)
    
    otp = models.CharField(max_length=6, null=True, blank=True)
   # is_active = models.BooleanField(default=True)
    #Partner_Govt_Id=models.CharField(max_length=100,null=True,blank=True)
    #Partner_No_Of_Deposits=models.CharField(max_length=100,null=True,blank=True)
    #Partner_QRCode=models.CharField(max_length=100,null=True,blank=True)
    #Partner_DOB=models.CharField(max_length=100,null=True,blank=True)
    #Partner_Gender=models.CharField(max_length=100,null=True,blank=True)
   
    mach_address = models.CharField(max_length=200,null=True,blank=True)
    ip_address = models.CharField(max_length=200,null=True,blank=True)
    objects = UserProfileManager()
    USERNAME_FIELD = 'employee_email'
    
    def __str__(self):
        return str(self.employee_email)
    
   # def company_photo(instance, filename):
    #    return 'images/{filename}'.format(filename=filename)
    
class Employee_Services(models.Model):
    Service_Id=models.AutoField(primary_key=True,editable=False)
    Service_Name=models.CharField(max_length=100,null=True,blank=True)
    Service_Description=models.CharField(max_length=100,null=True,blank=True)
    Service_Type=models.CharField(max_length=100,null=True,blank=True)
    employee_profile = models.ForeignKey(Employee_Profile, on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    created_by=models.CharField(max_length=100,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_by=models.CharField(max_length=100,null=True,blank=True)
    is_active = models.BooleanField(default=True)
   
    