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
    await ymaps3.ready;

    const {YMap, YMapDefaultSchemeLayer} = ymaps3;

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
}
