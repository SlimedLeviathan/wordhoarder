// this file just contains a lot of functions that streamline the use of getting information from the backend

export function login(username:string, password:string):Promise<JSON> {
    // whenever we login, we send the server the users username and password, then get back a access and refresh token

    // we should save both, and use the access token to authorize the user
    // refresh token refreshes the access token when it expires

    const request: RequestInfo = new Request("/api/token/obtain/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body:JSON.stringify({
            username:username,
            password:password
        })
    })

    return fetch(request).then(res => {
        return res.json().then((body) => {
            // check for if the response was good
            if (res.status == 200){
                // save the access and refresh tokens if good
                localStorage.setItem("userAccessToken", body["access"])
                localStorage.setItem("userRefreshToken", body["refresh"])

                // console.log(localStorage.getItem("userAccessToken"))
                // console.log(localStorage.getItem("userRefreshToken"))
            }

            body["status"] = res.status
        
            return body
        })
    })
}

// export function refresh():Promise<JSON> {

// }

export function get(url:string, data:object):Promise<JSON> {
    console.log("GET");
    
    const request: RequestInfo = new Request("/api" + url, {
        method: 'GET',
        body:JSON.stringify(data)
    })
    
    return fetch(request)
        .then(res => res.json())
        .then(res => {
            console.log(res);
            return res
        }
    )
}

export function post(url:string, data:object):Promise<JSON> {
    console.log("POST");

    const request: RequestInfo = new Request("/api" + url, {
        method: 'POST',
        body:JSON.stringify(data)
    })

    return fetch(request)
        .then(res => res.json())
        .then(res => {
            console.log(res);
            return res
        }
    )
}