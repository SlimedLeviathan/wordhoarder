This is the readme for the unit and component tests.

# Table of Contents
[Table of Contents](#table-of-contents)
[Overview](#overview)
    [Unit Tests](#unit-tests)
        [User Register](#user-register)
        [User Data](#get-user-data)
        [Frontend Word Input](#frontend-word-input)
        [Server Word Validation](#server-word-validation)
    [Component Tests](#component-tests)
        [Auth Sequence](#auth-sequence)
        [Word Validation](#word-validation)

# Overview
Firstly, to run any of the services that are needed for testing (the website or the server), please check the README inside of the root folder of this project. It will describe how to install and start both parts of the project.

## Unit Tests

The 4 units that we created tests for are:
* User Register Function
* Reset Password
* Frontend Word Input
* Server Word Validation

### User Register
The user register function is a pretty simple function, as it just takes in the users username, password and email and then adds a value to the database based on these values. There are some things that need to be taken care of though.

Users can't have the same name, the users email must be of a correct format, and the password must fit our criteria.

Our criteria is: 
* 8 letters or longer
* At least one number
* At least one symbol

There are 6 automated tests:
* Unique Name
* Valid Email
* 8 Letter Password
* At least 1 number in password
* At least 1 symbol in password

If any of these fail, then the server should send a 400 response, with a description of the problem.

### Get User Data
Getting user data is an important function of the server, and users should not be able to get other users data, unless they are an admin. Security data also should not go to the user. So, the checks for this test are as follows:

* Players must be logged in to get their data
* Player data should not include passwords or reset password information
* Logged in players should not get other players data 


### Frontend Word Input
This function handles the user's word submission on the client side before sending any request to the server. It formats the input (such as trimming whitespace and converting letters to uppercase) and checks basic client-side constraints, including ensuring the input is not empty, matches the required character length, and contains only valid alphabetic characters (no numbers or symbols). If the input is invalid, it displays a warning message to the user and blocks the API call.

### Server Word Validation

## Component Tests

The 2 components that we made tests for are:
* User register, login and authorization (aka the auth sequence)
* Word Validation (frontend and backend)

### Auth Sequence
The auth sequence details everything that a user would do before they are able to get into the game, as well as making sure that everything they do is associated with their account.

This includes:
* Registering a new account
* Logging into that account (and refreshing the tokens)
* Using the access and refresh tokens to authorize a task
* Deleting the account

### Word Validation
