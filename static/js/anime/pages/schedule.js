(function () {
  $(".day-label-con").click(function () {
    const thisEle = $(this)
    const day = thisEle.data("day")
    showCloseEle(`.mobile-day-animes-con[data-day="${day}"]`, "slide")
  });
})();

