from rest_framework import serializers
from hotels.models import Hotel


class HotelListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Hotel
        fields = '__all__'


class HotelDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Hotel
        fields = '__all__'