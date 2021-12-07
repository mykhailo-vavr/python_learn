from rest_framework import generics
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from hotels.serializers import HotelDetailSerializer, HotelListSerializer
from hotels.models import Hotel
from hotels.permissions import isOwnerReadOnly
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .services import PaginationHotels
from .types import STATUS_200
from .support_functions import stringify
from rest_framework.decorators import api_view
from rest_framework import status

# @api_view(['GET', 'POST'])
# def hotel_list(request, format=None):
#     if request.method == 'GET':
#         hotels = Hotel.objects.all()
#         serializer = HotelListSerializer(hotels, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = HotelDetailSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelCreateView(generics.CreateAPIView):
    serializer_class = HotelDetailSerializer
    paginator = PaginationHotels()

    def get_queryset(self):
        return Hotel.objects.all()

    def get(self, request, *args, **kwargs):
        hotels = self.get_queryset()
        serializer = self.serializer_class(
            hotels,
            many=True,
            context={'request': request},
        )
        page = self.paginator.paginate_queryset(serializer.data, request)
        return self.paginator.get_paginated_response(page)
        # return Response(serializer.data)

    # def post(self, request, format=None):
    # serializer = self.serializer_class(
    #     data=request.data,
    #     many=True,
    #     context={'request': request},
    # )
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response(
    #     stringify({
    #         'status': STATUS_200,
    #         'message': 'Customer has been successfully created.'
    #     }))

    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer):
    #     serializer.save(data=self.request.data)


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
