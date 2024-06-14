const button = document.querySelector('.route-window-toggler');
const route_container = document.querySelector('.route-container');
let parity_counter = 1;
function route_window_toggle(){
    if (parity_counter % 2 != 0){
        route_container.classList.add('active')
        // route_container.classList.add('fade-out');
        parity_counter += 1;
    }
    else { 
        route_container.classList.remove('active')
        // route_container.classList.remove('fade-out');
        // route_container.classList.add('fade-in');
        parity_counter += 1;
    }
}
button.addEventListener('click', route_window_toggle);

const submit_button = document.querySelector('.submit-field');
const propeties_container = document.querySelector('.propeties-container');

// function route_window_toggle(submit_button){
//     if (data-routeid == '21'){
//         route_container.classList.add('active')
//         parity_counter += 1;
//     }
// }
