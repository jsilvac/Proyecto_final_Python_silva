# Proyecto_final_Python_silva

###Entrega Final Python y utilizando Django.

## Descripción del Proyecto

Este proyecto en el cual utilizamos Python y Django, esta orientado en la administracion de un libreria, en la cual podremos agregar libros,clientes,trabajadores y realizar busqueda de libros, por el momento, la idea es lograr poder generar un sistema completo, con entrega según disponiblidad del libro,mientras exista el libro y el cliente correspondiente, gestionado por un trabajador x

#Datos de accesos a administrar panel de control de django:

- Usuario: admin
- Contraseña: a1313

- Usuario : usuario
- Contraseña : !7ZQ#CMeC+s9*2u

- Usuario : coder
- Contrasña : *coder_12345

##Descripción de estructura de carpetas y archivos :

### Rutas

- 127.0.0.1:8000/libreria/  => Pantalla de inicio o home del programa
- 127.0.0.1:8000/libros/    => Pantalla donde podras gestionar la creacion de nuevos Libros
- 127.0.0.1:8000/clientes/    => Pantalla donde podras gestionar la creacion de nuevos Clientes
- 127.0.0.1:8000/trabajadores/    => Pantalla don podras gestionar la creacion de nuevos Trabajadores
- 127.0.0.1:8000/busquedalibro/    => Pantalla donde podras buscar libros ya existentes en nuestra BD
- 127.0.0.1:8000/clientes_list/    => Pantalla donde visualizar los clientes ya existentes en nuestra BD
- 127.0.0.1:8000/perfil/    =>  Pantalla donde podras actualizar un usuario en particular
- 127.0.0.1:8000/register/    => Pantalla donde podrear crearte un usuario y ser registrado para tener acceso a los demas menus 
- 127.0.0.1:8000/messages/        => Pantalla donde se pueden enviar mensajes entre los usuarios registrados

## Uso del Programa

### clientes

- *Crear un cleinte*: Para crear un nuevo cliente:
  1. Aacceder con el boton clientes e iingresar datos solicitados.
  2. Finaliza dando al boton de agregar, lo cual creara el cliente en la base de datos.


### trabajadores

- *Agregar un trabajadores*: Para registrar a un nuevo trabajador:
  1. Aacceder con el boton trabajador e ingresar datos solicitados.
  2. Finaliza dando al boton de agregar, lo cual creara el trabajador en la base de datos09
### libros

- *Agregar un libro*: Para registrar a un nuevo libro:
  1. Aacceder con el boton libros e ingresar datos solicitados.
  2. Finaliza dando al boton de agregar, lo cual creara el nuevo libro en la base de datos.
 
### burcar libros

- *Buscar libros: Para buscar un libro o alguna coindidencia:
  1. Acceder con el boton buscar libro e ingresar el ISBN a buscar que representa a el libro.
  2. Al finalizar dando al boton de buscar, este te respondera con los resultados obtenidos en la BD.

### Mensajeria

- *Mensajeria: enviar mensaje entre usuarios:
1. Al acceder, encontrras un cuadro de texto donde debras ecribir el mensaje correspondiente.
2. Luego deberas elegis en To: a quien le enviaras el mensaje propiamente tal, recordar que solo aapreceran ususarios registrados 

### Registro / Perfil

- * registro usuario y actualizacion del usuario
1. En la pestaña de registro de usuario, podras crear un usuario para tener acceso a los menus disponibles
2. En la pestana de perfil, podras actualizar tu perfil, dependiendo de que lo que necesites actualizar.

### Login/Logout

- *Login y logout:
1. En este boton podras acceder con un usuario y contraseña registrado.
2. En caso de ya estar logeado, con este boton podras deslogearte.