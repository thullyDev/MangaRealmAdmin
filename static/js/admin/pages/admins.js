(function () { 
	$(".real.add-admin, .outter-add-admin-modal-con .close-btn").click(() => showCloseEle(".outter-add-admin-modal-con"));

	$(".reset-btn").click(function() {
		$.ajax({
		    url: "/admin/ajax/post/reset_settings/",
		    type: 'POST',
		    data: {
		        csrfmiddlewaretoken: csrfToken,
		        site_key: $(".sitekey-input").val()
		    },
		    beforeSend: function() {
		    	showLoader()
		    },
		    success: (response) => {
		        const { message } = response
				showAlert({ message })
				closeLoader()
		    },
		    error: (error) => {
		    	const { message } = error.responseJSON
				showAlert({ message })
				closeLoader()
		    }
		});
	})

	$(".save-btn").click(function() {
		const data = getInput()
		const isValidate = validate(data)
		if(!isValidate) return

		$.ajax({
		    url: "/admin/ajax/post/add_admin/",
		    type: 'POST',
		    data: {
		        csrfmiddlewaretoken: csrfToken,
		        data: JSON.stringify(data),
		        site_key: $(".sitekey-input").val()
		    },
		    beforeSend: function() {
		    	showLoader()
		    },
		    success: (response) => {
		        const { message } = response
				showAlert({ message })
				closeLoader()
		    },
		    error: (error) => {
		    	const { message } = error.responseJSON
				showAlert({ message })
				closeLoader()
		    }
		});
	});

	$(".delete-btn").click(function() {
		const thisEle = $(this)
		const email = thisEle.data("email")
		const deleted = thisEle.data("deleted")
		const deleteAdmin = deleted ? false : true
		modifyAdmin(deleteAdmin, email)
	});


	function getInput() {
	  const settingsInput = $(".outter-add-admin-modal-con .icon-input")
	  const data = {}

	  settingsInput.each((_, ele) => {
	    const thisEle = $(ele)
	    const name = thisEle.data("key")
	    const value = thisEle.val() 
	    data[name] = value
	  })

	  if( Object.keys(data).length < 4) return 

	  return data
	}

	function modifyAdmin(deleteAdmin, email) {
		$.ajax({
		    url: "/admin/ajax/post/update_admin/",
		    type: 'POST',
		    data: {
		        csrfmiddlewaretoken: csrfToken,
		        data: JSON.stringify({ deleted: deleteAdmin, email }),
		        site_key: $(".sitekey-input").val()
		    },
		    beforeSend: function() {
		    	showLoader()
		    },
		    success: (response) => {
		        const { message } = response
				showAlert({ message })
				$(`.status-tick[data-email="${email}"]`).text(deleteAdmin ? "inactive" : "active")
				$(`.delete-btn[data-email="${email}"]`).data("deleted", deleteAdmin).text(deleteAdmin ? "add" : "delete")
				closeLoader()
		    },
		    error: (error) => {
		    	const { message } = error.responseJSON
				showAlert({ message })
				closeLoader()
		    }
		});
	}

	function validate({ username, email, password, confirm }) {
		if (!username || !email || !password || !confirm) {
			showAlert({ message: `missing inputs`})
			return false
		}

		if (password != confirm) {
			showAlert({ message: `confirm and password are not the same`})

			return false
		}

		if (confirm.length < 8) {
			showAlert({ message: `password is too short, it should be atleast 8 characters long`})

			return false
		}

		return true
	}
})();

