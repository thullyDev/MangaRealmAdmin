(function () { 
	saveBtn.click(function() {
	  const data = getSettingsInput()
	  saveSettings({data})
	});

	$(".settings-input.image-input").change(function() {
	  const file = this.files[0];
	  const thisEle = $(this)
	  const name = thisEle.data("name")
	  
	  const reader = new FileReader();
	  reader.onload = function(e) {
	  	const res = e.target.result
	    $(`.settings-image[data-name="${name}"]`).attr("src", res)
	    thisEle.data("value", res)
	  }
	  
	  reader.readAsDataURL(file);
	});
})();
