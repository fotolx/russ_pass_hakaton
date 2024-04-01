window.addEventListener('DOMContentLoaded', () => {
    let cartItem = document.querySelectorAll('.card-product')

    cartItem.forEach(function (el) {
        const btnDelete = el.querySelector('.card-delete')
        btnDelete.addEventListener('click', deleteItemShop)
    })
    function deleteItemShop(item) {
        item.target.closest('.card-product').remove()

        updateStorage()
    }
})