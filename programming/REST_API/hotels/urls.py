from django.urls import path
from hotels.views import *

app_name = 'hotel'
urlpatterns = [
    # path('hotels/', HotelListView.as_view()),
    path('hotels/', HotelCreateView.as_view()),
    # path('hotels/<int:pk>/', HotelDetailView.as_view()),
]
