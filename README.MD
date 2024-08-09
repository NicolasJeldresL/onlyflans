# ONLYFLANS

ONLYFLANS es una aplicación web de ventas de postres creada con Python y Django.


### Tecnologías

- Python 3
- Django 5

### Descripción

El proyecto consiste en crear una aplicación web para una PYME de venta de postres, que permita el acceso a usuarios no registrados solo a su página principal y que además tenga una url a la cual solo podrán acceder aquellos usuarios que
estén registrados en el sistema.

### Características

- Registro e inicio de sesión de usuarios
- Navegación de postres disponibles
- Carrito de compras
- Realización de pedidos
- Gestión de pedidos por parte de los administradores

### Instalación y Configuración

#### Requisitos Previos

- Python 3.x
- Pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)

#### Pasos de Instalación

1. Clona el repositorio:

   ```bash
   git clone <https://github.com/ksm2024/onlyflans.git >
   cd onlyflans
   ```

2. Crea y activa un entorno virtual:

   ```bash
   virtualenv venv
   source venv/Scripts/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en un archivo `.env` (opcional):

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py makemigrations
   ```

   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario para acceder al panel de administración:

   ```bash
   python manage.py createsuperuser
   ```

7. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver

### Uso

1. Abre tu navegador web y navega a `http://127.0.0.1:8000/` para ver la página de inicio.
2. Usa el panel de administración en `http://127.0.0.1:8000/admin/` para gestionar el contenido de la aplicación.
3. Mensaje de texto `http://127.0.0.1:8000/text/`
4. Json `http://127.0.0.1:8000/json/`
5. Template `http://127.0.0.1:8000/template/`

### Rutas

- `/` - Página principal
- `/` - Página de ejemplo de plantilla

### Estructura del Proyecto

Una descripción rápida de la estructura de directorios principal:

```plaintext
onlyflans/
├── manage.py
├── onlyflans/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── web/
     __migrations
│   │__init__.py
│   │── admin.py
│   │── models.py
│   │── views.py
│   ├── urls.py
├── templates/
│   ├── index.html
│   ├── curriculum.html
├── static/
│   ├── css/styles.css
│   ├── js/index.js
│   ├── ...
├── ...
```

### Integrantes

- KATHERINE SILVA
    - [GitHub](<https://github.com/ksm2024/onlyflans.git>)

- NICOLÁS JELDRES   
    - [GitHub](<https://github.com/ksm2024/onlyflans.git>)

 
### Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva característica (`git checkout -b feature/nueva-caracteristica`).
3. Haz commit de tus cambios (`git commit -am 'Añadida nueva característica'`).
4. Empuja tu rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

### Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

### Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarnos a través de [email@example.com].



