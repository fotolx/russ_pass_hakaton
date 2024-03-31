document.addEventListener("DOMContentLoaded", function() {
    const prevButton = document.querySelector('.carusel-prev');
    const nextButton = document.querySelector('.carusel-next');
    const carousel = document.querySelector('.wrapper-carusel');
    const caruselCard = document.querySelectorAll('.carusel-card')

    nextButton.addEventListener('click', () => {
        carousel.scrollLeft += carousel.offsetWidth;
    });

    prevButton.addEventListener('click', () => {
        carousel.scrollLeft -= carousel.offsetWidth;
    });
});