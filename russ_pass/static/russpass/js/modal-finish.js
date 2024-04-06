document.addEventListener("DOMContentLoaded", function() {
    // Получаем последний слайдер
    var lastSlide = document.querySelector(".swiper-slide:last-child");
    
    // Проверяем, что слайдер существует
    if (lastSlide) {
        // Подождать 1.5 секунды перед показом блока .finish
        setTimeout(function() {
            var finishBlock = document.querySelector(".finish");
            if (finishBlock) {
                finishBlock.style.display = "block";
            }
        }, 1500);
    }

    // Обработчик для кнопки закрытия
    var closeButton = document.querySelector(".btn-close");
    if (closeButton) {
        closeButton.addEventListener("click", function() {
            var finishBlock = document.querySelector(".finish");
            if (finishBlock) {
                finishBlock.style.display = "none";
            }
        });
    }
});