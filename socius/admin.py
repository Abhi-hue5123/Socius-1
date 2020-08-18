from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Destination
from .models import UserList,DirectoryCreation,DirectoryMembers
from import_export.admin import ImportExportModelAdmin 
# Register your models here.
admin.site.register(Destination)
admin.site.register(DirectoryCreation)
admin.site.register(UserList)
admin.site.register(DirectoryMembers)
class UserListAdmin(ImportExportModelAdmin):
    list_display = ('name','email','coupon')

