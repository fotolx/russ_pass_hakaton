const burgerDashbord = document.querySelector('[data-burger-dashbord]');
const menuDashbord = document.querySelector('.dasbord-wrapper__menu')

burgerDashbord.addEventListener('click', () => {
    menuDashbord.classList.toggle('dasbord-wrapper__menu--active')
})