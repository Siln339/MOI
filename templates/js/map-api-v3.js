initMap();

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

//console.log(httpGet("https://geocode-maps.yandex.ru/1.x/?apikey=9d41c8c3-eca5-4b49-9eaa-c08e88bbd00a&geocode=Екатеринбург&format=json"))

async function initMap() {
    // Промис `ymaps3.ready` будет зарезолвлен, когда загрузятся все компоненты основного модуля API
    await ymaps.ready;

    const {YMap, YMapDefaultSchemeLayer} = ymaps;

    // Иницилиазируем карту
    const map = new YMap(
        // Передаём ссылку на HTMLElement контейнера
        document.getElementById('map'),
        // Передаём параметры инициализации карты
        {
            location: {
                // Координаты центра карты
                center: [60.6, 56.81],
                // Уровень масштабирования
                zoom: 11,
                type: "yandex#satellite"
            }
        }

    );
    // Добавляем слой для отображения схематической карты
    map.addChild(new YMapDefaultSchemeLayer());

    // Загрузка XML данных.
    var data = ymaps.geoXml.load("drive.google.com/uc?export=download&id=164AOlTXR2yW9Gh3_vccwvmqvvErEEem9")

    // Загрузка производится асинхронно.
    data.then(function(res) {
        // Установка пресета.
        res.geoObjects.options.set({
            "preset": "gpx#plain"
        });
        // Добавление объектов на карту.
        map.geoObjects.add(res.geoObjects);
    });

}
