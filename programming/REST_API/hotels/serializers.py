from rest_framework import serializers
from hotels.models import Hotel


class HotelListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        if data['checkin_datetime'] > data['checkout_datetime']:
            raise serializers.ValidationError(
                "Checkin date should be earlier than checkout date")
        return data

    class Meta:
        model = Hotel
        fields = '__all__'


class HotelDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        if data['checkin_datetime'] > data['checkout_datetime']:
            raise serializers.ValidationError(
                "Checkin date should be earlier than checkout date")
        return data

    class Meta:
        model = Hotel
        fields = '__all__'
