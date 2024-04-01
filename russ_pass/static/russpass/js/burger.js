const dataBurger = document.querySelector('[data-burger]')
const mainNavigation = document.querySelector('.main-navigation')
const storag = document.querySelector('.storag')

dataBurger.addEventListener('click', (e) => {
    mainNavigation.classList.toggle('main-navigation--active')
    storag.classList.toggle('storag--active')
})