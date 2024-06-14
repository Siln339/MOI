const route_container = document.querySelector('.route-container');

document.querySelector('.route-window-toggler').onclick = () => route_container.classList.toggle("active");
 
document.querySelectorAll('.submit-field').forEach((ob) => {
    console.log(ob);
    ob.onclick = () => loadRoute(ob.dataset.routeid); 
});

function loadRoute(routeid, response = false) {
    if (response === false) {

        // Отправляем запрос к БД, полученныйы ответ переносим в responseData.

        loadRoute(routeid, responseData) // responseData - ответ от БД.
        return true;
    }

    // Заполняем блок маршрута на основе данных, полученных в переменной response.

    // Показываем блок.

    alert(routeid);
}

const propeties_container = document.querySelector('.propeties-container');

// function route_window_toggle(submit_button){
//     if (data-routeid == '21'){
//         route_container.classList.add('active')
//         parity_counter += 1;
//     }
// }
