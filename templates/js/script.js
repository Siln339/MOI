const button = document.querySelector('.route-window-toggler');
const route_container = document.querySelector('.route-container');
let parity_counter = 1;
function route_window_toggle(){
    if (parity_counter % 2 != 0){
        route_container.classList.add('active');
        parity_counter += 1;
    }
    else { 
        route_container.classList.remove('active');
        parity_counter += 1;
    }
}
button.addEventListener('click', route_window_toggle);