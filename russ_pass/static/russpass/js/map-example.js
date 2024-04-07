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
            `<div style="display:flex; align-items: center">
                <div class="wrapper-camera">
                   <input type="file" class="input-map" id="map-local" capture="user" style="display:none">
                   <label for="map-local" style="cursor:pointer; margin-right: 10px">
                       <img src="/static/russpass/img/camera.png"/>
                   </label>
                </div>
                <div class="wrapper-content" >
                    <div style="font-size:14px">Загрузи фото этой точки <br> и получи очки и бонусы</div>
                    <div style="display:flex; align-items: center">
                        <div style="display:flex; align-items: center; margin-right: 10px">
                             <img src="/static/russpass/img/icon/bonus.png">
                             <div class="title" style="font-size: 12px; color: #2D3134; font-weight: 600;">+ 15</div>
                        </div>
                        <div style="display:flex; align-items: center">
                            <img src="/static/russpass/img/icon/ruk.png">
                            <div class="title" style="font-size: 12px; color: #2D3134; font-weight: 600;">+ 8</div>
                        </div>
                    </div>
                </div>
            </div>
            `,
        ].join('')
    }, {
        preset: 'islands#redDotIcon'
    });

    myMap.geoObjects.add(myPlacemark);
});
