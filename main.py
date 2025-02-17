from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import conectar_postgreSQL as con
# instalar fastapi uvicorn
# para correr el proyecto uvicorn main:app --reload
app = FastAPI()
variable_precio = 1000
tarifa_parado = con.sql_select_one('precios', "estado = 'parado'")
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/r")
async def get_root(request: Request):
    return HTMLResponse(templates.TemplateResponse(
        request=request, name="index.html", context={"id": tarifa_parado})
    )

@app.get("/")
async def read_root():
    return HTMLResponse("""
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestión de Taxímetro</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 20px;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
            color: white;
        }
        .start { background-color: #3498db; } /* Azul */
        .stop { background-color: #e91e63; } /* Rosa */
        .config { background-color: #f39c12; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Taxímetro</h1>
        <p>Precio actual: <span id="precio">"""+ str(tarifa_parado) +"""</span> €</p>
        <p>Estado: <span id="estado">Parado</span></p>
        <button class="btn start" id="btnInicio">Iniciar Trayecto</button>
        <button class="btn stop" id="btnFin">Finalizar Trayecto</button>
        <button class="btn config" id="btnConfig">Configurar Tarifas</button>
        
        <div id="configPanel" class="hidden">
            <h3>Cambiar Tarifas</h3>
            <label>Precio en marcha (€): <input type="number" id="tarifaMarcha" step="0.01"></label><br>
            <label>Precio detenido (€): <input type="number" id="tarifaParado" step="0.01"></label><br>
            <button class="btn start" id="guardarTarifas">Guardar</button>
        </div>
    </div>
    
    <script>
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
    </script>
</body>
</html>

    """)
#    return templates.TemplateResponse(
#        request=request, name="index.html", context={"id": variable_precio}
#    )
