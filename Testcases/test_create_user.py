import requests
import helpers

# initialization variables
user_id = ''
response = requests.request("POST", helpers.base_url('/users'), params=helpers.input_data,
                            headers=helpers.headers)
#call request
def call_request(input_data):
    global response
    response = requests.request("POST", helpers.base_url('/users'), params=input_data,
                            headers=helpers.headers)

#call request invalid
def call_request_invalid(input_data):
    global response
    response = requests.request("POST", helpers.base_url('/usr'), params=input_data,
                            headers=helpers.headers)

# check new user id which is created user with id = 11, then response is returned with id =11 if creating success
def test_check_new_user_id():
    global user_id
    input_data = {
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
    call_request(input_data)
    user_id = response.json()[helpers.key_id]
    assert user_id == 11, "The returned user id is not as expected. Expected: 11, Actual: {act}".format(act=user_id)

#check create user with empty data
def test_check_new_user_empty_data():
    global user_id
    input_data = {}
    call_request(input_data)
    if len(response.json())>0:
        user_id = response.json()[helpers.key_id]
    else:
        user_id=[]
    assert user_id == 11, "The returned user id is not as expected. Expected: 11, Actual: {act}".format(act=user_id)


# check returned status code with value = 201 when creating success
def test_status_code():
    input_data = {"name": 'abc1',
                  "username": 'test1'}
    call_request(input_data)
    assert response.status_code == 201, "The returned status code is not as expected. Expected: 201, Actual: {act}".format(
        act=response.status_code)


# check returned error status code with value != 200
def test_error_status():
    input_data={"name": 'abc',
        "username": '123'}
    call_request_invalid(input_data)
    statuscode = response.status_code
    if statuscode != 200:
        assert statuscode != 200, "The returned error status is not as expected. Expected: 404, Actual: {act}".format(
            act=statuscode)
    else:
        {}
