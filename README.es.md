# Cyberark
  
Módulo para conectarse a Cyberark y manejar contraseñas 

*Read this in other languages: [English](README.md), [Portugues](README.pr.md), [Español](README.es.md).*

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Overview


1. Configurar credenciales Cyberark  
Configura credenciales para conectar con el API de Cyberark.

2. Obtener todas las Cajas fuertes  
Obtener todas las Cajas fuertes del Vault de CyberArk

3. Obtener Caja Fuerte  
Obtener información sobre una Caja Fuerte específica en el Vault.

4. Añadir Caja fuerte  
Añade una nueva Caja fuerte al Vault. El usuario debe tener permisos para añadir Cajas fuertes en el Vault.

5. Actualizar Caja fuerte  
Actualiza una sola Caja fuerte en el Vault de CyberArk

6. Eliminar Caja fuerte  
Eliminar Caja fuerte del Vault

7. Obtener todas las cuentas  
Obtener una lista de todas las cuentas en el Vault

8. Obtener cuenta  
Obtener información sobre una cuenta identificada por su ID

9. Añadir Cuenta  
Añade una nueva cuenta privilegiada o clave SSH al Vault

10. Eliminar Cuenta  
Eliminar Cuenta del Vault

11. Generar contraseña  
Genera una nueva contraseña para una cuenta existente. La contraseña se genera de acuerdo con la política de contraseñas definida en el sistema de destino.

12. Obtener el valor de la contraseña  
Recupera la contraseña o la clave SSH de una cuenta existente identificada por su ID de cuenta.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**python-requests**](https://pypi.org/project/python-requests/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)