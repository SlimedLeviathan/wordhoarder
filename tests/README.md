This is the readme for the unit and component tests.

# Table of Contents
[Table of Contents](#table-of-contents)
[Overview](#overview)
    [Unit Tests](#unit-tests)
        [User Register](#user-register)
        [Reset Password Function](#reset-password)
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

Users can't have the same name, and the password must fit our criteria.

Our criteria is: 
* 8 letters or longer
* At least one number
* At least one symbol

### Reset Password
The reset password function is the function that runs when the user submits a password to a link sent to their email, after they ask for a password reset.

What happens before this is that a user asks for a password reset, the server creates a reset password id as a uuid4, which is then saved to the users information. The time that the id was created is also saved alongside this. The server then sends an email containing the link to the reset page, with the reset password id. Whenever someone goes to a reset password link, their link should also contain the id that is saved with their account. When the user submits a new password,the server then gets the id, and then checks the database for the user with this id.

All of the things that the server should check before allowing the user to change their password is:
* Making sure the user isn't logged in with some other account
* Making sure that the id matches with a user
* Making sure that the id was created within an hour (this makes the link automatically expire after an hour)
* Making sure the password follows the previous criteria

After all of this, the password is then reset and the user gets a notification that their password was reset. If any of the previous checks go wrong, the server should instead send an error detailing the problem.

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
* Logging into that account
* Getting the access and refresh tokens
* Using the access and refresh tokens to authorize a task

### Word Validation
