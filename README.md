# Guia de Instalación de UnTrip

## Requerimientos necesarios para poder correr el proyecto

* Git
* Python v3.8.5 + pip
* Node v14.5.0 + npm

## Sigue los siguientes pasos

### Descarga el respositorio

* Crea una nueva carpeta para el proyecto
* Abre la cmd o terminal e ingresa desde ella a la nueva carpeta creada
* Corre el siguiente comando en tu terminal `git clone https://github.com/ajarellanod/UnTrip.git`
* Espera a que se descargue el proyecto

### Instala Virtualenv

* Ingresa a la carpeta creada desde tu terminal
* Corre el siguiente comando > `pip install virtualenv`
* Luego que finalize la descarga > `virtualenv env`
* > `cd env/scripts`
* Si estas en windows > `activate.bat` o en sistemas unix > `activate`
* > `cd ../..`

### Instala dependencias del backend

> `pip install -r requirements.txt`

### Instala dependencias del frontend

* Abre una nueva cmd o terminal e ingresa desde ella al directorio `UnTrip/untrip/fronted`
* > `npm install`

### Inicia el Proyecto

* Desde la primera cmd creada que se encuentra en la dirección `UnTrip` corre los siguientes comandos
* > `cd untrip`
* > `python manage.py migrate`
* > `python manage.py runserver`

* Desde la segunda cmd creada que se encuentra en la dirección `UnTrip/untrip/fronted` corre los siguientes comandos
* > `npm run serve`
