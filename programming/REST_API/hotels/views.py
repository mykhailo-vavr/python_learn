from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.serializers import Serializer
from hotels.serializers import HotelDetailSerializer, HotelListSerializer
from hotels.models import Hotel
from hotels.permissions import isOwnerReadOnly
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class HotelCreateView(generics.CreateAPIView):
    serializer_class = HotelDetailSerializer

    def get_queryset(self, ):
        return Hotel.objects.all()

    def get(self, request, *args, **kwargs):
        hotels = self.get_queryset()
        serializer = self.serializer_class(hotels, many=True)
        return Response(serializer.data)


# class HotelListView(generics.ListAPIView):
#     serializer_class = HotelListSerializer
#     permission_classes = (IsAuthenticated, )
#     queryset = Hotel.objects.all()

# def get_queryset(self, ):
#     return Hotel.objects.all()

# def get(self, request, *args, **kwargs):
#     hotels = self.get_queryset()
#     serializer = self.serializer_class(hotels, many=True)
#     return Response(serializer.data)

# def post(self, request, *args, **kwargs):
#     hotel_data = request.data
#     print(hotel_data)
#     new_hotel = Hotel.objects.create(
#         user=hotel_data['user'],
#         booking_number=hotel_data['booking_number'],
#         checkin_datetime=hotel_data['checkin_datetime'],
#         checkout_datetime=hotel_data['checkout_datetime'],
#         price=hotel_data['price'],
#         city=hotel_data['city'],
#         guest_name=hotel_data['guest_name'],
#     )
#     new_hotel.save()
#     serializer = self.serializer_class(new_hotel)
#     return Response(serializer.data)
# def post(self, request, format=None):
#     return Response("ok")

# def get():
#     hotels = Hotel.objects.all()
#     serializer_class = HotelListSerializer(hotels, many=True)
#     return Response(serializer_class.data)

# def get_queryset(self):
#     """
#     Optionally restricts the returned purchases to a given user,
#     by filtering against a `username` query parameter in the URL.
#     """
#     queryset = Hotel.objects.all()
#     guest_name = self.request.query_params.get('guest_name')
#     if guest_name is not None:
#         queryset = queryset.filter(hotel__guest_name=guest_name)
#     return queryset


class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HotelDetailSerializer
    queryset = Hotel.objects.all()
    permission_classes = (IsAdminUser, )
