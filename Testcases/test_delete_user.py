import requests
import helpers


# call request
def call_request(user_id, is_valid_request):
    if is_valid_request:
        return requests.request('DELETE', helpers.base_url('/users/' + str(user_id)), headers=helpers.headers)
    else:
        return requests.request('DELETE', helpers.base_url('/usr/' + str(user_id)), headers=helpers.headers)


# test delete a user with id =3, then response is empty dictionary if success
def test_delete_by_user_id():
    user_id = 3
    response = call_request(user_id, True)
    response_json = response.json()

    assert response_json == {}, "The response data is not as expected. Expected: {}, Actual: {act}".format(
        act=response_json)


# test delete a user with id which is not existed in system, then response is empty dictionary
# check error status when sending a invalid request
def test_delete_invalid_by_user_id():
    user_id = 13
    response = call_request(user_id, True)
    status_code = response.status_code
    response_json = response.json()

    assert response_json == {}, "The response data is not as expected. Expected: {}, Actual: {act}".format(
        act=response_json)
    assert status_code == 404, "The returned error status code is not as expected. Expected: 404, Actual: {act}".format(
        act=status_code)


# test delete user with user_id = null
def test_delete_null_user_id():
    user_id = None
    response = call_request(user_id, True)
    status_code = response.status_code
    response_json = response.json()

    assert response_json == {}, "The response data is not as expected. Expected: {}, Actual: {act}".format(
        act=response_json)
    assert status_code == 404, "The returned error status code is not as expected. Expected: 404, Actual: {act}".format(
        act=status_code)


# test delete user with user_id = text
def test_delete_user_id_text():
    user_id = 'test'
    response = call_request(user_id, True)
    status_code = response.status_code
    response_json = response.json()

    assert response_json == {}, "The response data is not as expected. Expected: {}, Actual: {act}".format(
        act=response_json)
    assert status_code == 404, "The returned error status code is not as expected. Expected: 404, Actual: {act}".format(
        act=status_code)


# check returned status code with value = 200
def test_status_code():
    user_id = 1
    response = call_request(user_id, True)
    statuscode = response.status_code

    assert statuscode == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=statuscode)


# check returned error status code with value != 200
def test_error_status():
    user_id = 1
    response = call_request(user_id, False)
    statuscode = response.status_code

    if statuscode != 200:
        assert statuscode != 200, "The returned error status is not as expected. Expected: Not 200, Actual: {act}".format(
            act=statuscode)
    else:
        {}
