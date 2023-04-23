import pprint
import requests
import pytest

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'
STATUS_OK = 200


# POST authorization
@pytest.fixture(scope='module')
def auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(AUTH_URL, json=payload)
    assert response.status_code == STATUS_OK, \
        'Wrong status code'

    assert 'token' in response.json(), \
        'No token found'

    token = response.json().get('token')
    print(f'\n{token}')

    yield token


# POST new booking
@pytest.fixture(scope='module')
def booking_id():
    # загружаемые данные
    payload = {
        "firstname": "Ilosha",
        "lastname": "Test",
        "totalprice": 550,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-01-06",
            "checkout": "2023-01-12"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == STATUS_OK, \
        'Wrong status code'

    pprint.pprint(response.json())
    new_booking_id = response.json().get('bookingid')
    print(f'New booking id = {new_booking_id}')

    yield new_booking_id


# GET all bookings
def test_get_all_bookings():
    response = requests.get({BASE_URL})  # обращаемся к ендпоинту
    print(f'\nThe quantity of bookings: {len(response.json())}')  # количество записей (букингов)

    assert response.status_code == STATUS_OK, \
        'Wrong status code'

    print(f'Status code: {response.status_code}')
    pprint.pprint(response.json())  # увидеть тело ответа красивое
    print(response.headers)

    # проверка на присутствие какого-то элемента в header, например
    # headers это словарь, соответственно проходимся по items и ищем пару внутри

    header = ('Connection', 'keep-alive')
    assert header in response.headers.items(), \
        f'No such header found: {header}'


# GET special booking by id
def test_get_booking_with_id():
    response = requests.get(f'{BASE_URL}/2')
    pprint.pprint(response.json())

    #assert response.json()['firstname'] == 'Jim', \
        #'Firstname is wrong'

    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']

    for key in expected_keys:
        assert key in response.json().keys(), \
            f'No expected key found: {key}'


# POST find created booking (booking create is in the booking_id fixture function)
def test_create_booking(booking_id):
    response = requests.get(f'{BASE_URL}/{booking_id}')
    assert response.status_code == STATUS_OK, \
        'Wrong status code'
    assert response.json().get('firstname') == 'Ilosha', \
        'Wring [firstname] parameter'


# PUT update booking

def test_update_booking(booking_id, auth_token):
    payload = {
        "firstname": "Ilosha",
        "lastname": "Test",
        "totalprice": 785,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-01-06",
            "checkout": "2023-01-12"
        },
        "additionalneeds": "Lunch"
    }

    header = {'Cookie': f'token={auth_token}'}
    response = requests.put(f'{BASE_URL}/{booking_id}', json=payload, headers=header)
    assert response.status_code == STATUS_OK, \
        'Wrong status code'

    response_get = requests.get(f'{BASE_URL}/{booking_id}')
    assert response_get.status_code == STATUS_OK, \
        'Wrong status code'

    assert payload.get('totalprice') == response_get.json().get('totalprice'), \
        'Wrong update info displayed'

    assert payload.get('additionalneeds') == response_get.json().get('additionalneeds'), \
        'Wrong update info displayed'


# DELETE delete booking
def test_delete_booking(booking_id, auth_token):
    header = {'Cookie': f'token={auth_token}'}
    response = requests.delete(f'{BASE_URL}/{booking_id}', headers=header)

    assert response.status_code == 201, \
        'Wrong status code'

    # проверяем, что запись удалилась по статус коду
    response_get = requests.get(f'{BASE_URL}/{booking_id}')
    assert response_get.status_code == 404, \
        'Wrong status code'


# PATCH update booking
def test_update_booking_patch(booking_id, auth_token):
    payload = {
        "bookingdates": {
            "checkin": "2023-02-07",
            "checkout": "2023-02-14"
        }
    }

    header = {'Cookie': f'token={auth_token}'}

    response = requests.patch(f'{BASE_URL}/{booking_id}', json=payload, headers=header)
    pprint.pprint(response.json())

    assert response.status_code == STATUS_OK, \
        'Wrong status code'

    assert payload.get('bookingdates')['checkin'] == response.json().get('bookingdates')['checkin'], \
        f'Wrong checkin date found: {response.json().get("bookingdates")["checkin"]}'

    assert payload.get('bookingdates')['checkout'] == response.json().get('bookingdates')['checkout'], \
        f'Wrong checkout date found: {response.json().get("bookingdates")["checkout"]}'

















