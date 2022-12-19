# proyecto-final
Mi proyecto final


Para correr el programa, realizar los siguientes pasos:

1 Abrir VSCode.

2 Seleccionar Clone git repository y agregar la URL de este proyecto.

3 Seleccionar o crear una carpeta para el programa.

4 En la terminal ejecuta los comandos: python manage.py migrate y python manage.py runserver

5 Ya se puede abrir la pagina que aparece en el texto, tipicamente: http://127.0.0.1:8000/

6 Si quieres tener algunos datos precargados, en la terminal, ejecuta los comandos:
    Para familiares: python manage.py shell < seed_data.py
    Para autos: python manage.py shell < seed_data_autos.py
    Para mascotas: python manage.py shell < seed_data_mascotas.py

En la web hay 3 tipos de listas: mi-familia, mis-autos y mis-mascotas

Agrega las url que ves abajo a la url en la barra de direcciones para utilizarlas

Ejemplo: para ver la lista de familiares agregar: /mi-familia
         para ver la lista de autos agregar: /mis-autos
         para ver la lista de mascotas agregar: /mis-mascotas
         

7 Dentro de cada lista tendras las opciones de agregar un nuevo elemento, borrar un elemento o 
  actualizar un elemento. 
  
8 para buscar un elemento en una lista determinada agregar a la URL:
    para familiares: /mi-familia/buscar
    para autos: /mis-autos/buscar-auto
    para mascotas: /mis-mascotas/buscar-mascotas

Gracias.



