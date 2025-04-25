document.getElementById('crearUsuarioForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Evitar envío normal

    const form = event.target;
    const email = form.email.value.trim();
    const telefono = form.telefono.value.trim();

    // Expresión regular para validar email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Validar correo
    if (!emailRegex.test(email)) {
        Swal.fire({
            title: '¡Error!',
            text: 'Ingresa un correo electrónico válido.',
            icon: 'error',
            confirmButtonText: 'Cerrar'
        });
        return;
    }

    // Validar teléfono (10 dígitos)
    if (!/^\d{10}$/.test(telefono)) {
        Swal.fire({
            title: '¡Error!',
            text: 'El número de teléfono debe tener exactamente 10 dígitos.',
            icon: 'error',
            confirmButtonText: 'Cerrar'
        });
        return;
    }

    // Si el formulario HTML también es válido (campos obligatorios)
    if (form.checkValidity()) {
        Swal.fire({
            title: '¡Éxito!',
            text: 'Usuario creado exitosamente.',
            icon: 'success',
            confirmButtonText: 'Aceptar'
        }).then(() => {
            form.submit(); // Ahora sí enviamos el formulario
        });
    } else {
        Swal.fire({
            title: '¡Error!',
            text: 'Por favor, completa todos los campos.',
            icon: 'error',
            confirmButtonText: 'Cerrar'
        });
        form.classList.add('was-validated');
    }
});
