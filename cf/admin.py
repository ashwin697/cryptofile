from django.contrib import admin
from .models import Contact,EncryptedPath ,DecryptedPath 

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','desc')

class DecryptedAdmin(admin.ModelAdmin):
    list_display = ('user','fpath','password','ddate','dfilename')

class EncryptedAdmin(admin.ModelAdmin):
    list_display = ('user','fpath','password','edate','efilename')

admin.site.register(Contact , ContactAdmin)

admin.site.register(DecryptedPath , DecryptedAdmin)
admin.site.register(EncryptedPath , EncryptedAdmin)
