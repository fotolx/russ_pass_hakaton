const btnLikeCard = document.querySelectorAll('.like');

btnLikeCard.forEach((el) => {
    el.addEventListener('click', (e) => {
        if (el.setAttribute('disabled')) {
            console.log('Кнопка уже недоступна');
        } else {
            console.log('Кнопка разблокирована!');
            el.setAttribute('disabled', true); // Добавить атрибут disabled после клика
        }
    });
});