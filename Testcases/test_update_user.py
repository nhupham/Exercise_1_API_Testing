import requests
import helpers

# initialization variables
response = requests.request("PUT", helpers.base_url('/users/' + str(helpers.id)), params=helpers.input_data,
                            headers=helpers.headers)


# call request
def call_request(id, input_data):
    global response
    response = requests.request("PUT", helpers.base_url('/users/' + str(id)), params=input_data,
                                headers=helpers.headers)


# call request invalid
def call_request_invalid(id, input_data):
    global response
    response = requests.request("PUT", helpers.base_url('/usr/' + str(id)), params=input_data,
                                headers=helpers.headers)


# check user for update that user has had id = 2, then response is returned with id =2 if updating success
def test_check_updated_user_id():
    input_data = {
        "name": 'Van',
        "username": 'VanPTT',
        "email": 'vanptt@gmail.com',
        "address": {
            "street": 'Cong Hoa',
            "suite": '796',
            "city": 'Ho Chi Minh',
            "zipcode": '70000',
            "geo": {
                "lat": '-90',
                "lng": '67.9'
            }
        },
        "phone": '097 874 9248',
        "website": 'vanptt.org',
        "company": {
            "name": 'Marketing company',
            "catchPhrase": 'Multi-layered',
            "bs": 'Test'
        }
    }
    request_user_id = 2
    call_request(request_user_id, input_data)
    response_user_id = response.json()[helpers.key_id]
    assert response_user_id == request_user_id, "The returned user id is not as expected. Expected: {act1}, Actual: {act2}".format(
        act1=request_user_id, act2=response_user_id)


# check update for user have id that is not existed in system, then response is returned with empty dictionary
# check error status when sending a invalid request
def test_check_updated_invalid_user_id():
    input_data = {
        "name": 'Hoa',
        "username": 'HoaLP',
        "email": 'hoa@gmail.com',
    }
    request_user_id = 17
    call_request(request_user_id, input_data)
    statuscode = response.status_code
    response_user_id = {}
    assert response_user_id != request_user_id, "The returned user id is not as expected. Expected: {act1}, Actual: {act2}".format(
        act1=request_user_id, act2=response_user_id)
    assert statuscode == 404, "The returned error status code is not as expected. Expected: 404, Actual: {act}".format(
        act=statuscode)

# check returned status code with value = 200
def test_status_code():
    input_data = {"name": 'abc1',
                  "username": 'test1'}
    call_request(3, input_data)
    assert response.status_code == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=response.status_code)


# check returned error status code with value = 404
def test_error_status():
    input_data = {"name": 'abc3',
                  "username": 'usertest1'}
    call_request_invalid(6, input_data)
    statuscode = response.status_code
    if statuscode != 200:
        assert statuscode != 200, "The returned error status is not as expected. Expected: Not 200, Actual: {act}".format(
            act=statuscode)
    else:
        {}
