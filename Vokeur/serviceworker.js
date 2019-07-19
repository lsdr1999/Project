var staticCacheName = 'VokeurCache';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        "/",
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match("/"));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});

// https://www.freecodecamp.org/news/i-built-a-pwa-and-published-it-in-3-app-stores-heres-what-i-learned-7cb3f56daf9b/

// in settings
// PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'website/static/website', 'serviceworker.js')
// pwa, toevoegen bij installed apps

// in urls
// path("", include("pwa.urls")),

// in layout
// {% load pwa %}
// {% progressive_web_app_meta %}

// in views
// def base_layout(request):
//      return render(request, "index.html")
