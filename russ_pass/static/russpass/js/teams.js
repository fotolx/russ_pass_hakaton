const flagCountry = document.querySelector('.flag-country');
  let clicked = false;

  flagCountry.addEventListener('click', () => {
    if (!clicked) {
      document.documentElement.style.setProperty('--color-black', '#fff');
      document.documentElement.style.setProperty('--color-white', '#2D3134');

      document.documentElement.style.setProperty('--color-boby', '#5B5F62');
      document.documentElement.style.setProperty('--color-gray', '#FAF8ED');
    } else {
      document.documentElement.style.setProperty('--color-black', '#2D3134');
      document.documentElement.style.setProperty('--color-white', '#fff');

      document.documentElement.style.setProperty('--color-boby', '#FAF8ED');
      document.documentElement.style.setProperty('--color-gray', '#5B5F62');
    }
    clicked = !clicked;
  });