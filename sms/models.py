from django.db import models

# Create your models here.

class SmsFile(models.Model):
    sms_file = models.FileField(upload_to='sms/')
    body_message = models.CharField(max_length=1000)