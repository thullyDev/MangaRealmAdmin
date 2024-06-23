(function () {
	$(".watch-room-search").change(function () {
		const thisEle = $(this)
		const value = thisEle.val()


		if (!value) return 

		const url = "/watch_rooms/"
		const query = `${url}?keywords=${encodeURIComponent(value)}`

		window.location.href = query 
	})

	getRoomViews()
})();

function getRoomViews() {
  $.ajax({
	  url: liveChatBase + "/rooms_views/",
	  type: 'GET',
	  headers: {
	    'accept': 'application/json',
	    'Content-Type': 'application/json'
	  },
    success: (response) => {
    	const { data } = response
    	const { messages } = data
    	showViews(data)
    },
    error: (error) => {
    	console.log("something went wrong with trying to get the views")
    }
});
}

function showViews(rooms) {
	for (let [roomID, views] of Object.entries(rooms)) {
		$(`.room-tick-viewer[data-room-id="${roomID}"]`).html('<i class="fas fa-eye"></i> ' + views)
	}
}

