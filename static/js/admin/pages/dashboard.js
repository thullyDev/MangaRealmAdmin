(function () {
	$(".table-search-btn").click(function() {
		searchTable(this)
	})

	$(".table-btn.disable").click(function() {
		const thisEle = $(this)
		const content = thisEle.data("content")
		const deleted = thisEle.data("deleted")
		const id = thisEle.data("id")
		const url = content == "animes" ? "/admin/ajax/post/update_anime/" : "/admin/ajax/post/update_user/"
		
		$.ajax({
		    url: url,
		    type: 'POST',
		    data: {
		        id: id,
		        data: JSON.stringify({ deleted }),
		        csrfmiddlewaretoken: csrfToken,
		    },
		    beforeSend: function() {
		    	showLoader()
		    },
		    success: (response) => {
		        const { message, data } = response
		        const { deleted } = data

		        thisEle.data("deleted", deleted)
		        thisEle.text(deleted ? "add" : "disable")
		        $(`.status-tick[data-id="${id}"]`).text(deleted ? "inactive" : "active")

				closeLoader()
		    },
		    error: (error) => {
		    	const { message } = error.responseJSON
				showAlert({ message })
				closeLoader()
		    }
		});
	})

	const searchTableInput = $(".table-search")
	searchTableInput.change(function() {
		searchTable(this)
	})

	function searchTable(ele) {
		const type = $(ele).data("type")
		const value = $(`.table-search[data-type="${type}"]`).val()
		if (!value) return 
		const query = encodeURI(value)
    	window.location.replace(`/admin/dashboard/?${type}_keywords=${query}`);
	}
})();

