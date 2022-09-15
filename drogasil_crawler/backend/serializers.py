from django.contrib.auth.models import User, Group
from rest_framework import serializers
from drogasil_crawler.backend.models import Productdata
from backend.models import Productdata

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productdata
        fields = ['all']