from django.db import models
from django.contrib.auth.models import User


class MeetingRoom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Booking(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE) # номер переговорной комнаты
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Связь с моделью User
    start_time = models.DateTimeField() 
    end_time = models.DateTimeField()
    purpose = models.TextField() # цель бронирования
    
    def __str__(self):
        return f"Пользователь {self.user.username} забронировал {self.room} с {self.start_time} до {self.end_time}"
    
    
