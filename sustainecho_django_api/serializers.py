from rest_framework import serializers
from .models import City, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_name', 'employee_count']


class CitySerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['city_name', 'brands']

    def create(self, validated_data):
        brands_data = validated_data.pop('brands')
        city = City.objects.create(**validated_data)
        for brand_data in brands_data:
            Brand.objects.create(city=city, **brand_data)
        return city
