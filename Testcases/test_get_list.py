import requests
import helpers
import pytest


@pytest.fixture(scope="module")
# call request
def call_request(is_valid_request):
    if is_valid_request:
        return requests.request('GET', helpers.base_url('/users/'))
    else:
        return requests.request('GET', helpers.base_url('/usr/'))


# check the returned status code with value = 200
def test_status_code():
    response = call_request(True)
    status_code = response.status_code

    assert status_code == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=status_code)


# check the returned error status code with value != 200
def test_error_status_code():
    response = call_request(False)
    status_code = response.status_code

    assert status_code != 200, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=statuscode)


# check get a valid username from users list
def test_check_get_valid_username():
    valid_username = 'Antonette'
    response = call_request(True)
    response_username = response.json()[1][helpers.key_username]

    assert response_username == valid_username, "The returned username is not as expected. Expected:{act1}, Actual: {act2}".format(
        act1=valid_username, act2=response_username)


# check a username is not exsited from users list
def test_check_get_invalid_username():
    invalid_username = 'nhuptt'
    response = call_request(True)
    if len(response.json()) > 0:
        response_username = response.json()[0][helpers.key_username]
    else:
        response_username = []

    assert response_username != invalid_username, "The returned username is not as expected. Expected:[], Actual: {act}".format(
        act=response_username)


# check a username is empty
def test_check_get_empty_username():
    empty_username = ''
    response = call_request(True)
    if len(response.json()) > 0:
        response_username = response.json()[0][helpers.key_username]
    else:
        response_username = []

    assert response_username != empty_username, "The empty username is not as expected. Expected:[], Actual: {act}".format(
        act=response_username)


# check a username is special characters
def test_check_get_empty_username():
    empty_username = '@#$%^&'
    response = call_request(True)
    if len(response.json()) > 0:
        response_username = response.json()[0][helpers.key_username]
    else:
        response_username = []

    assert response_username != empty_username, "The empty username is not as expected. Expected:[], Actual: {act}".format(
        act=response_username)


# count users from users list
def test_get_users_count():
    check_user_count = 10
    response = call_request(True)
    response_user_count = len(response.json())

    assert response_user_count == check_user_count, "The returned list user's number is not as expected. Expected:{act1}, Actual: {act2}".format(
        act1=check_user_count, act2=response_user_count)
