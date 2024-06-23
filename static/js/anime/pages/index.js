(function () {
	const slider = $(".features-swiper-wrapper");
	const slides = slider.children();
	const firstSlide = slides.first();
	const lastSlide = slides.last();

	const nextSlider = () => {
		const activeSlide = $(".swiper-slide.active")
		const nextSlide = activeSlide.next();

		if (nextSlide.length != 0) {
		    activeSlide.fadeOut(() => {
		      activeSlide.removeClass("active");
		      nextSlide.addClass("active").fadeIn();
		    });
		    return
		}

	    activeSlide.fadeOut(() => {
	      activeSlide.removeClass("active");
	      firstSlide.addClass("active").fadeIn();
	    }); 
	}

	const prevSlider = () => {
		const activeSlide = $(".swiper-slide.active")
		const prevSlide = activeSlide.prev();

	  if (prevSlide.length) {
	    activeSlide.fadeOut(() => {
	      activeSlide.removeClass("active");
	      prevSlide.addClass("active").fadeIn();
	    });
	    return
	  } 

	  activeSlide.fadeOut(() => {
	  	activeSlide.removeClass("active");
	  	lastSlide.addClass("active").fadeIn();
	  });
	};

	$(".swiper-button-next").click(() => nextSlider());
	$(".swiper-button-prev").click(() => prevSlider());
    setInterval(() => nextSlider(), 7000);
})();
