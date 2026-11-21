import requests

# All of the things that need to be tested with the auth sequence is:

# Create a user
# Log in (Obtain their tokens + refresh their tokens)
# Get their information
# Do an authorized action
# Delete their user

url = "http://localhost:8000"

username = "testUser"
password = "t3stPass!"

# Create a test user
r = requests.post(url + "/models/players/", json={
    "username":username,
    "password":password,
    "email":"testUser@example.com"
})

# test we got the right status code
assert r.status_code == 200
print(r.json())

# now we obtain the tokens (log in) using the players credentials
r = requests.post(url + "/token/obtain/", {"username":username, "password":password})

assert r.status_code == 200

tokens = r.json()

# if we didnt get a token, that means that the player does not exist
assert "access" in tokens and "refresh" in tokens

print("Player was logged in successfully.")

# test token refreshing
r = requests.post(url + "/token/refresh/", {"refresh":tokens["refresh"]})

assert r.status_code == 200

newToken = r.json()

assert "access" in newToken
print("Tokens refreshed properly.")

tokens["access"] = newToken["access"]

# now that we have the token, we can get the player
r = requests.get(url + "/models/players/", headers={"Authorization":"Bearer " + tokens["access"]})

assert r.status_code == 200
print("Player data grabbed successfully.")

firstUser = r.json()[0]

# now we can do an authorized action
r = requests.post(url + "/main/auth_test/", headers={"Authorization": "Bearer " + tokens["access"]})
assert r.status_code == 200
print(r.json())

# Delete both so that we can run these tests multiple times
r = requests.delete(url + "/models/players/" + str(firstUser["id"]) + "/", headers={"Authorization": "Bearer " + tokens["access"]})

assert r.status_code == 200
print(r.json())

# check they are both deleted, by trying to log in
r = requests.post(url + "/token/obtain/", {"username":username, "password":password})
assert r.status_code == 401
print(r.json())

print("Auth Sequence Tests Complete")