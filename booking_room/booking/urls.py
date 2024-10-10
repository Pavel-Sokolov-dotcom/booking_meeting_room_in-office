from django.urls import path
from .views import MeetingRoomList, BookingList, BookingReport
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('rooms/', MeetingRoomList.as_view(), name='meeting-room-list'),
    path('bookings/', BookingList.as_view(), name='booking_list'),
    path('report/', BookingReport.as_view(), name='booking_report'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
