from django.contrib import admin
from app.models import contact_message
# Register your models here.
class saveEnquiryAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'subject', 'message']
    
admin.site.register(contact_message,saveEnquiryAdmin)

