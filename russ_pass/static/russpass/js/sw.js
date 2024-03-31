self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open('my-cache').then(function(cache) {
            return cache.addAll([
                '/index.html',
                '/marhrut.html',
                '/css/style.css',
                '/css/normalize.css',
                '/js/teams.css',
                '/js/local.css',
                '/js/slider.css',
                '/js/carusel.css',
                '/js/tab.css',
                // Добавьте сюда другие ресурсы вашего сайта
            ]);
        })
    );
});

