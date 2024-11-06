function buscarProducto() {
    const input = document.getElementById('nombreProducto');
    const filter = input.value.toLowerCase();
    const table = document.querySelector('.tabla-estilo1 tbody');
    const rows = table.getElementsByTagName('tr');

    for (let i = 0; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        let found = false;

        if (cells.length > 0) {
            const nombreProducto = cells[0].textContent || cells[0].innerText; // Asumiendo que el nombre del producto está en la primera columna
            if (nombreProducto.toLowerCase().indexOf(filter) > -1) {
                found = true;
            }
        }

        rows[i].style.display = found ? "" : "none"; // Muestra la fila si se encuentra una coincidencia, de lo contrario, la oculta
    }
}

function filtrarPorPrecio() {
    const precioVentaInput = document.getElementById('precioVenta').value;
    const precioCompraInput = document.getElementById('preciocompra').value;
    const table = document.querySelector('.tabla-estilo1 tbody');
    const rows = table.getElementsByTagName('tr');

    for (let i = 0; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        let showRow = true; // Asumimos que la fila debe mostrarse

        if (cells.length > 0) {
            const precioVenta = cells[4].textContent.replace(/s\/\s*/, ''); // Obtener precio de venta de la columna correspondiente
            const precioCompra = cells[3].textContent.replace(/s\/\s*/, ''); // Obtener precio de compra de la columna correspondiente

            // Verificar si se ingresó un precio de venta para filtrar
            if (precioVentaInput && (parseFloat(precioVenta) < parseFloat(precioVentaInput))) {
                showRow = false; // No mostrar fila si el precio de venta es menor que el ingresado
            }

            // Verificar si se ingresó un precio de compra para filtrar
            if (precioCompraInput && (parseFloat(precioCompra) < parseFloat(precioCompraInput))) {
                showRow = false; // No mostrar fila si el precio de compra es menor que el ingresado
            }
        }

        rows[i].style.display = showRow ? "" : "none"; // Mostrar o ocultar la fila según la evaluación
    }
}

function filtrarPorCategoriaYModelo() {
    const categoriaSeleccionada = document.getElementById('categoria').value;
    const modeloSeleccionado = document.getElementById('modelo').value;
    const table = document.querySelector('.tabla-estilo1 tbody');
    const rows = table.getElementsByTagName('tr');

    for (let i = 0; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        let showRow = true; // Asumimos que la fila debe mostrarse

        if (cells.length > 0) {
            const categoriaProducto = cells[1].textContent.trim(); // Categoría en la segunda columna
            const modeloProducto = cells[2].textContent.trim(); // Modelo en la tercera columna

            // Verificar si se seleccionó una categoría para filtrar
            if (categoriaSeleccionada && categoriaProducto !== categoriaSeleccionada) {
                showRow = false; // No mostrar fila si la categoría no coincide
            }

            // Verificar si se seleccionó un modelo para filtrar
            if (modeloSeleccionado && modeloProducto !== modeloSeleccionado) {
                showRow = false; // No mostrar fila si el modelo no coincide
            }
        }

        rows[i].style.display = showRow ? "" : "none"; // Mostrar o ocultar la fila según la evaluación
    }
}
