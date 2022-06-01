const nav = document.getElementById('nav');
    window.addEventListener('scroll', () => {
      if (window.scrollY >= 100) {
        nav.classList.add('nav__black');
      } else {
        nav.classList.remove('nav__black');
      }
    });

$(document).ready(function () {
    $('.details').hide()

    $('.poster').on('mouseenter', function() {
      $(this).children('.row__poster').addClass('blur')
      $(this).children('.details').fadeIn( "slow")
    })

    $('.poster').on('mouseleave', function() {
      $(this).children('.row__poster').removeClass('blur')
      $(this).children('.details').fadeOut( "slow")
    })
})
