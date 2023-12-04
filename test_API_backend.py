"""
Test steps:
1. I want to start by verifying that the DB is
   Indeed empty. I will start in a 'get_all_api' request to check it.
   If the db is not empty I will use the 'delete_api' method to delete all users in it.

   Expected results : None/empty []
   Actual results : None/empty  []


2. If the DB is indeed empty I will create some users,
   At first 1 user using the 'Post' method, and immediately after that the 'Get' method
   to validate the action. If I see it works properly I will continue creating more users.

   data: {"name": "Wall-E46765", "id": "666" }
   Expected results : response 200, {"name": "Wall-E46765", "id": "666" }
   Actual results : response 500, internal server error


3. If my user was created successfully, Try to 'post' multiple users at ones, in a list of jsons and validate the
   request failure and the correct response.

   data: [{"name": "Omri", "id": "2"}, {"name": "Gaia", "id": "3"}, {"name": "Alon", "id": "4"}, {"name": "Wall-E", "id": "5"}]
   Expected results : should receive 400 response-bad request / 401-not found etc.
   Actual results :  500 Internal Server Error and my list of users has been added to the db.


4. Try to 'post' duplicate users - same name and id , and then try to retrieve them by 'get' and examine the response.

   data: {"name": "Wall-E46765", "id": "666" }
   Expected results : 409 response-conflict in records
   Actual results : response 500, internal server error


5. I will continue using the 'Put' method to verify changes in the DB users,
   and validate their changes using the 'Get' method.

   data: {"name": "Yair", "id": "666"}
   Expected results : should receive response of 200 and the updated json: {"name": "Yair", "id": "666"}
   Actual results :  response 500, internal server error


6. I will try to delete all users by using the 'Delete' method, and validate that using the 'Get' method.

   "http://localhost:5000/users" - without mentioning a specific user-id
   Expected results : should receive 400 response-bad request / 401-not found etc.
   Actual results : response 500, internal server error


7. After I finished the 'flow' tests, I want to test and validate the methods instructions of json formats.
   Try to send all the methods with the opposite structure - instead of {name: str, id: str} --> send {id: str, name: str}

   Expected results : should receive 400 response-bad request
   Actual results : 200 (in the methods that didn't get 500)


8. try to post semi-duplicated users- same name OR same id.
   data: {"name": "Yair", "id": "898"} /  {"name": "Michal", "id": "898"}
   Expected results : should receive response of 200 and the updated json: {"name": "Yair", "id": "898"} /  {"name": "Michal", "id": "898"}
   (there is no Unique specification in the documentation)
   Actual results :  response 500, internal server error



 Bugs:

 1. In the 'Get user' & 'Post user' method, I supposed to receive a json response
  with a { name: str, id: str} structure, instead I received a json with the following structure-
  {id: str, name: str}.

 2. In the 'Post user' method I was able to create a new user with the opposite json format
    instead of {name: str, id: str} --> send {id: str, name: str}, it is not supposed to succeed.

 3.  when I try to 'Post' a list of users I supposed to receive a 400 code- bad request because there isn't such method,
    but instead I receive a 500 code, and my list of users does in fact being added to the db.

 4. 'Post user' allows you to create new users with the same name and id multiple times and due to that the

 5. 'Put' & 'Delete' not working properly, when I try to send the requests, in both json structures (regular and opposite),
    I receive a '500' response-server error.

"""


import pytest
import requests

api_url = "http://localhost:5000/users"
data_1_user = {"name": "Wall-E46765","id": "666"}
data_multi_users = [{"name": "Omri", "id": "2"}, {"name": "Gaia", "id": "3"}, {"name": "Alon", "id": "4"}, {"name": "Wall-E", "id": "5"}]


def validate_db_empty():
    # can be used as a 'setup' fixture
    response_empty = requests.get(api_url)
    assert response_empty.text == ""


@pytest.fixture
def post_api():
    # Post 1 user #
    response_post = requests.post(api_url, json=data_1_user)
    print(response_post.text, response_post.status_code)
    return response_post


@pytest.fixture
def get_api():
    # Get 1 user #
    response_get = requests.get(api_url+"/Wall-E46765")
    print(response_get.text, response_get.status_code)
    return response_get.text


@pytest.fixture
def get_all_api():
    # Get all users #
    response_get_all_users = requests.get(api_url)
    print(response_get_all_users.text, response_get_all_users.status_code)
    return response_get_all_users.text


@pytest.fixture
def put_api():
    # Put - edit user #
    data_put = {"name": "Yair", "id": "666"}
    response_put = requests.put(api_url + "/666", json=data_put)
    print(response_put.text, response_put.status_code)
    return response_put.text


@pytest.fixture
def delete_api():
    # Delete a user #
    response_delete = requests.delete(api_url + "/666")
    print(response_delete.text, response_delete.status_code)
    return response_delete.text





