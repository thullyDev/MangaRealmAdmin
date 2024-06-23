(function () {
	$(".menu-btn").click(() => showCloseEle(".mobile-viewer-con", "slide"));
	$(".open-search-btn").click(() => showCloseEle(".mobile-search-con", "slide"));
	$(".watch2gather-btn, .watch-room-modal-close-btn").click(() => showCloseEle(".watch-room-modal-con", "fade"));
	$(".create-watch-room-btn").click(() => createRoom())
	$(".search-btn").click(function () {
		const view = $(this).data("view")
		search($(`.search-input[data-view="${view}"]`))
	})
	$(".search-input").change(function () {
		search($(this))
	})
	$(".watch-room-input").keyup(function() {
		const thisEle = $(this)
		const limit = thisEle.data("limit")
		const value = $.trim(thisEle.val())
		const length = value.length
		$(".text-limit").text(`${length}/${limit}`)
	})

	$("input#checkbox-2-unlimited").click(function () {
		const thisEle = $(this)
		showCloseEle("input.watch-room-input[data-name='limit']", "fade")
	});
    showCloseEle(".preloader", "fade")

})();

function search(thisEle) {
	const value = thisEle.val()
	const type = thisEle.data("type")

	if (!value) return 

	const url = type == "latino" ? "/latino/search/" : "/main/filter/"
	const query = `${url}?keywords=${encodeURIComponent(value)}`
	window.location.href = query 
}

function getRoomInputs() {
  const inputs = $(".watch-room-input")
  const data = {}

  inputs.each((_, ele) => {
    const thisEle = $(ele)
    const name = thisEle.data("name")
    const value = thisEle.is(':checked') || $.trim(thisEle.val())  

    data[name] = value
  })

  return data
}

function createRoom() {
	data = getRoomInputs()
	const { room_name } = data

	if (room_name.length <= 10) {
		showAlert({ message: "room name should be atleast 10 characters long" })
		return
	}

	const captchaToken = getCaptchaResponse("auth_id_watch_rooms")

	if (captchaToken.length < 1) return


	data.csrfmiddlewaretoken = csrfToken
	data.captcha_token = captchaToken

	$.ajax({
	    data,
	    url: "/user/ajax/post/make_watch_room/",
	    type: 'POST',
	    beforeSend: function() {
	    	showLoader()
	    },
	    success: (response) => {
        const { message, room_id } = response
				showAlert({ message })
				closeLoader()
				window.location.replace(`/watch_rooms/${room_id}`)
	    },
	    error: (error) => {
	    	const { message, status_code } = error.responseJSON
				showAlert({ message })
				closeLoader()

				if(status_code == 403) popAuth()
    	}	
	});

}