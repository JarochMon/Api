REST API para Simulación de Predicción

Información del Servicio

Este servicio REST API simula un modelo de predicción utilizando Flask y Docker. Proporciona un endpoint para obtener una predicción simulada y una página de bienvenida.


API Base URL: http://localhost:5000

Framework: Flask

Contenedor: Docker}

Requerimientos
Para utilizar este servicio, necesitas tener instalados los siguientes requisitos:

Docker: Descargar Docker

Instalación

1. Clonar el Repositorio
Primero, clona el repositorio en tu máquina local:


Copiar código
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
2. Construir la Imagen Docker
Construye la imagen Docker para el servicio:

bash
Copiar código
docker build -t prediccion-api .
3. Ejecutar el Contenedor
Inicia el contenedor Docker:

bash
Copiar código
docker run -p 5000:5000 prediccion-api
Uso (Producción)
Una vez que el contenedor esté en funcionamiento, puedes interactuar con la API a través de los siguientes endpoints.

Endpoint de Bienvenida
URL: /
Método: GET
Descripción: Muestra una página de bienvenida.
Ejemplo de Solicitud:

bash
Copiar código
curl http://localhost:5000/
Respuesta Esperada:

html
Copiar código
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>Bienvenido a la API de Predicción</h1>
</body>
</html>
Endpoint de Predicción
URL: /predict
Método: POST
Descripción: Devuelve una predicción simulada.
Ejemplo de Solicitud:

bash
Copiar código
curl -X POST http://localhost:5000/predict
Respuesta Esperada:

json
Copiar código
{
  "prediction": "Resultado simulado"
}
Uso (Desarrollo)
Para el desarrollo, puedes seguir estos pasos:

Modificar el Código: Realiza cambios en el archivo app.py y otros archivos del proyecto según sea necesario.

Rebuild la Imagen Docker: Después de hacer cambios en el código, reconstruye la imagen Docker para reflejar las actualizaciones.

bash
Copiar código
docker build -t prediccion-api .
Reiniciar el Contenedor: Si el contenedor está en ejecución, deténlo y vuelve a iniciarlo para aplicar los cambios.

bash
Copiar código
docker stop <container-id>
docker run -p 5000:5000 prediccion-api
Ver Logs: Para ver los logs del contenedor, utiliza:

bash
Copiar código
docker logs <container-id>
Nota: Asegúrate de tener Docker y el archivo Dockerfile correctamente configurados para reflejar los cambios en el entorno de desarrollo.

Enlace al Repositorio Público
Puedes encontrar el repositorio público del proyecto en:

https://github.com/tu-usuario/tu-repositorio
