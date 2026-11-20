import requests

users = {}

# Helper Functions:
# Function to check that a user exists
def getUser(name):
    # in order to do this correctly, we need both the username and the password in order to get a token from the server
    # then, we add the token to a request to get all players, and we get the player that is associated with the token
    tokens = requests.post(url / "token/obtain/", {"username":name, "password":users[name]})

    print(tokens)

    # if we didnt get a token, that means that the player does not exist (so long as the password was right as well)
    if not "accessToken" in tokens.request.body:
        return False

    # now that we have the token, we can get the player
    return requests.get(url / "models/players/", headers={"Authorization":"Bearer " + tokens.request.body["accessToken"]})

# Function to make a new player
def creareUser(u, p, e):
    users[u] = p

    return requests.post(url / "models/players", json={
        "username":u,
        "password":p,
        "email":e
    })

# All of the things that need to be tested with user creation is:

# Players should not have the same name

# Password should have:
# at least 8 letters
# at least one capital letter
# at least one symbol

# The user should have an accurate / acceptable email

# if any of these are not right, the user should not get created

url = "http://localhost:8000"

# Create a default user, with everything right
# requests.post(url / "models/players", json={
#     "username":"testUser",
#     "password":"testUserPass!",
#     "email":"testUser@example.com"
# })

creareUser("testUser", "testUserPass!", "testUser@example.com")

first = getUser("testUser")

assert first != None

first.delete()
first.save()

# Create a new user with the same name

# Create a new user with bad password
# < 8 letters
# No cap letter
# No symbol

# All good

# Check both exist

# Delete both so that we can run these tests multiple times

# check they are both deleted