from django.forms import widgets
from rest_framework import serializers
from main.models import Recipe

class RecipeSerializer(serializers.Serializer):
    pk = serializers.Field()
    name = serializers.CharField(required=True, max_length=255)
    image_url = serializers.CharField(required=True, max_length=255)
    prep_time_seconds = serializers.IntegerField(default=1200)
    price = serializers.DecimalField(required=True)
    is_vegetarian = serializers.BooleanField(required=False, default=False)
    is_lactose_intolerant = serializers.BooleanField(required=False, default=False)