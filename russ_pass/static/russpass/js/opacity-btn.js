const next = document.querySelector('.next')
const card = document.querySelector('.slider-wrapper ')

card.addEventListener('mouseover', (e) => {
    next.classList.add('next--active')
    console.log('sdsd')
}) 
card.addEventListener('mouseout', ()=> {
    next.classList.remove('next--active')
})