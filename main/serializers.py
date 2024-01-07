from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ("id", "name", "ingredients", "picture", "difficulty", "prep_time", "prep_guide", "tags")