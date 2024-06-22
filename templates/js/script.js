const route_container = document.querySelector('.route-container');
const propeties_container = document.querySelector('.propeties-container');
const route_arrow = document.querySelector('.route-arrow-container');

document.querySelector('.route-window-toggler').onclick = () => route_container.classList.toggle("active");
 
document.querySelectorAll('.submit-field').forEach((ob) => {
    console.log(ob);
    ob.onclick = () => loadRoute(ob.dataset.routeid); 
});

function loadRoute(routeid, response = false) {
    // alert(routeid);
    // if (response === false) {

    //     // Отправляем запрос к БД, полученныйы ответ переносим в responseData.

    //     loadRoute(routeid, responseData) // responseData - ответ от БД.
    //     return true;
    // }

    // Заполняем блок маршрута на основе данных, полученных в переменной response.
    
   // Закрываем страницу с маршрутом.
   swapContainer();
}

function swapContainer() {
    route_container.classList.add('fade-out');
    setTimeout(() => { propeties_container.classList.add('fade-in'); }, 150);
    route_arrow.onclick = (() => {
        propeties_container.classList.remove("fade-in");
        setTimeout(() => { route_container.classList.remove('fade-out'); }, 50);
        route_container.classList.remove('active');
    });
}

function fillRouteBlock(response) {
    document.querySelector(response).src = "img/urfu.png";
}

// function getRouteData {

// }

const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  });

