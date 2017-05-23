import requests
import helpers


# call request
def call_request(input_data, is_valid_request):
    if is_valid_request:
        return requests.request("POST", helpers.base_url('/users'), params=input_data,
                                headers=helpers.headers)
    else:
        return requests.request("POST", helpers.base_url('/usr'), params=input_data,
                                headers=helpers.headers)


# check new user id which is created user with id = 11, then response is returned with id = 11 if creating success
def test_check_new_user_id():
    user_data = {
        "name": 'Nhu',
        "username": 'NhuPTT',
        "email": 'nhuptt@gmail.com',
        "address": {
            "street": 'Nguyen Van Troi',
            "suite": '786',
            "city": 'Ho Chi Minh',
            "zipcode": '70000',
            "geo": {
                "lat": '-90',
                "lng": '67.9'
            }
        },
        "phone": '097 864 9248',
        "website": 'nhuptt.org',
        "company": {
            "name": 'IT company',
            "catchPhrase": 'Multi-layered',
            "bs": 'Test'
        }
    }
    response = call_request(user_data, True)
    user_id = response.json()[helpers.key_id]
    request_id = 11
    assert user_id == request_id, "The returned user id is not as expected. Expected: {act1}, Actual: {act2}".format(
        act1=user_id, act2=user_id)


# check new user id which is created user with id = 11 and data input = special characters, then response is returned with id = 11 if creating success
def test_check_new_user_special_data():
    user_data = {
        "name": '&%$',
        "username": '*()0',
        "email": '#$%',
    }
    response = call_request(user_data, True)
    user_id = response.json()[helpers.key_id]
    request_id = 11
    assert user_id == request_id, "The returned user id is not as expected. Expected: {act1}, Actual: {act2}".format(
        act1=user_id, act2=user_id)


# check create user with user is empty data
def test_check_new_user_empty_data():
    input_data = {}
    request_id = 11
    response = call_request(input_data, True)
    if len(response.json()) > 0:
        user_id = response.json()[helpers.key_id]
    else:
        user_id = []
    assert user_id == request_id, "The returned user id is not as expected. Expected: {act1}, Actual: {act2}".format(
        act1=user_id, act2=user_id)


# check returned status code with value = 201 when creating success
def test_success_status_code():
    input_data = {"name": 'abc1',
                  "username": 'test1'}
    response = call_request(input_data, True)
    assert response.status_code == 201, "The returned status code is not as expected. Expected: 201, Actual: {act}".format(
        act=response.status_code)


# check returned error status code with value != 200
def test_error_status_code():
    input_data = {"name": 'abc',
                  "username": '123'}
    response = call_request(input_data, False)
    statuscode = response.status_code
    if statuscode != 200:
        assert statuscode != 200, "The returned error status is not as expected. Expected: Not 200, Actual: {act}".format(
            act=statuscode)
