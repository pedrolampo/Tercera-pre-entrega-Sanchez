# Tercera preentrega Python 57825 -  Pedro Sanchez
---

## Entorno virtual
Activar el entorno virtual con el comando:
```sh
source entorno-virtual/Scripts/activate
```

## Correr el servidor
Para poner el servidor en funcionamiento, ejecutar:
```sh
python manage.py runserver
```
Con esto el servidor estará funcionando y podemos acceder a él desde http://127.0.0.1:8000/

## Navegación
Al correr el servidor y entrar a http://127.0.0.1:8000/ solo será visible un botón de redirección a la aplicación `BaseApp`.

La aplicación consiste de 4 vistas principales, y se puede navegar hacia cualquier de estas páginas desde la navbar de arriba de todo:
  - Inicio
  - Guitarras
  - Bajos
  - Clientes

Cada una de ellas (excepto inicio) tiene 2 botones, uno para insertar un nuevo item en la BD, y otro para buscar en la BD.    
Una vez ingresado a una sección, elegir la acción y llenar el formulario.

Si se elige insertar datos en la BD, al llenar el formulario serás redirigido a la página de Inicio, y podrás ver los cambios dentro de `db.sqlite3`.

Si se elige buscar datos, al llenar el formulario serás redirigido a `results.html` donde se mostrarán los datos correspondientes a tu búsqueda.

## Funcionamiento
La aplicación funciona de manera que al ingresar en cualquiera de las rutas mostradas en `BaseApp/urls.py` se llama a la función correspondiente de `BaseApp/views.py` y renderiza el template que le corresponda.

Al entrar a cualquiera de los 3 forms para ingreso de datos, se hace una petición HTPP POST de manera que se instancia un nuevo objecto del modelo correspondiente (`BaseApp/models.py`), y se llama al método `save()` para cargarlo en la BD.

Si se ingresa a los forms de búsqueda de información, al llenar el fomulario, se hace una petición GET del item correspondiente y se redirecciona al usuario a la url de resultados que usa el template `BaseApp/templates/BaseApp/results.html`, ejemplo: http://127.0.0.1:8000/BaseApp/search-results/?guitar=Epiphone.