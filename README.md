# Api-Manager

Este es un backend diseñado para manejar las solicitudes web de una tienda cualquiera, fue creado sobre Django y Django REST Framework, utiliza sqlite3 como base de datos. Proporciona una interfaz de administración y una API. Para el deploy se utilizó una instacia gratis de Render y se puede visitar en el siguiente link: https://api-manager-x6lx.onrender.com/

## Django Framework

### Admin
Esta interfaz se utiliza para gestionar directamente los modelos ubicados en la base de datos. Al acceder a ella como un super-admin puedes realizar operaciones CRUD directamente en la base de datos sobre los modelos Purchase Requests, Request Lines y Users. Además puedes configurar grupos de usuarios para manejar juegos de datos entre ellos y elegir a quién permitir qué información ver.

Para acceder utilizar las siguientes credenciales:
- Username: superuser
- Password: superuser123

### API
La API soporta operaciones CRUD para los siguientes endpoints:

1. **Purchase Requests**: https://api-manager-x6lx.onrender.com/api/purchase_requests/
2. **Request Lines**: https://api-manager-x6lx.onrender.com/api/request_lines/

La relación entre Purchase Requests y Request Lines es de 1 a N, por lo tanto, el endpoint de Purchase Requests muestra las ordenes de compra y los ítems de ellas.

Las siguientes deciciones se tomaron asumiendo que las reglas de negocio no han sido establecidas y pueden cambiar a futuro:

* No se puede crear un Request Line sin asignarle un Purchase Request
* Se puede crear un Purchase Request con Request Lines vacíos

## Base de datos sqlite3
Django permite usar una base de datos interna, sin la necesidad de utilizar una base de datos que implique confiraciones extra. Sqlite3 crea un archivo con las tablas de los modelos. Este archivo debe subirse al repositorio de github para que el servicio de despliegue tenga acceso a el en producción. Esta práctica es común para proyectos de desarrollo personal, pero no es recomendada para proyectos grandes con clientes reales, debido a que implica subir datos sensibles a un repositorio de la web.

## Despliegue en Render
Para el deploy de esta applicación se utilizó render, donde se configuraron las varibles de entorno:

- ALLOWED_HOSTS = api-manager-x6lx.onrender.com,https://dashboard-kxki.onrender.com
- CORS_ALLOW_ALL_ORIGINS = True
- DEBUG = False
- SECRET_KEY = (llave secreta con valor alfanumérico)
- STATIC_URL = /static/

## Dependencias Utilizadas

- **asgiref**: Proporciona la infraestructura para la comunicación asíncrona en Django.
- **Django**: Framework web para el desarrollo de sitios web seguros y mantenibles.
- **django-cors-headers**: Maneja problemas de CORS para accesos seguros desde dominios cruzados.
- **djangorestframework**: Herramientas para construir APIs web, manejo de serialización y enrutamiento.
- **gunicorn**: Servidor WSGI para la implementación en producción de aplicaciones Python.
- **packaging**: Analiza y compara versiones de paquetes para la correcta gestión de dependencias.
- **sqlparse**: Analiza y formatea sentencias SQL, útil para debugging y configuración de bases de datos.
- **whitenoise**: Permite manejar archivos estáticos directamente desde Django.