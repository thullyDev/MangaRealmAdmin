function getPage() {
	const currentURL = window.location.href;
	const urlParts = currentURL.split("/");

	return urlParts[urlParts.length - 2];	
}

function reloadPage() {
    window.location.reload();
}

function showAlert(message) {
    const alertBox = $(".alert-box")

    alertBox.fadeIn(function() {
        $(this).text(message)
    })

    const timeOut = 1500
    setTimeout(timeOut, alertBox.fadeOut())
}
