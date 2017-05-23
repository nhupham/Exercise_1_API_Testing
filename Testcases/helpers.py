# default variables
id = 1
email = ''
username = ''
input_data = {}
headers = {'content-type': "application/json"}

#dictionary keys
key_id = 'id'
key_username = 'username'
key_email = 'email'

#base url method
def base_url(path):
    return 'https://jsonplaceholder.typicode.com' + path
