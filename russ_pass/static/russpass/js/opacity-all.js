const next = document.querySelectorAll('.next');
const sliderWrapper = document.querySelectorAll('.card');

sliderWrapper.forEach((el) => {
    el.addEventListener('mouseover', (e) => {
        next.forEach((element) => {
            element.classList.add('next--active');
        });
    }); 
    el.addEventListener('mouseout', (e) => {
        // Проверяем, если событие произошло при наведении на .next
        if (!e.relatedTarget || !e.relatedTarget.matches('.next')) {
            next.forEach((element) => {
                element.classList.remove('next--active');
            });
        }
    }); 
});
