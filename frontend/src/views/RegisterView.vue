<template>
    <main>
        <p>Register View</p>
        
        <form id="registerForm" action="localhost:8000/models/players/create" method="post" onsubmit="return false">
            <label for="userInput">Username:</label>
            <input id="userInput"/>
            <label for="passInput">Password:</label>
            <input type="password" id="passInput"/>
            <label for="emailInput">Email:</label>
            <input id="emailInput"/>
            <input type="submit" />
        </form>
    </main>
</template>