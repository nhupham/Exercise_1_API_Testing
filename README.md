# API Testing in Python

## Exercise Description: 
* Tests are defined in basic in python
* Write tests to automate an API
* Python is preferred, but it is not mandatory, tests can be written in any language you feel comfortable. 
* Using this fake API: 
	https://jsonplaceholder.typicode.com/ 
* Write test to check user handler: 
	https://jsonplaceholder.typicode.com/users/ 

## Create tests for: 
1. List users
2. Find user
3. Create / Delete / Update users 
4. Negative cases

## Installation
Platforms: MacOS X 10.12.4
Install pip is a package management system used to install and manage software packages written in Python
```sh
sudo easy_install pip
```
Pythons: Python 2.7
```sh
pip install -U pytest
```

To check your installation has installed the correct version:
```sh
$ py.test --version
```
Install PyCharm on Mac OS X
PyCharm is an excellent editor for Python that has a community edition that you can use for free
Prerequisites
Install the Oracle JDK 7 on Mac OS X
Download Pycharm
1. Download PyCharm from PyCharm Download page.
2. Click Download Community.
3. Select Save File, then click OK.
4. Wait for the download to complete, then double click the .dmg file.
5. Drag the PyCharm icon to the Applications folder.
6. Open PyCharm as you would any other application.

## Sample Test
@pytest.mark.parametrize: parametrizing test functions

```js
# @pytest.mark.parametrize allows one to define multiple sets of arguments at the test function
@pytest.mark.parametrize("valid_username", [('Antonette'),
                                            ])
# check get a valid username from users list
def test_check_get_valid_username(valid_username):
    response = call_request(True)
    response_username = response.json()[1][helpers.key_username]

    assert response_username == valid_username, "The returned username is not as expected. Expected:{act1}, Actual: {act2}".format(
        act1=valid_username, act2=response_username)

```

## Running Test
Run all test cases

```sh
$ py.test TestCases/
```

Run a Test case suite
```sh
$ py.test TestCases/test_get_list.py 
```
