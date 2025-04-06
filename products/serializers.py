import requests
from django.core.files.base import ContentFile
from rest_framework import serializers
import os

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category']

    def to_internal_value(self, data):
        # If image is sent as a URL string in JSON, download and convert it
        image_url = data.get('image')

        if isinstance(image_url, str) and image_url.startswith('http'):
            try:
                response = requests.get(image_url)
                if response.status_code != 200:
                    raise serializers.ValidationError({"image": "Could not download image from URL."})
                
                filename = os.path.basename(image_url)
                data['image'] = ContentFile(response.content, name=filename)
            except Exception:
                raise serializers.ValidationError({"image": "Invalid URL or download failed."})

        return super().to_internal_value(data)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
