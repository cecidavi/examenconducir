document.getElementById('crearUsuarioForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Evitar el envío automático

    const form = event.target;
    const nombre = form.nombre.value.trim();
    const paterno = form.paterno.value.trim();
    const materno = form.materno.value.trim();
    const email = form.email.value.trim();
    const telefono = form.telefono.value.trim();
    const contrasena = form.contrasena.value.trim();

    // Expresiones regulares
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const telefonoRegex = /^\d{10}$/;

    // Validaciones personalizadas
    if (nombre.length === 0) {
        Swal.fire({
            title: '¡Error!',
            text: 'Debes ingresar tu nombre.',
            icon: 'error',
            confirmButtonText: 'Cerrar'
        });
        return;
    }

    if (paterno.length === 0) {
        Swal.fire({
            title: '¡Error!',
            text: 'Debes ingresar tu apellido paterno.',
            icon: 'error',
            confirmButtonText: 'Cerrar'
        });
        return;
    }

    if (materno.length === 0) {
        Swal.fire({
            title: '¡Error!',
            text: 'Debes ingresar tu apellido materno.',
            icon: 'error',
            confirmButtonText: 'Cerrar'
        });
        return;
    }

    if (!emailRegex.test(email)) {
        Swal.fire({
            title: '¡Error!',
            text: 'Debes ingresar un correo electrónico válido (ejemplo: usuario@dominio.com).',
            icon: 'error',
            confirmButtonText: 'Cerrar'
        });
        return;
    }

    if (!telefonoRegex.test(telefono)) {
        Swal.fire({
            title: '¡Error!',
            text: 'El número de teléfono debe tener exactamente 10 dígitos.',
            icon: 'error',
            confirmButtonText: 'Cerrar'
        });
        return;
    }

    if (contrasena.length < 4) {
        Swal.fire({
            title: '¡Error!',
            text: 'La contraseña debe tener al menos 4 caracteres.',
            icon: 'error',
            confirmButtonText: 'Cerrar'
        });
        return;
    }

    // Si todo pasa:
    Swal.fire({
        title: '¡Usuario Creado!',
        text: 'Tu registro fue exitoso. Ahora puedes iniciar sesión.',
        icon: 'success',
        confirmButtonText: 'Aceptar'
    }).then(() => {
        form.submit();  // Ahora sí enviamos el formulario
    });
});
