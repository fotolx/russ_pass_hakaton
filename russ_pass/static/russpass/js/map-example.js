ymaps.ready(function () {
    var myMap = new ymaps.Map('map-example', {
        center: [55.733835, 37.588227],
        zoom: 15,
        // Обратите внимание, что в API 2.1 по умолчанию карта создается с элементами управления.
        // Если вам не нужно их добавлять на карту, в ее параметрах передайте пустой массив в поле controls.
        controls: []
    });

    var myPlacemark = new ymaps.Placemark(myMap.getCenter(), {
        balloonContentBody: [
            `<div style="display:inline"><input type="file" class="input-map" id="map-local" accept="image/*" capture></div>
            <div style="font-size:14px">Загрузи фото этой точки и получи очки и бонусы</div>`,
        ].join('')
    }, {
        preset: 'islands#redDotIcon'
    });

    myMap.geoObjects.add(myPlacemark);
});
