import requests
import helpers
import pytest


# call request
def call_request(is_valid_request):
    if is_valid_request:
        return requests.request('GET', helpers.base_url('/users/'))
    else:
        return requests.request('GET', helpers.base_url('/usr/'))


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("valid_username", [('Antonette'),
                                            ])
# check get a valid username from users list
def test_check_get_valid_username(valid_username):
    response = call_request(True)
    response_username = response.json()[1][helpers.key_username]

    assert response_username == valid_username, "The returned username is not as expected. Expected:{act1}, Actual: {act2}".format(
        act1=valid_username, act2=response_username)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("invalid_username", [
    ('nhuptt'),
    (''),
    ('@#$%^&'),
])
# Case 1: check a username (nhuptt) is not exsited from users list
# Case 2: check a username ('') is null
# Case 3: check a username ('@#$%^&') is special characters
def test_check_get_invalid_username(invalid_username):
    response = call_request(True)
    if len(response.json()) > 0:
        response_username = response.json()[0][helpers.key_username]
    else:
        response_username = []
    assert response_username != invalid_username, "The returned username is not as expected. Expected:[], Actual: {act}".format(
        act=response_username)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("check_user_count", [(10), ])
# count users from users list
def test_get_users_count(check_user_count):
    response = call_request(True)
    response_user_count = len(response.json())
    assert response_user_count == check_user_count, "The returned list user's number is not as expected. Expected:{act1}, Actual: {act2}".format(
        act1=check_user_count, act2=response_user_count)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("status_Code", [(200)])
# check the returned status code with value = 200
def test_status_code(status_Code):
    response = call_request(True)
    assert response.status_code == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=status_Code)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("status_Code", [(200)])
# check the returned error status code with value != 200
def test_error_status_code(status_Code):
    response = call_request(False)
    assert response.status_code != status_Code, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=status_Code)
