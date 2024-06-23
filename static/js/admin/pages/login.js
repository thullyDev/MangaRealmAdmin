(function () { 
	$(".submit-btn").click(function() {
	  login()
	});
})();

function login() {
	const data = {}
	$(".icon-input").each(function() {
		const thisEle = $(this)
		const value = thisEle.val()
		const key = thisEle.data("key")

		if (!value || !["email", "password"].includes(key)) return

		data[key] = value
	})

	if (!Object.keys(data).length) { 
		showAlert({ message: "inputs are empty" }) 
		return 
	} 

	$.ajax({
	    url: "/admin/ajax/post/login/",
	    type: 'POST',
	    data: {
	        csrfmiddlewaretoken: csrfToken,
	        data: JSON.stringify(data),
	    },
	    beforeSend: function() {
	    	showLoader()
	    },
	    success: function(response) {
	        const { message } = response
			showAlert({ message })
			closeLoader()
			redirect({ path: "/admin/dashboard" })
	    },
	    error: function(error) {
	    	const { message } = error.responseJSON
			showAlert({ message })
			closeLoader()
	    }
	});
}