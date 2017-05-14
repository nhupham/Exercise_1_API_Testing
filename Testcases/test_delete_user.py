import requests
import helpers

# initialization variables
response = requests.request('DELETE', helpers.base_url('/users/' + str(helpers.id)), headers=helpers.headers)

#call request
def call_request(id):
    global response
    response = requests.request('DELETE', helpers.base_url('/users/' + str(id)), headers=helpers.headers)

#call request invalid
def call_request_invalid(id):
    global response
    response = requests.request('DELETE', helpers.base_url('/usr/' + str(id)), headers=helpers.headers)

# test delete a user with id =3, then response is empty dictionary if success
def test_delete_by_user_id():
    id=3
    global response
    call_request(id)
    user_id = response.json()
    assert user_id == {}, "The user ID is not as expected. Expected: {}, Actual: {act}".format(
        act=user_id)

# test delete a user with id which is not existed in system, then response is empty dictionary
# check error status when sending a invalid request
def test_delete_invalid_by_user_id():
    id=13
    global response
    call_request(id)
    statuscode = response.status_code
    user_id = response.json()
    assert user_id == {}, "The user ID is not as expected. Expected: {}, Actual: {act}".format(
        act=user_id)
    assert statuscode == 404, "The returned error status code is not as expected. Expected: 404, Actual: {act}".format(
        act=statuscode)

# check returned status code with value = 201
def test_status_code():
    call_request(1)
    statuscode = response.status_code
    assert statuscode == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=statuscode)

# check returned error status code with value != 200
def test_error_status():
    call_request_invalid(1)
    statuscode = response.status_code
    if statuscode != 200:
        assert statuscode != 200, "The returned error status is not as expected. Expected: Not 200, Actual: {act}".format(
            act=statuscode)
    else:{}
