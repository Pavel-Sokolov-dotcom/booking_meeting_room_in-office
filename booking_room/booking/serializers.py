from rest_framework import serializers
from .models import MeetingRoom, Booking


class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = '__all__'
        
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['room', 'start_time', 'end_time', 'purpose']

    def validate(self, data):
        room = data['room']
        start_time = data['start_time']
        end_time = data['end_time']

        if Booking.objects.filter(room=room, 
                                   start_time__lt=end_time, 
                                   end_time__gt=start_time).exists():
            raise serializers.ValidationError("Переговорка уже забронирована на это время.")

        return data