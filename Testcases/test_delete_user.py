import requests
import helpers
import pytest


# call request
def call_request(user_id, is_valid_request):
    if is_valid_request:
        return requests.request('DELETE', helpers.base_url('/users/' + str(user_id)), headers=helpers.headers)
    else:
        return requests.request('DELETE', helpers.base_url('/usr/' + str(user_id)), headers=helpers.headers)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
# xfail marker to indicate that expect a test to fail
@pytest.mark.parametrize("user_id", [(3),
                                     pytest.mark.xfail(13),
                                     ])
# Case 1: test delete a user with id =3, then response is empty dictionary if success
# Case 2: test delete a user with id =13 which is not existed in system, then response is empty dictionary, case fail
def test_delete_by_user_id(user_id):
    response = call_request(user_id, True)
    response_json = response.json()

    assert response_json == {}, "The response data is not as expected. Expected: {}, Actual: {act}".format(
        act=response_json)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("user_id, statuscode", [(13, 404),
                                                 (None, 404),
                                                 ('test', 404),
                                                 ])
# test delete user with user_id is invalid
# case 1: test delete a user with id =13 which is not existed in system, then response is empty dictionary
# case 2: # test delete user with user_id = null
# case 3: test delete user with user_id = character
def test_delete_for_user_id_invalid(user_id, statuscode):
    response = call_request(user_id, True)
    response_json = response.json()

    assert response_json == {}, "The response data is not as expected. Expected: {}, Actual: {act}".format(
        act=response_json)
    assert response.status_code == statuscode, "The returned error status code is not as expected. Expected: {act1}, Actual: {act2}".format(
        act1=user_id, act2=statuscode)


@pytest.mark.parametrize("user_id, statuscode", [(1, 200)])
# check returned status code with value = 200
def test_status_code(user_id, statuscode):
    response = call_request(user_id, True)
    assert response.status_code == statuscode, "The returned status code is not as expected. Expected: 200, Actual: {act}".format(
        act=statuscode)


# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("user_id, statuscode", [(1, 200)])
# check returned error status code with value != 200
def test_error_status(user_id, statuscode):
    response = call_request(user_id, False)
    if response.status_code != statuscode:
        assert response.status_code != statuscode, "The returned error status is not as expected. Expected: Not 200, Actual: {act}".format(
            act=statuscode)
    else:
        {}
