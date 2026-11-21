import requests

users = {}
userTokens = {}

# Helper Functions:
# Function to check that a user exists
def getUser(name):
    # in order to do this correctly, we need both the username and the password in order to get a token from the server
    # then, we add the token to a request to get all players, and we get the player that is associated with the token
    tokens = requests.post(url + "/token/obtain/", {"username":name, "password":users[name]}).json()

    # if we didnt get a token, that means that the player does not exist (so long as the password was right as well)
    if not "access" in tokens:
        return None

    userTokens[name] = tokens

    print("Player:", name, "was gotten successfully.")

    # now that we have the token, we can get the player
    return requests.get(url + "/models/players/", headers={"Authorization":"Bearer " + tokens["access"]})

# Function to make a new player
def createUser(u, p, e):
    response = requests.post(url + "/models/players/", json={
        "username":u,
        "password":p,
        "email":e
    })

    if response.status_code == 200:
        users[u] = p
    elif not u in users:
        users[u] = None
    
    return response

# All of the things that need to be tested with user creation is:

# Players should not have the same name

# Password should have:
# at least 8 letters
# at least one capital letter
# at least one symbol

# The user should have an accurate / acceptable email

# if any of these are not right, the user should not get created

url = "http://localhost:8000"

r = createUser("testUser", "t3stUser!", "testUser@example.com")
print(r.json())
assert r.status_code == 200

first = getUser("testUser")

assert first != None

firstUser = first.json()[0]

# Create a new user with the same name
r = createUser("testUser", "t3stUserPass!", "testUser@example.com")
print(r.json())
assert r.status_code == 400

# Create a new user with bad password
# < 8 letters
r = createUser("testUser2", "test", "testUser@example.com")
print(r.json())
assert r.status_code == 400
assert getUser("testUser2") == None

# No number
r = createUser("testUser2", "testUser", "testUser@example.com")
print(r.json())
assert r.status_code == 400
assert getUser("testUser2") == None

# No symbol
r = createUser("testUser2", "t3stUser", "testUser@example.com")
print(r.json())
assert r.status_code == 400
assert getUser("testUser2") == None

# Bad Email (I won't be checking all of the functionality of this, as i use a module instead of checking it myself)
r = createUser("testUser2", "t3stUser!", "testUser")
print(r.json())
assert r.status_code == 400
assert getUser("testUser2") == None

# All good
r = createUser("testUser2", "t3stUser!", "testUser@example.com")
print(r.json())
assert r.status_code == 200

# Check both exist
assert getUser("testUser") != None
second = getUser("testUser2")
assert second != None

secondUser = second.json()[0]

# Delete both so that we can run these tests multiple times
print(requests.delete(url + "/models/players/" + str(firstUser["id"]) + "/", headers={"Authorization": "Bearer " + userTokens[firstUser["username"]]["access"]}).json())
print(requests.delete(url + "/models/players/" + str(secondUser["id"]) + "/", headers={"Authorization": "Bearer " + userTokens[secondUser["username"]]["access"]}).json())

print("User Registration Tests Complete")