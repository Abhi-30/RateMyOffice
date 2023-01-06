from django.contrib import admin

# Register your models here.
from . models import Employee_Profile,Employee_Role,Employee_Services

admin.site.register(Employee_Profile)
admin.site.register(Employee_Role)
admin.site.register(Employee_Services)