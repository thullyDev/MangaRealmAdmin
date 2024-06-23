(function () {
	$(".auth-con span.close-btn, .user-action-btn[data-type='login'], .anon-user-con").click(() => {
		$(`.form-con`).removeClass('active')
		$(`.form-con[data-type="signup"]`).addClass('active')
		showCloseEle(".auth-con", "fade")
	});
	
	$(".auth-link").click(function() {
		const thisEle = $(this)
		const closeEle = thisEle.data('type')
		const showEle = closeEle == "login" ? "signup" : "login"
		showCloseAuthEle(closeEle, showEle)
	});
	
	$(".forgot-btn").click(function() {
		const thisEle = $(this)
		const closeEle = thisEle.data('type')
		showCloseAuthEle(closeEle, "forgot_password")
	});

	$(".submit-btn").click(function (e) {
		e.preventDefault();
		const thisEle = $(this)
	  	const type = thisEle.data("type")

	  	if (!["signup", "login", "forgot_password", "resend", "verify", "renew_password"].includes(type)) return

	    const data = getInputs(`.form-con.active .icon-input`)
	    let url = ""


	  	if ("signup" == type) {
	  		const { email, username, password, confirm } = data

	  		if (!isValidEmail(email)) {
	  			showAlert({ message: "email is invalid" })
	  			return
	  		} 

	  		if (password != confirm) {
	  			showAlert({ message: "password and confirm dont match" })
	  			return
	  		}

	  		if (password.length <= 10) {
	  			showAlert({ message: "password should be atleast 10 characters long" })
	  			return
	  		}
	  	}

	  	if (["login", "forgot_password", "resend"].includes(type)) {
	  		const { email } = data

	  		if (!isValidEmail(email)) {
	  			showAlert({ message: "email is invalid" })
	  			return
	  		} 
	  	}

	  	if ("renew_password" == type) {
	  		const { password, confirm } = data

	  		if (password != confirm) {
	  			showAlert({ message: "password and confirm dont match" })
	  			return
	  		}

	  		if (password.length <= 10) {
	  			showAlert({ message: "password should be atleast 10 characters long" })
	  			return
	  		}
	  	}

	const captchaToken = getCaptchaResponse("auth_id_" + type)

	if (captchaToken.length < 1) return 

	$.ajax({
	    url: `/user/ajax/post/${type}/`,
	    type: 'POST',
	    data: {
	        csrfmiddlewaretoken: csrfToken,
	        data: JSON.stringify(data),
	        captcha_token: captchaToken,
	    },
	    beforeSend: function() {
	    	showLoader()
	    },
	    success: function(response) {
	        const { message, data } = response
			showAlert({ message })
			closeLoader()
			
			if ("verify" == type) {
				const isfor = thisEle.data('isfor')
				isfor == "signup" ? window.location.reload() : renewPasswordProcessor(data.code)
				return 
			}

			if (["login", "renew_password"].includes(type)) window.location.reload()

			if (["signup", "forgot_password"].includes(type)) {
				$(`.submit-btn[data-type="verify"]`).data("isfor", type)
				showCloseAuthEle(type, "verify")
			} 

	    },
	    error: function(error) {
	    	const { message } = error.responseJSON
			showAlert({ message })
			closeLoader()
	    }
	});
	});

	$(".logout-btn").click(() => logoutUser());

})();

function showCloseAuthEle(closeEle, showEle) {
	$(`.form-con[data-type="${closeEle}"]`).removeClass('active')
	$(`.form-con[data-type="${showEle}"]`).addClass('active')
}

function renewPasswordProcessor(code) {
	$(`.renew_password .code`).val(code)
	showCloseAuthEle("verify", "renew_password")
}

function popAuth() {
	$(".auth-con span.close-btn").click()
}

function logoutUser () {
	$.ajax({
	    url: "/admin/ajax/get/logout/",
	    type: 'GET',
	    data: {
	        csrfmiddlewaretoken: csrfToken,
	    },
	    beforeSend: function() {
	    	showLoader()
	    },
	    success: (response) => {
	        const { message } = response
			showAlert({ message })
			closeLoader()
			window.location.replace("/")
	    },
	    error: (error) => {
	    	const { message } = error.responseJSON
			showAlert({ message })
			closeLoader()
	    }
	});
}


function renderCaptchas(IDs) {
	for (let i = 0; i < IDs.length; i++) {
		const id = IDs[i]
		captchas[id] = hcaptcha.render(id, {
          'sitekey' : '39e81e61-6f35-44ba-b557-668c9016779a',
        });
	}
}

function renderCaptchaWidgets() {
	const captchaIDs = []
	$(".captcha-widgets").each(function() {
		const thisEle = $(this)
		const id = thisEle.attr("id")

		captchaIDs.push(id)
	})

	renderCaptchas(captchaIDs)
}

function getCaptchaResponse(id) {
	const widgetID = captchas[id] 
	return hcaptcha.getResponse(widgetID)
}