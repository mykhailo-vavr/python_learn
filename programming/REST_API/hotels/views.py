from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from hotels.serializers import HotelDetailSerializer, HotelListSerializer
from hotels.models import Hotel
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .services import PaginationHotels, ReadOnlyOrAdmin


class HotelView(generics.CreateAPIView, generics.ListAPIView):
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = [
        'id',
        'price',
        'booking_number',
        'price',
        'guest_name',
        'checkin_datetime',
        'checkout_datetime',
    ]
    ordering_fields = '__all__'

    def get_queryset(self):
        return Hotel.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated(), ReadOnlyOrAdmin()]
        elif self.request.method == 'POST':
            return (
                IsAuthenticated(),
                IsAdminUser(),
            )

    serializer_class = HotelListSerializer
    pagination_class = PaginationHotels


class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return (
                IsAuthenticated(),
                IsAdminUser(),
            )

    serializer_class = HotelDetailSerializer
    queryset = Hotel.objects.all()
