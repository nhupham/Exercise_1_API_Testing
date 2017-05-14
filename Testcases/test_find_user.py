import requests
import helpers

response_id = requests.request('GET', helpers.base_url('/users?id=' + str(helpers.id)))
response_email = requests.request('GET', helpers.base_url('/users?email=' + str(helpers.email)))
response_username = requests.request('GET', helpers.base_url('/users?username=' + str(helpers.key_username)))

# call request valid by id
def call_request_by_id(id):
    global response_id
    response_id = requests.request('GET', helpers.base_url('/users?id=' + str(id)))

# call request valid by email
def call_request_by_email(email):
    global response_email
    response_email = requests.request('GET', helpers.base_url('/users?email=' + str(email)))

# call request valid by username
def call_request_by_username(username):
    global response_username
    response_username = requests.request('GET', helpers.base_url('/users?username=' + str(username)))


# call request invalid by id
def call_request_invalid_by_id(id):
    global response_id
    response_id = requests.request('GET', helpers.base_url('/usrid' + str(id)))


# call request invalid by username
def call_request_invalid_by_username(username):
    global response_username
    response_username = requests.request('GET', helpers.base_url('/usrna' + str(username)))


# call request invalid by email
def call_request_invalid_by_email(email):
    global response_email
    response_email = requests.request('GET', helpers.base_url('/usrmail' + str(email)))


# test find user with valid id
def test_find_user_by_id():
    id = 1
    call_request_by_id(id)
    user_id = response_id.json()[0][helpers.key_id]
    assert user_id == id, "The user ID is not as expected. Expected: 1, Actual: {act}".format(
        act=user_id)


# find user by valid email
def test_find_user_by_email():
    email = 'Shanna@melissa.tv'
    call_request_by_email(email)
    response_user_email = response_email.json()[0][helpers.key_email]
    assert response_user_email == email, "The user email is not as expected. Expected: Shanna@melissa.tv, Actual: {act}".format(
        act=response_user_email)


# find user by valid username
def test_find_user_by_username():
    username = 'Samantha'
    call_request_by_username(username)
    response_user_name = response_username.json()[0][helpers.key_username]
    assert response_user_name == response_user_name, "The username is not as expected. Expected: Samantha, Actual: {act}".format(
        act=response_user_name)


# test find user with invalid id
def test_find_user_by_invalid_id():
    id = 11
    call_request_by_id(id)
    if len(response_id.json()) > 0:
        user_id = response_id.json()[0][helpers.key_id]
    else:
        user_id = []
    assert user_id != id, "The user ID is not as expected. Expected: [], Actual: {act}".format(
        act=user_id)


# find user by invalid email
def test_find_user_by_invalid_email():
    email = 'nhuptt@gmail.com'
    call_request_by_email(email)
    if len(response_email.json()) > 0:
        response_user_email = response_email.json()[0][helpers.key_email]
    else:
        response_user_email = []
    assert response_user_email != email, "The user email is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_email)


# find user by invalid username
def test_find_user_by_invalid_username():
    username = 'NhuPTT'
    call_request_by_username(username)
    if len(response_username.json()) > 0:
        response_user_name = response_username.json()[0][helpers.key_username]
    else:
        response_user_name = []
    assert response_user_name != username, "The username is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_name)


# test find user with empty id
def test_find_user_by_empty_id():
    id = None
    call_request_by_id(id)
    if len(response_id.json()) > 0:
        user_id = response_id.json()[0][helpers.key_id]
    else:
        user_id = []
    assert user_id != id, "The user ID is not as expected. Expected: [], Actual: {act}".format(
        act=user_id)


# find user by empty email
def test_find_user_by_empty_email():
    email = ''
    call_request_by_email(email)
    if len(response_email.json()) > 0:
        response_user_email = response_email.json()[0][helpers.key_email]
    else:
        response_user_email = []
    assert response_user_email != email, "The user email is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_email)


# find user by empty username
def test_find_user_by_empty_username():
    username = ''
    call_request_by_username(username)
    if len(response_username.json()) > 0:
        response_user_name = response_username.json()[0][helpers.key_username]
    else:
        response_user_name = []
    assert response_user_name != username, "The username is not as expected. Expected: [], Actual: {act}".format(
        act=response_user_name)


# check returned status code by id with value = 200
def test_status_code_by_id():
    type_response = response_id
    statuscode = type_response.status_code
    assert statuscode == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=statuscode)


# check returned status code by username with value = 200
def test_status_code_by_username():
    type_response = response_username
    statuscode = type_response.status_code
    assert statuscode == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=statuscode)


# check returned status code by email with value = 200
def test_status_code_by_email():
    type_response = response_email
    statuscode = type_response.status_code
    assert statuscode == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=statuscode)


# check returned error status code by id with value = 400
def test_error_status_code_by_id():
    id = 12
    call_request_invalid_by_id(id)
    statuscode = response_id.status_code
    assert statuscode != 200, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=statuscode)


# check returned error status code by username with value = 400
def test_error_status_code_by_username():
    username = 'abc'
    call_request_invalid_by_username(username)
    statuscode = response_username.status_code
    assert statuscode != 200, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=statuscode)


# check returned error status code by email with value = 400
def test_error_status_code_by_email():
    email = 'abc@gmail.com'
    call_request_invalid_by_email(email)
    statuscode = response_email.status_code
    assert statuscode != 200, "The returned error status code is not as expected. Expected: Not 200, Actual: {act}".format(
        act=statuscode)
