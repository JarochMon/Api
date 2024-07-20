# REST API para Simulación de Predicción

## Información del Servicio

Este servicio REST API simula un modelo de predicción utilizando Flask y Docker. Proporciona un endpoint para obtener una predicción simulada y una página de bienvenida.

- **API Base URL**: `http://localhost:5000`
- **Framework**: Flask
- **Contenedor**: Docker

## Requerimientos

Para utilizar este servicio, necesitas tener instalados los siguientes requisitos:

- Docker: [Descargar Docker](https://www.docker.com/products/docker-desktop)

## Instalación

### 1. Clonar el Repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/JarochMon/Api.git
cd Api

## Uso (Producción)

Una vez que el contenedor esté en funcionamiento, puedes interactuar con la API a través de los siguientes endpoints.

### Endpoint de Bienvenida

- **URL**: `/`
- **Método**: `GET`
- **Descripción**: Muestra una página de bienvenida.

**Ejemplo de Solicitud:**

```bash
curl http://localhost:5000/

## Uso (Desarrollo)

Para el desarrollo, puedes seguir estos pasos:

1. **Modificar el Código**: Realiza cambios en el archivo `app.py` y otros archivos del proyecto según sea necesario.

2. **Rebuild la Imagen Docker**: Después de hacer cambios en el código, reconstruye la imagen Docker para reflejar las actualizaciones.

   ```bash
   docker build -t prediccion-api .
