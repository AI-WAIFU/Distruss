function request(method,endpoint,object,callback){
    // construct an HTTP request
    let xhr = new XMLHttpRequest()
    xhr.open(method, endpoint, true)
    xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')

    // send the collected data as JSON
    xhr.send(JSON.stringify(callback))

    // send the collected data as JSON
    xhr.onloadend = callback

    xhttp.onreadystatechange = function() {
        if (this.readyState != 4){
            //do nothing
            return null
        }
        if (this.readyState == 4 && this.status == 200) {
            let json = JSON.parse(xhr.responseText)
            callback(json)
        }
    }
}

const main = {
}

Vue.createApp(CounterApp).mount('#counter')

