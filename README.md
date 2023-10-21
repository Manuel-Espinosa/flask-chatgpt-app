# App Flask con Jinja2 - TESCHA

Este proyecto es parte de la materia de Inteligencia Artificial del Noveno semestre de la ingeniería en sistemas computacionales del TESCHA.

## Descripción:

Esta aplicación está diseñada con Flask y Jinja2 y se ejecuta dentro de un contenedor Docker.

## Pre-requisitos:

Antes de levantar la aplicación, es necesario crear dos redes en Docker:

```bash
docker network create backend
docker network create flaskapp
```

## Instrucciones para levantar la app:

- Clona este repositorio:
```git clone https://github.com/Manuel-Espinosa/ia-image-generator```

- Navega al directorio del proyecto:
```cd ia-image-generator```

- Utiliza docker-compose para levantar los servicios:
```docker-compose up```

### Nota: Como recomendación, no uses el argumento -d al usar docker-compose up para poder ver en tiempo real los registros (logs) que la aplicación genera, ademas debes crear tu archivo .env a partir del ejemplo .env-example en este repositorio.

## Licencia:

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.