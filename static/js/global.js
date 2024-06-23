const print = (message) => console.log(message)

function showAlert({ message, timeOut = 3500 } = {}) { // 3.5 secs
  const outerAlertBox = $(".outer-alert-box");
  const alertBox = $(".alert-box");

  alertBox.text(message)
  outerAlertBox.css("display", "flex").hide().fadeIn()
  setTimeout(() => {
    outerAlertBox.fadeOut(() => {
      alertBox.text("");
    });
  }, timeOut);
}

function showLoader({ selector=".page-loader" } = {}) {
    const loader = $(selector) 
    loader.css("display", "flex").hide().fadeIn()
}

function removeEle(id) {
    $(`*[data-id="${id}"]`).fadeOut().remove()
}

function closeLoader({ selector=".progress-loader" } = {}) {
    const loader = $(selector) 
    loader.fadeOut()
}

function redirect({ path=null } = {}) {
    const location = window.location
    !path ? location.reload() : location.replace(path)
}

function showCloseEle(showele_key, animate="fade") {
    const showEle  = $(showele_key)
    const showEleIsOpen  = showEle.data("open")

    if (animate == "slide") {
        !showEleIsOpen ?
          showEle.css("display", "flex").hide().slideDown().data("open", true) :
          showEle.slideUp().data("open", false) 
          return
    }

    !showEleIsOpen ?
      showEle.css("display", "flex").hide().fadeIn().data("open", true) :
      showEle.fadeOut().data("open", false) 
  }


function getInputs(selector) {
  const selectInputs = $(selector)
  const data = {}

  selectInputs.each((_, ele) => {
    const thisEle = $(ele)
    const name = thisEle.data("key")
    let value = $.trim(thisEle.val())
    value = value == "None" ? "" : value

    data[name] = value
  })

  return data
}

function getCookies() {
    const cookies = document.cookie.split(";");
    const cookiesObject = {};

    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        const [name, value] = cookie.split("=");
        const decodedValue = decodeURIComponent(value);
        cookiesObject[name] = decodedValue;
    }

    return cookiesObject;
}

function setCookie(cookieName, cookieValue, expirationDays) {
    let d = new Date();
    d.setTime(d.getTime() + (expirationDays * 24 * 60 * 60 * 1000));
    let expires = "expires=" + d.toUTCString();
    document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
}

function getCookie(cookieName) {
    let name = cookieName + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let cookieArray = decodedCookie.split(';');
    for(let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) == ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) == 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return "";
}

function deleteCookie(cookieName) {
    document.cookie = cookieName + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}



function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

