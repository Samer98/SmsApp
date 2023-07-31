from rest_framework import serializers
from .models import SmsFile
class SmsFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsFile
        fields = ['id', 'sms_file','body_message']