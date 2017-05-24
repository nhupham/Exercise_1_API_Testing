import requests
import helpers
import pytest


# call request for (id, email, username)
def call_request(user_id, email, username, is_valid_request):
    if is_valid_request:
        if user_id != None:
            return requests.request('GET', helpers.base_url('/users?id=' + str(user_id)))
        if email != None:
            return requests.request('GET', helpers.base_url('/users?email=' + str(email)))
        if username != None:
            return requests.request('GET', helpers.base_url('/users?username=' + str(username)))
    else:
        if user_id != None:
            return requests.request('GET', helpers.base_url('/usrid' + str(id)))
        if email != None:
            return requests.request('GET', helpers.base_url('/usrmail' + str(email)))
        if username != None:
            return requests.request('GET', helpers.base_url('/usrna' + str(username)))


@pytest.fixture(scope="module")
def find_user():
    return ['id', 'email', 'username']
# test find user with valid id
def test_find_user(find_user):
    request_user_id = 1
    id_response = call_request(request_user_id, None, None, True)
    assert isinstance(id_response.json()[0], dict), "Information of user with id = 1: {act}".format(
        id_response.json()[0])
    print ("Information of user with id = 1" + str(id_response.json()[0]))
    assert id_response.json()[0]['id'] == 1, "The user ID is not as expected. Expected:{act1}, Actual: {act2}".format(
        act1=request_user_id, act2=id_response.json()[0]['id'])
    print (id_response.json()[0]['id'])
    assert set(find_user).issubset(
        id_response.json()[0].keys()), "Id, email, username keys should be in the response: {act}".format(
        id_response.json()[0].keys())
    print (id_response.json()[0].keys())


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("request_user_email", [('Shanna@melissa.tv'),])
# find user by valid email
# then check returned status code by email with value = 200
def test_find_user_by_email(request_user_email):
    email_response = call_request(None, request_user_email, None, True)
    response_user_email = email_response.json()[0][helpers.key_email]
    assert response_user_email == request_user_email, "The user email is not as expected. Expected: {act1}, Actual: {act2}".format(
        act1=request_user_email, act2=response_user_email)

    status_code = email_response.status_code

    assert status_code == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=status_code)


@pytest.mark.parametrize("request_username", [('Samantha'),
                                              ])
# find user by valid username
# then check returned status code by username with value = 200
def test_find_user_by_username_valid(request_username):
    username_response = call_request(None, None, request_username, True)
    assert username_response.json()[0][
               'username'] == request_username, "The user ID is not as expected. Expected:{act1}, Actual: {act2}".format(
        act1=request_username, act2=username_response.json()[0]['username'])
    print (username_response.json()[0]['username'])

    status_code = username_response.status_code

    assert status_code == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=status_code)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("request_user_id", [(11),
                                             (''),
                                             ('#$%&*&^%<>?'),
                                             ('test1'),
                                             ])
# Case 1: test find user with invalid id = 11, the Id is not existed in system
# Case 2: test find user with empty id
# Case 3: test find user with id is special characters with '#$%&*&^%<>?' characters
# Case 4: test find user with id is characters text with 'test1' text
def test_find_user_by_invalid_id(request_user_id):
    id_response = call_request(request_user_id, None, None, True)
    if len(id_response.json()) > 0:
        response_user_id = id_response.json()[0][helpers.key_id]
    else:
        response_user_id = []

    assert response_user_id != request_user_id, "The user ID is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_id)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("request_user_email", [('nhuptt@gmail.com'),
                                                (''),
                                                ('%$^&'),
                                                ('1234'),
                                                ])
# Case 1: find user by invalid email, the email is not existed in system (nhuptt@gmail.com)
# Case 2: find user by empty email
# Case 3: find user by special characters email ('%$^&')
# Case 4: find user by wrong format email with '1234'
def test_find_user_by_invalid_email(request_user_email):
    email_response = call_request(None, request_user_email, None, True)
    if len(email_response.json()) > 0:
        response_user_email = email_response.json()[0][helpers.key_email]
    else:
        response_user_email = []

    assert response_user_email != request_user_email, "The user email is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_email)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("request_username", [('NhuPTT'),
                                              (''),
                                              ('@#$!'),
                                              ])
# Case 1: find user by invalid username, the username is not existed in system
# Case 2: find user by empty username
# Case 3: find user by special_characters username
def test_find_user_by_invalid_username(request_username):
    username_response = call_request(None, None, request_username, True)
    if len(username_response.json()) > 0:
        response_username = username_response.json()[0][helpers.key_username]
    else:
        response_username = []

    assert response_username != request_username, "The username is not as expected. Expected: [], Actual: {act}".format(
        act=response_username)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("user_id", [(1), ])
# check returned status code by id with value = 200
def test_status_code_by_id(user_id):
    id_response = call_request(user_id, None, None, True)
    status_code = id_response.status_code

    assert status_code == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=status_code)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("user_id", [(12)])
# check returned error status code by id with value != 200
def test_error_status_code_by_id(user_id):
    id_response = call_request(user_id, None, None, False)
    status_code = id_response.status_code

    assert status_code != 200, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=status_code)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("username", [
    ('abc'),
])
# check returned error status code by username with value != 200
def test_error_status_code_by_username(username):
    username_response = call_request(None, None, username, False)
    status_code = username_response.status_code

    assert status_code != 200, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=status_code)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("user_email", [
    ('abc@gmail.com'),
])
# check returned error status code by email with value != 200
def test_error_status_code_by_email(user_email):
    email_response = call_request(None, user_email, None, False)
    status_code = email_response.status_code

    assert status_code != 200, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=status_code)
