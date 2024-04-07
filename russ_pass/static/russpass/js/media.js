const hero = document.querySelector('.hero')
const mediaQuery = window.matchMedia('(max-width: 1120px)')

if (mediaQuery.matches) {
    hero.style.backgroundImage = '#FFFBF3'
}