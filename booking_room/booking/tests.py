import requests
import pytest

# URL для получения токена
TOKEN_URL = "http://127.0.0.1:8000/api/token/"
# URL для бронирования
BOOKING_URL = "http://127.0.0.1:8000/api/bookings/"
# URL для получения бронирований
GET_BOOKING = "http://127.0.0.1:8000/api/bookings/"


@pytest.fixture
def get_access_token():
    # Данные для входа пользователя
    login_data = {
        "username": "user3",
        "password": "password3"
    }
    
    # Получаем токен
    response = requests.post(TOKEN_URL, json=login_data)
    response.raise_for_status()  # Генерирует исключение для статус-кодов 4xx/5xx
    tokens = response.json()
    return tokens['access']

def test_booking_room(get_access_token):
    # Данные для бронирования
    booking_data = {
        "room": 3,
        "start_time": "2024-10-26T10:00:00Z",  # Время в UTC
        "end_time": "2024-10-26T10:00:00Z",    # Время в UTC
        "purpose": "Обсуждение 7877"
    }

    headers = {
        "Authorization": f"Bearer {get_access_token}"
    }
    
    # Отправка запроса на бронирование
    booking_response = requests.post(BOOKING_URL, json=booking_data, headers=headers)
    
    # Проверка результата
    assert booking_response.status_code == 201, f"Ошибка при создании бронирования: {booking_response.json()}"
    print("Бронирование успешно создано:", booking_response.json())
    
    
def test_get_booking_room(get_access_token):
    headers = {
        "Authorization": f"Bearer {get_access_token}"
    }
    
    # Отправка запроса на бронирование
    booking_response = requests.get(GET_BOOKING, headers=headers)
    
    # Проверка результата
    assert booking_response.status_code == 200, f"Ошибка при создании бронирования: {booking_response.json()}"
    print("Бронирование успешно создано:", booking_response.json())

