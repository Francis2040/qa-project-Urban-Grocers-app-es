# QA Project: Urban Grocers App
Este proyecto permite la creación de kits personalizados para usuarios específicos mediante la aplicacion Urban Grocers. Incluye un conjunto de pruebas automatizadas para validar diversos casos de uso relacionados con la longitud y el formato del campo name en el cuerpo de la solicitud.

## Descripción:

La API permite:

Crear un nuevo usuario y obtener un token de autenticación.

Crear un kit asociado a un usuario específico utilizando el token de autenticación.

Validar la creación del kit mediante un conjunto de pruebas automatizadas que verifican diferentes escenarios de entrada.


### Bibliotecas:

requests

copy

json

pytest

#### Autenticación:

Para interactuar con la API, es necesario obtener un token de autenticación:

Envía una solicitud para crear un nuevo usuario.

Extrae el authToken de la respuesta.

Utiliza este token en el encabezado Authorization para crear un kit asociado al usuario.

##### Estructura de archivo:

├── configuration.py

├── data.py

├── sender_stand_request.py

├── create_kit_name_kit_test.py

├── README.md

└── .gitignoreArchivos

configuration.py: Contiene la URL base y las rutas de la API.

data.py: Contiene los cuerpos base para crear usuarios y kits.

sender_stand_request.py: Maneja las solicitudes HTTP a la API.

create_kit_name_kit_test.py: Contiene las pruebas automatizadas según la lista de comprobación.

.gitignore: Archivos que no deben subirse al repositorio.


###### Cómo ejecutar las pruebas
Asegúrate de tener `pytest` y `requests` instalados

```bash
pip install pytest requests
