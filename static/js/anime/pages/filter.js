(function () {
  $(".apply-btn").click(function () {
    const data = getInputs(".filter-select")
    const url = buildUrl(data)
    window.location.href = url;
  });
})();

function buildUrl(params) {
    const query = new URLSearchParams(params).toString();
    return `/${type}/filter/${query ? `?${query}` : ''}`;
}

