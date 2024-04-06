ymaps.ready(init);

function init() {
    var geolocation = ymaps.geolocation;

    geolocation.get({
        provider: 'auto',
        mapStateAutoApply: true
    }).then(function (result) {
        const city = result.geoObjects.get(0).properties.get('name');
        const country = result.geoObjects.get(0).properties.get('metaDataProperty').GeocoderMetaData.AddressDetails.Country.CountryName;
        const location = result.geoObjects.get(0).geometry.getCoordinates();

        const apiKey = '23422f44d0a84bd05ebd4b7d0cdd0156';
        const weatherUrl = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&lang=ru&appid=${apiKey}`;

        fetch(weatherUrl)
        .then(function(resp) {return resp.json() })
        .then(function(data) {
            console.log(data);
            const cardsContainer = document.getElementById('weather-cards');
            for (let i = 0; i < 4; i++) {
                const weatherData = data.list[i];
                const card = document.createElement('div');
                card.classList.add('weather-container__card');
                card.innerHTML = `
                    <div class="name-city">${data.city.name}</div>
                    <div class="features">
                        <img src="https://openweathermap.org/img/wn/${weatherData.weather[0].icon}@2x.png">
                    </div>
                    <div class="temp-city">${Math.round(weatherData.main.temp - 273)}&deg;</div>
                    <div class="current-time">${getNextHourTimeString(weatherData.dt)}</div>
                `;
                cardsContainer.appendChild(card);
            }
        });

        document.getElementById('local').innerHTML = city + ', ' + country;
    });
}

function getNextHourTimeString(timestamp) {
    const date = new Date(timestamp * 1000);
    date.setHours(date.getHours() - 3); 
    const hours = date.getHours();
    const minutes = (date.getMinutes() < 10 ? '0' : '') + date.getMinutes();
    return `${hours}:${minutes}`;
}
