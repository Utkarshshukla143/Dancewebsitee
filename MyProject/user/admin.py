from django.contrib import admin

# Register your models here.
from .models import *

class contactAdmin(admin.ModelAdmin):
    list_display=("name","contact","email","message")
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=('id',"cname","cpic","cdate")
admin.site.register(category,categoryAdmin)

class profileAdmin(admin.ModelAdmin):
    list_display=("name","mobile","email","passwd","ppic","address")
admin.site.register(profile,profileAdmin)

class signupAdmin(admin.ModelAdmin):
    list_display=("name","dob","mobile","email","password","profession","college","profile",)
admin.site.register(signup,signupAdmin)


class blogdetailAdmin(admin.ModelAdmin):
    list_display=("authorid","blogcategory","title","description","attechment","thumbnail","blogdate")
admin.site.register(blogdetail,blogdetailAdmin)

class createblogsAdmin(admin.ModelAdmin):
    list_display=("topic","discription","document","thumbnail")
admin.site.register(createblogs,createblogsAdmin)