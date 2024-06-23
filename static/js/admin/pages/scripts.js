(function () { 
	saveBtn.click(function() {
	  const data = getSettingsInput()
	  saveSettings({data})
	});
})();
