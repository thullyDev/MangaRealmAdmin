(function () { 
	saveBtn.click(function() {
	  const data = getSettingsInput({ is_checkbox: true })
	  console.log({data})
	  saveSettings({data})
	});
})();
