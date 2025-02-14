let enMarcha = false;
document.getElementById('btnInicio').addEventListener('click', function() {
    enMarcha = true;
    document.getElementById('estado').innerText = "En marcha";
});

document.getElementById('btnFin').addEventListener('click', function() {
    enMarcha = false;
    document.getElementById('estado').innerText = "Parado";
});

document.getElementById('btnConfig').addEventListener('click', function() {
    let clave = prompt("Introduce la contraseña:");
    if (clave === "admin") {
        document.getElementById('configPanel').classList.toggle('hidden');
    } else {
        alert("Acceso denegado");
    }
});

document.getElementById('guardarTarifas').addEventListener('click', function() {
    let tarifaMarcha = document.getElementById('tarifaMarcha').value;
    let tarifaParado = document.getElementById('tarifaParado').value;
    localStorage.setItem('tarifaMarcha', tarifaMarcha);
    localStorage.setItem('tarifaParado', tarifaParado);
    alert("Tarifas actualizadas");
});