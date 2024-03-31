document.addEventListener("DOMContentLoaded", function () {
    const carousels = document.querySelectorAll('.carousel');
    
    carousels.forEach(function(carousel) {
        const cards = carousel.querySelectorAll('.card');
        const likeButton = carousel.querySelector('.like');
        const cardWidth = cards[0].offsetWidth;
        let currentPosition = 0;

        // Показать кнопку "Нравится"
        function showLikeButton() {
            likeButton.style.display = 'block';
        }

        // Скрыть кнопку "Нравится"
        function hideLikeButton() {
            likeButton.style.display = 'none';
        }

        // Переместить карусель на новую позицию
        function moveCarousel(position) {
            carousel.style.transform = `translateX(-${position + 30}px)`;
            carousel.style.transition = `all 0.5s ease`;
            currentPosition = position;
            // Проверяем, достигли ли конца карусели, чтобы скрыть или показать соответствующие кнопки
            if (currentPosition === 0) {
                carousel.parentElement.querySelector('.prev').style.display = 'none';
            } else {
                carousel.parentElement.querySelector('.prev').style.display = 'block';
            }
            if (currentPosition >= (cardWidth * (cards.length - 3))) {
                carousel.parentElement.querySelector('.next').style.display = 'none';
            } else {
                carousel.parentElement.querySelector('.next').style.display = 'block';
            }
        }

        // Переместить карусель на следующий слайд
        function nextSlide() {
            if (currentPosition < (cardWidth * (cards.length - 3))) {
                moveCarousel(currentPosition + cardWidth);
                hideLikeButton();
            }
        }

        // Переместить карусель на предыдущий слайд
        function prevSlide() {
            if (currentPosition > 0) {
                moveCarousel(currentPosition - cardWidth);
                showLikeButton();
            }
        }

        // Перемещение карусели по клику на кнопки
        carousel.parentElement.querySelector('.next').addEventListener('click', nextSlide);
        carousel.parentElement.querySelector('.prev').addEventListener('click', prevSlide);

        // Изначально скрываем кнопку "prev"
        carousel.parentElement.querySelector('.prev').style.display = 'none';
    });
});