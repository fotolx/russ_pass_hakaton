const apiKey = '23422f44d0a84bd05ebd4b7d0cdd0156';
const apiUrl = `https://api.openweathermap.org/data/2.5/forecast?q=Moscow&appid=${apiKey}&units=metric`;

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    const forecast = data.list.filter(item => item.dt_txt.includes('12:00:00'));
    const weatherForecast = document.getElementById('weatherForecast');

    forecast.forEach(item => {
      const date = new Date(item.dt * 1000);
      const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
      const dayOfWeek = days[date.getDay()];

      const card = document.createElement('div');
      card.classList.add('card');

      const icon = document.createElement('img');
      icon.classList.add('weather-icon');
      icon.src = `https://openweathermap.org/img/wn/${item.weather[0].icon}.png`;
      icon.alt = item.weather[0].description;

      const temperature = document.createElement('div');
      temperature.classList.add('temperature');
      temperature.textContent = `${Math.round(item.main.temp)}°C`;

      const time = document.createElement('div');
      time.classList.add('time');
      time.textContent = dayOfWeek;

      card.appendChild(icon);
      card.appendChild(temperature);
      card.appendChild(time);

      weatherForecast.appendChild(card);
    });
  })
  .catch(error => console.log('Error fetching weather data:', error));