window.addEventListener('load', function () {
  var homeCarouselEl = document.querySelector('#home-img-carousel')
  if (homeCarouselEl) {
    new Splide('#home-img-carousel', {
      type: 'loop',       // Keeps the slider looping infinitely
      autoWidth: true,
      gap: '1rem',        // Adds space (16px) between the images

      focus: 'center',
      trimSpace: false,

      perMove: 1,
      speed: 800,
      easing: 'cubic-bezier(0.25, 1, 0.5, 1)',

      autoplay: true,
      interval: 4000,
      
      pauseOnHover: false, // Prevents mouse hover from permanently freezing it
      pauseOnFocus: false, // Prevents clicks from permanently freezing it

      reducedMotion: {
          speed: 800,
          rewindSpeed: 800,
          autoplay: 'play'
      },

      pagination: false,

      breakpoints: {
        900: {
          perMove: 1,
        },
        600: {

          perMove: 1,
        }
      }
    }).mount();
  }

  var testimonialSliderEl = document.querySelector('.testimonial-slider');
  if (testimonialSliderEl) {
    new Splide('.testimonial-slider', {
      type: 'loop',       // Keeps the slider looping infinitely
      gap: '1200px',        // Adds space (16px) between the images

      focus: 'center',
      trimSpace: false,

      perMove: 1,
      speed: 800,
      easing: 'cubic-bezier(0.25, 1, 0.5, 1)',

      autoplay: true,
      interval: 4000,
      
      pauseOnHover: false, // Prevents mouse hover from permanently freezing it
      pauseOnFocus: false, // Prevents clicks from permanently freezing it

      reducedMotion: {
          speed: 800,
          rewindSpeed: 800,
          autoplay: 'play'
      },

      pagination: false,

      breakpoints: {
        900: {
          perMove: 1,
        },
        600: {

          perMove: 1,
        }
      }
    }).mount();
  }
});