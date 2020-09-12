function validURL(str) {
    var pattern = new RegExp('^(https?:\\/\\/)?' + // protocol
        '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
        '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
        '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
        '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
        '(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator
    return !!pattern.test(str);
}


document.addEventListener("keypress", function (event) {
    if (event.code == "Enter") return false
})

function noenter() {
    return !(window.event && window.event.keyCode == 13);
}

var code
    = document.getElementById("inputPassword");

var strengthbar = document.getElementById("meter");

code.addEventListener("keyup", function () {
    checkpassword(code.value)

})
var display = document.getElementsByClassName("textbox")[0];

function checkpassword(password) {
    var strength = 0;
    if (password.match(/[a-z]+/)) {
        strength += 1;
    }
    if (password.match(/[A-Z]+/)) {
        strength += 1;
    }
    if (password.match(/[0-9]+/)) {
        strength += 1;
    }
    if (password.match(/[$@#&!]+/)) {
        strength += 1;

    }
    if (password.length < 6) {
        display.innerHTML = "minimum number of characters is 6";
    }

    if (password.length > 12) {
        display.innerHTML = "maximum number of characters is 12";
    }
    switch (strength) {
        case 0:
            strengthbar.value = 0;
            break;

        case 1:
            strengthbar.value = 25;
            break;

        case 2:
            strengthbar.value = 50;
            break;

        case 3:
            strengthbar.value = 75;
            break;

        case 4:
            strengthbar.value = 100;
            break;
    }
}

let url_form = document.getElementById("send-form");
url_form.addEventListener("submit", function (event) {
    let url_input = document.getElementById("url");
    let value = url_input.value;
    if (validURL(value) === true) {
        return true
    } else return false;
})