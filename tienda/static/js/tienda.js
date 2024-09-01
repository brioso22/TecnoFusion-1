const abrirPopup = document.getElementById('abrir-popup');
const cerrarPopup = document.getElementById('cerrar-popup');
const popup = document.getElementById('popup');
const cartItems = document.getElementById('cart-items');

// Abrir la ventana emergente
abrirPopup.addEventListener('click', () => {
    popup.style.display = 'flex';
});

// Cerrar la ventana emergente
cerrarPopup.addEventListener('click', () => {
    popup.style.display = 'none';
});

// Cerrar la ventana emergente al hacer clic fuera del contenido
window.addEventListener('click', (e) => {
    if (e.target == popup) {
        popup.style.display = 'none';
    }
});


// Función para agregar un producto al carrito
function addToCart(nombre, precio) {
    const listItem = document.createElement('li');
    listItem.textContent = `${nombre} - $${precio}`;
    cartItems.appendChild(listItem);
}