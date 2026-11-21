import requests

users = {}
userTokens = {}

# Helper Functions:
def getTokens(name):
    tokens = requests.post(url + "/token/obtain/", {"username":name, "password":users[name]}).json()
    
    # if we didnt get a token, that means that the player does not exist (so long as the password was right as well)
    if not "access" in tokens:
        return None

    userTokens[name] = tokens

    return tokens["access"]

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

# All of the things that need to be tested with user data is:

# Players must be logged in
# Players must not get other player data
# Player data shall not contain passwords
# Player data shall not contain reset password information

url = "http://localhost:8000"

# First user
r = createUser("testUser", "t3stUser!", "testUser@example.com")
assert r.status_code == 200

# Second user
r = createUser("testUser2", "t3stUser!", "testUser@example.com")
assert r.status_code == 200

# Check both exist (log in as both)
assert getTokens("testUser") != None
assert getTokens("testUser2") != None

print("Both users created and logged in successfully.")

# Check that we need to be logged in to get user information
r = requests.get(url + "/models/players/")
print(r.json())
assert r.status_code == 401

# Get player information for both
r = requests.get(url + "/models/players/", headers={"Authorization":"Bearer " + userTokens["testUser"]["access"]})
assert r.status_code == 200
firstUser = r.json()[0]
print("Player testUser has an id of", firstUser["id"])

r = requests.get(url + "/models/players/", headers={"Authorization":"Bearer " + userTokens["testUser2"]["access"]})
assert r.status_code == 200
secondUser = r.json()[0]
print("Player testUser2 has an id of", secondUser["id"])

# Test that data has excluded the correct information
assert not "password" in firstUser and not "password" in secondUser
print("Password Excluded")

assert not "resetPasswordToken" in firstUser and not "resetPasswordToken" in secondUser
print("Reset Password Token Excluded")

assert not "resetPasswordExpire" in firstUser and not "resetPasswordExpire" in secondUser
print("Reset Password Expire DateTime Excluded")

assert not "resetPasswordUsed" in firstUser and not "resetPasswordUsed" in secondUser
print("Reset Password Usage Value Excluded")

# Now test that we need to be the correct person to get the information
r = requests.get(url + "/models/players/" + str(secondUser["id"]) + "/", headers={"Authorization":"Bearer " + userTokens["testUser"]["access"]})
print(r.json())
assert r.status_code == 401

# Delete both so that we can run these tests multiple times
assert requests.delete(url + "/models/players/" + str(firstUser["id"]) + "/", headers={"Authorization": "Bearer " + userTokens[firstUser["username"]]["access"]}).status_code == 200
assert requests.delete(url + "/models/players/" + str(secondUser["id"]) + "/", headers={"Authorization": "Bearer " + userTokens[secondUser["username"]]["access"]}).status_code == 200

print("Players deleted successfully")

print("User Data Tests Complete")