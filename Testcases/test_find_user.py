import requests
import helpers
import pytest


@pytest.fixture(scope="module")
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

# test find user with valid id
def test_find_user_by_id():
    request_user_id = 1
    id_response = call_request(request_user_id, None, None, True)
    response_user_id = id_response.json()[0][helpers.key_id]

    assert response_user_id == request_user_id, "The user ID is not as expected. Expected:{act1}, Actual: {act2}".format(
        act1=request_user_id, act2=response_user_id)


# find user by valid email
def test_find_user_by_email():
    request_user_email = 'Shanna@melissa.tv'
    email_response = call_request(None, request_user_email, None, True)
    response_user_email = email_response.json()[0][helpers.key_email]

    assert response_user_email == request_user_email, "The user email is not as expected. Expected: {act1}, Actual: {act2}".format(
        act1=request_user_email, act2=response_user_email)


# find user by valid username
def test_find_user_by_username():
    request_username = 'Samantha'
    username_response = call_request(None, None, request_username, True)
    response_username = username_response.json()[0][helpers.key_username]

    assert response_username == request_username, "The username is not as expected. Expected: {act1}, Actual: {act2}".format(
        act1=request_username, act2=response_username)


# test find user with invalid id, the Id is not existed in system
def test_find_user_by_invalid_id():
    request_user_id = 11
    id_response = call_request(request_user_id, None, None, True)
    if len(id_response.json()) > 0:
        response_user_id = id_response.json()[0][helpers.key_id]
    else:
        response_user_id = []

    assert response_user_id != request_user_id, "The user ID is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_id)


# find user by invalid email, the email is not existed in system
def test_find_user_by_invalid_email():
    request_user_email = 'nhuptt@gmail.com'
    email_response = call_request(None, request_user_email, None, True)
    if len(email_response.json()) > 0:
        response_user_email = email_response.json()[0][helpers.key_email]
    else:
        response_user_email = []

    assert response_user_email != request_user_email, "The user email is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_email)


# find user by invalid username, the username is not existed in system
def test_find_user_by_invalid_username():
    request_username = 'NhuPTT'
    username_response = call_request(None, None, request_username, True)
    if len(username_response.json()) > 0:
        response_username = username_response.json()[0][helpers.key_username]
    else:
        response_username = []

    assert response_username != request_username, "The username is not as expected. Expected: [], Actual: {act}".format(
        act=response_username)


# test find user with empty id
def test_find_user_by_empty_id():
    request_user_id = ''
    id_response = call_request(request_user_id, None, None, True)
    if len(id_response.json()) > 0:
        response_user_id = id_response.json()[0][helpers.key_id]
    else:
        response_user_id = []

    assert response_user_id != request_user_id, "The user ID is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_id)



# test find user with id is special characters
def test_find_user_special_characters_id():
    request_user_id = '#$%&*'
    id_response = call_request(request_user_id, None, None, True)
    if len(id_response.json()) > 0:
        response_user_id = id_response.json()[0][helpers.key_id]
    else:
        response_user_id = []

    assert response_user_id != request_user_id, "The user ID is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_id)


# test find user with id is characters text
def test_find_user_characters_id():
    request_user_id = 'test'
    id_response = call_request(request_user_id, None, None, True)
    if len(id_response.json()) > 0:
        response_user_id = id_response.json()[0][helpers.key_id]
    else:
        response_user_id = []

    assert response_user_id != request_user_id, "The user ID is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_id)

# find user by empty email
def test_find_user_by_empty_email():
    request_user_email = ''
    email_response = call_request(None, request_user_email, None, True)
    if len(email_response.json()) > 0:
        response_user_email = email_response.json()[0][helpers.key_email]
    else:
        response_user_email = []

    assert response_user_email != request_user_email, "The user email is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_email)


# find user by special characters email
def test_find_user_by_special_characters_email():
    request_user_email = '%$^&'
    email_response = call_request(None, request_user_email, None, True)
    if len(email_response.json()) > 0:
        response_user_email = email_response.json()[0][helpers.key_email]
    else:
        response_user_email = []

    assert response_user_email != request_user_email, "The user email is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_email)

# find user by wrong format email
def test_find_user_text_format_by_email():
    request_user_email = '1234'
    email_response = call_request(None, request_user_email, None, True)
    if len(email_response.json()) > 0:
        response_user_email = email_response.json()[0][helpers.key_email]
    else:
        response_user_email = []

    assert response_user_email != request_user_email, "The user email is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_email)

# find user by empty username
def test_find_user_by_empty_username():
    request_username = ''
    username_response = call_request(None, None, request_username, True)
    if len(username_response.json()) > 0:
        response_username = username_response.json()[0][helpers.key_username]
    else:
        response_username = []

    assert response_username != request_username, "The username is not as expected. Expected: [], Actual: {act}".format(
        act=response_username)

# find user by special_characters username
def test_find_user_by_special_characters_username():
    request_username = '@#$!'
    username_response = call_request(None, None, request_username, True)
    if len(username_response.json()) > 0:
        response_username = username_response.json()[0][helpers.key_username]
    else:
        response_username = []

    assert response_username != request_username, "The username is not as expected. Expected: [], Actual: {act}".format(
        act=response_username)

# check returned status code by id with value = 200
def test_status_code_by_id():
    user_id = 1
    id_response = call_request(user_id, None, None, True)
    status_code = id_response.status_code

    assert status_code == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=status_code)


# check returned status code by username with value = 200
def test_status_code_by_username():
    username = 'Samantha'
    username_response = call_request(None, None, username, True)
    status_code = username_response.status_code

    assert status_code == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=status_code)


# check returned status code by email with value = 200
def test_status_code_by_email():
    user_email = 'Shanna@melissa.tv'
    email_response = call_request(None, user_email, None, True)
    status_code = email_response.status_code

    assert status_code == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=status_code)


# check returned error status code by id with value != 200
def test_error_status_code_by_id():
    user_id = 12
    id_response = call_request(user_id, None, None, False)
    status_code = id_response.status_code

    assert status_code != 200, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=status_code)


# check returned error status code by username with value != 200
def test_error_status_code_by_username():
    username = 'abc'
    username_response = call_request(None, None, username, False)
    status_code = username_response.status_code

    assert status_code != 200, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=status_code)


# check returned error status code by email with value != 200
def test_error_status_code_by_email():
    user_email = 'abc@gmail.com'
    email_response = call_request(None, user_email, None, False)
    status_code = email_response.status_code

    assert status_code != 200, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=status_code)