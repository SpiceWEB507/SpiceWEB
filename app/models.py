from django.db import models


# contact page    
class contact_message(models.Model):
    name = models.CharField(max_length=35, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=60, null=False, blank=False)
    message = models.TextField()
    
    def __str__(self):
        return self.name