ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map('map', {
            center: [56.8, 60.7], // Екатеринбург
            zoom: 11,
            controls: ['zoomControl']
        })
    // Загрузка XML данных.
    // var data = ymaps.geoXml.load("https://mapofinterestgpx.ucoz.net/mapofinterest-vokrug_iseti.gpx")
    var data = ymaps.geoXml.load("https://filepomoika.ucoz.net/load/0-0-0-3-20")

    // Загрузка производится асинхронно.
    data.then(function(res) {
        // Установка пресета.
        res.geoObjects.options.set({
            "preset": "gpx#plain"
        });
        // Добавление объектов на карту.
        myMap.geoObjects.add(res.geoObjects);
    });
}


