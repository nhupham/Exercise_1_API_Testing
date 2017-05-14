import requests
import helpers

user_name=''
user_count=''
response = requests.request('GET', helpers.base_url('/users/'))


# call request
def call_request():
    global response
    response = requests.request('GET', helpers.base_url('/users/'))


# call request invalid
def call_request_invalid():
    global response
    response = requests.request('GET', helpers.base_url('/usr/'))

# check the returned status code with value = 200
def test_status_code():
    call_request()
    statuscode = response.status_code
    assert statuscode == 200, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(act=statuscode)

# check the returned error status code with value != 200
def test_error_status_code():
    call_request_invalid()
    statuscode = response.status_code
    assert statuscode != 200, "The returned status code is not as expected. Expected: Not 200, Actual: {act}".format(act=statuscode)

#check get a valid username from users list
def test_check_get_valid_username():
    username= 'Antonette'
    global user_name
    call_request()
    user_name = response.json()[1][helpers.key_username]
    assert user_name == username, "The returned username is not as expected. Expected:'Leanne Graham', Actual: {act}".format(act=user_name)

#check a username is not exsited from users list
def test_check_get_invalid_username():
    username= 'nhuptt'
    global user_name
    call_request()
    if len(response.json()) >0:
        user_name = response.json()[0][helpers.key_username]
    else:
        user_name=[]
    assert user_name != username, "The returned username is not as expected. Expected:[], Actual: {act}".format(act=user_name)

#check a username is empty
def test_check_get_empty_username():
    username= ''
    global user_name
    call_request()
    if len(response.json()) >0:
        user_name = response.json()[0][helpers.key_username]
    else:
        user_name=[]
    assert user_name != username, "The empty username is not as expected. Expected:[], Actual: {act}".format(act=user_name)

#count users from users list
def test_get_users_count():
    global user_count
    call_request()
    user_count = len(response.json())
    assert user_count == 10, "The returned list user's number is not as expected. Expected:10, Actual: {act}".format(act=user_count)
