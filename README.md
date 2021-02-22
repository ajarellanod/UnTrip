# Guia de Instalación de UnTrip

## Requerimientos necesarios para poder correr el proyecto

- Git
- Python v3.8.5 + pip
- Node v14.5.0 + npm

*Nota: Si eres usuario windows debes tener configurado*
*los tres programas en las variables de entorno de windows*

## Sigue los siguientes pasos

### Descarga el respositorio

- Crea una nueva carpeta para el proyecto

- Abre la cmd o terminal e ingresa desde ella a la nueva carpeta creada

- Corre el siguiente comando en tu terminal `git clone https://github.com/ajarellanod/UnTrip.git`

- Espera a que se descargue el proyecto


### Instala virtualenv y dependencias del backend

- Ingresa a la carpeta creada `UnTrip` desde tu terminal

- Corre el siguiente comando (solo si no tienes instalado virtualenv) > `pip install virtualenv`

- Luego que finalice la descarga exitosamente, corre el comando > `virtualenv env`

- Ingresa al directorio `env/scripts` desde tu terminal

- Si estas en windows corre el comando > `activate.bat` o en sistemas unix > `activate`

- `cd ../..` para regresar al directorio `UnTrip`

- Instala dependencias con el comando `pip install -r requirements.txt`


### Instala dependencias del frontend

- Abre una nueva cmd o terminal e ingresa desde ella al directorio `UnTrip/untrip/frontend`

- Ahi corre un nuevo comando `npm install`


### Inicia el Proyecto

Desde la primera cmd creada que se encuentra en la dirección `UnTrip` corre los siguientes comandos

- > `cd untrip`

- > `python manage.py migrate`

- > `python manage.py runserver`

Desde la segunda cmd creada que se encuentra en la dirección `UnTrip/untrip/frontend` corre el siguiente comando

- > `npm run serve`


### Visualiza el Proyecto

- Abre tu navegador

- Ingresa a `http://localhost:8080/` para la vista de usuario

- Ingresa a `http://localhost:8080/admin/create` para la vista de administrador