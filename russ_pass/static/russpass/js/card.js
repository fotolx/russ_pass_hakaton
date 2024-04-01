const likeBtn = document.querySelectorAll('.like');
const listLocation = document.querySelector('.product-list');
const cart = document.querySelector('.card');


const generateCart = (id, img, title, text, num_r, km, level, icon_1, icon_2, icon_3, icon_4) => {
    return `
    <div class="card card--dasbord card-product" data-id="${id}">
    <img src="${img}" class="card__img" alt="">
    <a href="park.html" class="card__link card__link--dasbord">
        <div class="card__title">${title}</div>
    </a>
    <div class="card__text card__text--dasbord">${text}</div>
    <div class="card-lits">
        <div class="card-lits__item card-lits__item--dasbord">
            <svg width="23" height="20" viewBox="0 0 23 20" fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_178_413)">
                    <path
                        d="M10.4141 0.416511L7.8633 5.58839L2.15627 6.42042C1.13283 6.56885 0.722675 7.83057 1.46486 8.55323L5.59377 12.5767L4.61721 18.2603C4.44142 19.2876 5.52346 20.0571 6.42971 19.5767L11.5352 16.8931L16.6406 19.5767C17.5469 20.0532 18.6289 19.2876 18.4531 18.2603L17.4766 12.5767L21.6055 8.55323C22.3477 7.83057 21.9375 6.56885 20.9141 6.42042L15.2071 5.58839L12.6563 0.416511C12.1992 -0.505364 10.875 -0.517083 10.4141 0.416511Z" />
                </g>
                <defs>
                    <clipPath id="clip0_178_413">
                        <rect width="22.5" height="20" fill="white"
                            transform="translate(0.285156 -0.279297)" />
                    </clipPath>
                </defs>
            </svg>
            <span>${num_r}</span>
        </div>
        <div class="card-lits__item card-lits__item--dasbord">${km} км</div>
        <div class="card-lits__item card-lits__item--dasbord">${level}</div>
    </div>
    <div class="card-group">
        <div class="card-group__link card-group__link--dasbord">
            <img src="${icon_1}" alt="">
        </div>
        <div class="card-group__link card-group__link--dasbord">
            <img src="${icon_2}" alt="">
        </div>
        <div class="card-group__link card-group__link--dasbord">
            <img src="${icon_3}" alt="">
        </div>
        <div class="card-group__link card-group__link--dasbord">
            <img src="${icon_4}" alt="">
        </div>
    </div>
    <div class="load-marshrut">
    <span>25% Пройдено</span>
        <div class="load-marshrut__line"><span></span></div>
    </div>
    <button type="button" class="like like--dashbord">
        <svg width="20" height="20" viewBox="0 0 12 12" fill="none"
            xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_279_3945)">
                <path
                    d="M6.10914 2.31302L5.6879 2.67022L6.10914 3.1671L6.53039 2.67022L6.10914 2.31302ZM6.12571 11.0493L5.75746 11.4611C5.85867 11.5516 5.98967 11.6016 6.12543 11.6016C6.26119 11.6016 6.39219 11.5516 6.4934 11.4611L6.12571 11.0504V11.0493ZM6.53039 1.95637C5.265 0.464078 3.07763 0.00860548 1.42247 1.4352L2.1435 2.27217C3.25319 1.3154 4.74659 1.55942 5.6879 2.67022L6.53039 1.95637ZM1.42247 1.4352C-0.180238 2.81708 -0.412115 5.14026 0.853822 6.78383L1.38163 6.37756L1.72888 6.11028C0.823457 4.93433 0.981354 3.27365 2.14295 2.27161L1.42302 1.4352H1.42247ZM11.3639 6.78383C12.6254 5.14689 12.4294 2.80493 10.7897 1.43023L10.3211 1.98934L10.0803 2.27658C11.2535 3.25985 11.4003 4.92826 10.4894 6.11028L11.3639 6.78383ZM10.7897 1.43023C9.11692 0.0273766 6.9577 0.458557 5.68845 1.95637L6.53039 2.67022C7.46728 1.56494 8.94135 1.32147 10.0803 2.27658L10.3211 1.98934L10.7897 1.43023ZM0.854374 6.78383C1.34021 7.41431 2.36157 8.39758 3.33766 9.29417C4.3248 10.2018 5.3169 11.0675 5.75746 11.4611L6.4934 10.638C6.03848 10.2316 5.06515 9.38196 4.08464 8.4815C3.09309 7.57 2.14571 6.65133 1.72888 6.11028L1.38163 6.37756L0.854374 6.78383ZM6.4934 11.4611C6.93727 11.0647 7.91778 10.2013 8.89884 9.29252C9.86665 8.39537 10.8792 7.41321 11.3639 6.78383L10.4894 6.11028C10.0715 6.65298 9.13127 7.57166 8.14855 8.4826C7.17743 9.38251 6.20907 10.2344 5.75802 10.638L6.4934 11.4611Z"
                    fill="white" />
                <path
                    d="M3.60457 1.21694L6.15959 2.16908L8.85069 1.38034L10.2097 1.76085L11.161 3.17421L11.2425 4.72347L10.3999 6.95222L8.93223 8.93635L6.48604 10.4584L5.67064 10.4312L4.61062 9.50713L2.30033 7.22402L0.832617 5.45732L0.77798 3.47319L1.78375 1.92393L3.60457 1.21694Z"
                    fill="white" />
            </g>
            <defs>
                <clipPath id="clip0_279_3945">
                    <rect width="12.1459" height="11.0418" fill="white"
                        transform="translate(0.0419922 0.558105)" />
                </clipPath>
            </defs>
        </svg>
    </button>
    <button class="card-delete" aria-label="Удалить товар"><span>×</span></button>
</div>
`;
}

likeBtn.forEach(function (el) {
    el.addEventListener('click', function (event) {
        let self = event.currentTarget;
        let parent = self.closest('.card');
        let id = parent.dataset.id;
        let img = parent.querySelector('.card__img').getAttribute('src');
        let title = parent.querySelector('.card__title').textContent;
        let text = parent.querySelector('.card__text').textContent;
        let num_r = parent.querySelector('.reiting-card').textContent;
        let km = parent.querySelector('.km-card').textContent;
        let level = parent.querySelector('.level-card').textContent;
        let icon_1 = parent.querySelector('.icon-one').getAttribute('src');
        let icon_2 = parent.querySelector('.icon-two').getAttribute('src');
        let icon_3 = parent.querySelector('.icon-free').getAttribute('src');
        let icon_4 = parent.querySelector('.icon-fout').getAttribute('src');

        listLocation.insertAdjacentHTML('afterbegin', generateCart(id, img, title, text, num_r, km, level, icon_1, icon_2, icon_3, icon_4));

        updateStorage()
        self.disabled = true;

    })
})

// Изначальное состояние приложения
const initialState = () => {
    if (localStorage.getItem('tur') !== null) {
        listLocation.innerHTML = localStorage.getItem('tur')

        // Обработка активной кнопки
        const CartContentLocal = document.querySelectorAll('.card-product');
        for(let el of CartContentLocal) {
            let id = el.dataset.id;
            const idProduct = document.querySelector(`.card[data-id="${id}"]`);
            if(idProduct == undefined) continue;
            idProduct.querySelector('.like').disabled = true;
        };
    };
};
initialState();

// Функция, которая будет добавлять данные в локал стореж
const updateStorage = () => {
    let parent = listLocation
    let html = parent.innerHTML
    html = html.trim()

    if (html.length) {
        localStorage.setItem('tur', html)
    } else {
        localStorage.removeItem('tur')
    }
}

const clearStoreg = () => {
    window.localStorage.clear()
}

const winLoad = () => {
    window.location.reload()
}

