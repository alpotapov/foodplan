from django.forms import widgets
from rest_framework import serializers
from user_profiles.models import User

class UserSerializer(serializers.Serializer):
    pk = serializers.Field()
    name = serializers.CharField(required=True, max_length=30)
    vegetarian = serializers.BooleanField(required=False, default=False)
    vegan = serializers.BooleanField(required=False, default=False)
    diabetes = serializers.BooleanField(required=False, default=False)
    lactose_intolerance = serializers.BooleanField(required=False, default=False)