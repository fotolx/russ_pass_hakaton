ymaps.ready(init);

function init() {
    var geolocation = ymaps.geolocation;

    // Получение данных о местоположении
    geolocation.get({
        provider: 'auto',
        mapStateAutoApply: true
    }).then(function (result) {
        // Получение информации о местоположении
        const city = result.geoObjects.get(0).properties.get('name');
        const country = result.geoObjects.get(0).properties.get('metaDataProperty').GeocoderMetaData.AddressDetails.Country.CountryName;

        document.getElementById('local').innerHTML = city + ', ' + country;
    });
}

