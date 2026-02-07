document.addEventListener("DOMContentLoaded", () => {
  // Hero Carousel Logic
  const slides = document.querySelectorAll('.hero-slide');
  const indicators = document.querySelectorAll('.indicator');
  const heroPrevBtn = document.getElementById('prev-slide');
  const heroNextBtn = document.getElementById('next-slide');
  let currentIndex = 0;
  const totalSlides = slides.length;
  let slideInterval;

  function showSlide(index) {
    // Ensure index is within bounds
    if (index < 0) index = totalSlides - 1;
    if (index >= totalSlides) index = 0;
    currentIndex = index;

    // Update slides
    slides.forEach((slide, i) => {
      if (i === currentIndex) {
        slide.classList.remove('opacity-0');
        slide.classList.add('opacity-100');
      } else {
        slide.classList.remove('opacity-100');
        slide.classList.add('opacity-0');
      }
    });

    // Update indicators (only if they exist)
    if (indicators.length > 0) {
      indicators.forEach((indicator, i) => {
        if (i === currentIndex) {
          indicator.classList.remove('h-3', 'bg-white/30');
          indicator.classList.add('h-12', 'bg-primary');
        } else {
          indicator.classList.remove('h-12', 'bg-primary');
          indicator.classList.add('h-3', 'bg-white/30');
        }
      });
    }
  }

  function nextSlide() {
    showSlide(currentIndex + 1);
  }

  function prevSlide() {
    showSlide(currentIndex - 1);
  }

  // Event Listeners - Enhanced touch support for mobile
  if (heroNextBtn) {
    heroNextBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      nextSlide();
      resetInterval();
    });
    heroNextBtn.addEventListener('touchend', (e) => {
      e.preventDefault();
      e.stopPropagation();
      nextSlide();
      resetInterval();
    });
  }

  if (heroPrevBtn) {
    heroPrevBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      prevSlide();
      resetInterval();
    });
    heroPrevBtn.addEventListener('touchend', (e) => {
      e.preventDefault();
      e.stopPropagation();
      prevSlide();
      resetInterval();
    });
  }

  // Swipe gesture support for mobile
  let touchStartX = 0;
  let touchEndX = 0;
  const carouselElement = document.getElementById('hero-carousel');

  if (carouselElement) {
    carouselElement.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, false);

    carouselElement.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }, false);
  }

  function handleSwipe() {
    const swipeThreshold = 50;
    if (touchStartX - touchEndX > swipeThreshold) {
      // Swiped left - next slide
      nextSlide();
      resetInterval();
    } else if (touchEndX - touchStartX > swipeThreshold) {
      // Swiped right - previous slide
      prevSlide();
      resetInterval();
    }
  }

  // Indicator click events
  indicators.forEach(indicator => {
    indicator.addEventListener('click', (e) => {
      const index = parseInt(e.target.dataset.index);
      showSlide(index);
      resetInterval();
    });
  });

  // Auto-play
  function startInterval() {
    slideInterval = setInterval(nextSlide, 5000); // Change slide every 5 seconds
  }

  function resetInterval() {
    clearInterval(slideInterval);
    startInterval();
  }

  if (totalSlides > 1) {
    startInterval();
  }
});


