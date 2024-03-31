const CACHE_NAME = 'my-site-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/marhrut.html',
  '/css/style.css',
  '/css/normalize.css',
  '/js/teams.css',
  '/js/local.css',
  '/js/slider.css',
  '/js/carusel.css',
  '/js/tab.css',
  // Добавьте сюда другие ресурсы вашего сайта, которые нужно закэшировать
];

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Кэш или сеть
        return response || fetch(event.request);
      })
  );
});