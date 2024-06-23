(function () { 
	$("#profile-image-inp").change(function() {
	  const file = this.files[0];
	  const thisEle = $(this)

	  const reader = new FileReader();
	  reader.onload = function(e) {
	  	const callback = () => {
		  	const image = `<img src="${res}" alt="${username}" class="profile-image">`
		    $(".profile-image").html(image)
	  	}
	  	const res = e.target.result
	    changeUserDetails("profile_image", res, callback)
	  }
	  reader.readAsDataURL(file);
	});
	  
	$("input.list-search-inp").change(function() {
		const thisEle = $(this)
		const value = thisEle.val()

		if (!value) return
			
		const query = encodeURI(value)
		window.location.replace(`?keywords=${query}`)
	});

	$("input.username-inp").change(() => changeUsername());
	$("button.username-inp").click(() => changeUsername());
	$("button.delete-btn").click(function() {
		const thisEle = $(this)
		const slug = thisEle.data("slug")
		const anime_title = thisEle.data("title")

		$.ajax({
		    url: "/user/ajax/post/delete_list_item/",
		    type: 'POST',
		    data: {
		    	slug,
		    	anime_title,
		        csrfmiddlewaretoken: csrfToken,
		    },
		    beforeSend: function() {
		    	showLoader()
		    },
		    success: (response) => {
		        const { message } = response
				removeEle(slug)
				closeLoader()
		    },
		    error: (error) => {
		    	const { message } = error.responseJSON
				showAlert({ message })
				closeLoader()
		    }
		});
	});

})();


function changeUserDetails(type, value, callback = null) {
	$.ajax({
	    url: "/user/ajax/post/change_user_details/",
	    type: 'POST',
	    data: {
	    	type,
	    	value,
	        csrfmiddlewaretoken: csrfToken,
	    },
	    beforeSend: function() {
	    	showLoader()
	    },
	    success: (response) => {
	        const { message } = response
			showAlert({ message })
			if (callback) callback()
			closeLoader()
	    },
	    error: (error) => {
	    	const { message } = error.responseJSON
			showAlert({ message })
			closeLoader()
	    }
	});
}

function changeUsername() {
	const value = $("input.username-inp").val()
	changeUserDetails("username", value, () => {
		username = value
	})
}