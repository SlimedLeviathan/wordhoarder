<script setup>
    import { login } from "../components/serverHandler";
    
    const handleLogin = () => {
        let user = document.getElementById("userInput").value
        let pass = document.getElementById("passInput").value

        login(user, pass).then((res) => {
            console.log(res)

            let loginInfo = document.getElementById("loginInfo")

            loginInfo.innerText = res["status"] == 200 ? "Login Successful!" : res["detail"]
        })
    }
</script>
<template>
    <main>
        <p>Login View</p>

        <form id="loginForm" onsubmit="return false">
            <label for="userInput">Username:</label>
            <input id="userInput"/>
            <label for="passInput">Password:</label>
            <input type="password" id="passInput"/>
            <input @click="handleLogin" type="submit" />
        </form>

        <p id="loginInfo"></p>
    </main>
</template>