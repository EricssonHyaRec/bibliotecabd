// Función para agregar productos a la tabla y calcular el precio final
document.getElementById("agregarProducto").addEventListener("click", function() {
    var nombre = document.getElementById("nombre_producto").value;
    var marca = document.getElementById("marca").value;
    var modelo = document.getElementById("modelo").value;
    var precio = document.getElementById("precio").value;
    var cantidad = document.getElementById("cantidad").value;

    if (nombre && precio && cantidad) {
        var tableBody = document.getElementById("productosTableBody");

        var precioTotal = (parseFloat(precio) * parseFloat(cantidad)).toFixed(2);

        var row = document.createElement("tr");

        row.innerHTML = `
            <td>${nombre} - ${marca} - ${modelo}</td>
            <td>${cantidad}</td>
            <td>S/ ${parseFloat(precio).toFixed(2)}</td>
            <td>S/ ${precioTotal}</td>
            <td><button class="btn btn-danger btn-sm borrarProducto"><i class="bi bi-trash"></i></button></td>
        `;

        tableBody.appendChild(row);

        // Limpiar los campos después de agregar el producto
        document.getElementById("formProducto").reset();

        // Actualizar el precio final
        actualizarPrecioFinal();

        // Funcionalidad para eliminar un producto de la tabla
        document.querySelectorAll(".borrarProducto").forEach(function(btn) {
            btn.addEventListener("click", function() {
                this.parentElement.parentElement.remove();
                actualizarPrecioFinal();  // Recalcular el precio final después de eliminar un producto
            });
        });
    }
});

// Función para actualizar el precio final
function actualizarPrecioFinal() {
    var tableBody = document.getElementById("productosTableBody");
    var rows = tableBody.getElementsByTagName("tr");
    var precioFinal = 0;

    for (var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        var precioTotalProducto = parseFloat(cells[3].innerText.replace("S/ ", ""));
        precioFinal += precioTotalProducto;
    }

    document.getElementById("precioFinal").innerText = `S/. ${precioFinal.toFixed(2)}`;
}

// Mostrar el modal de confirmación al intentar cancelar
document.getElementById("cancelarRegistro").addEventListener("click", function() {
    var modal = new bootstrap.Modal(document.getElementById("modalConfirmacion"));
    modal.show();
});

// Confirmar y proceder con la cancelación (borrar todos los productos de la tabla)
document.getElementById("confirmarCancelar").addEventListener("click", function() {
    var tableBody = document.getElementById("productosTableBody");
    tableBody.innerHTML = '';  // Borrar todos los productos de la tabla

    // Actualizar el precio final a cero
    actualizarPrecioFinal();

    // Cerrar el modal
    var modal = bootstrap.Modal.getInstance(document.getElementById("modalConfirmacion"));
    modal.hide();
});
