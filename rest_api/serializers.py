# serializers.py in ipo_app

from rest_framework import serializers
from ipo_app.models import IPODetails

class IPODetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPODetails
        fields = '__all__'  # You can specify specific fields as needed
