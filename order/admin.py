from django.contrib import admin
from .models import Userinformation
# Register your models here.
@admin.register(Userinformation)

class UserinformationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'first_name', 'last_name', 'email_id', 'phone_no', 'address', 'location', 'cake' , 'quantity']
#'quantity',