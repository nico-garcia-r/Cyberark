# Cyberark
  
Módulo para conectarse a Cyberark y manejar contraseñas  

*Read this in other languages: [English](Manual_Cyberark.md), [Portugues](Manual_Cyberark.pr.md), [Español](Manual_Cyberark.es.md).*
  
![banner](imgs/Banner_Cyberark.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Configurar credenciales Cyberark
  
Configura credenciales para conectar con el API de Cyberark.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Usuario|Usuario para conectar con el API de Cyberark|Usuario|
|Contraseña|Contraseña para conectar con el API de Cyberark|********|
|URL|URL del API de Cyberark|https://cyberark.example.com|
|Asignar resultado a variable|Asignar resultado de la conexión a variable|result|

### Obtener todas las Cajas fuertes
  
Obtener todas las Cajas fuertes del Vault de CyberArk
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtrar por nombre|Filtra el resultado por el nombre de la Caja fuerte|nombre|
|Cantidad de resultados|Cantidad de resultados máximos que se retornarán en la variable|25|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Obtener Caja Fuerte
  
Obtener información sobre una Caja Fuerte específica en el Vault.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Caja Fuerte|URL ID de la Caja Fuerte|123456|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Añadir Caja fuerte
  
Añade una nueva Caja fuerte al Vault. El usuario debe tener permisos para añadir Cajas fuertes en el Vault.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la Caja fuerte|Nombre que tendrá la nueva Caja fuerte|CAJA-1|
|Descripción de la Caja fuerte|Descripción de la nueva Caja fuerte|Caja fuerte de prueba|
|Ubicación de la Caja fuerte|Ubicación de la nueva Caja fuerte. Por defecto es la ruta raíz.|//|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Actualizar Caja fuerte
  
Actualiza una sola Caja fuerte en el Vault de CyberArk
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Caja fuerte|ID de la Caja fuerte a actualizar|123456|
|Nuevo nombre de la Caja fuerte|Nuevo nombre que se le asignará a la Caja fuerte|NUEVO-NOMBRE|
|Nueva descripción de la Caja fuerte|Nueva descripción que se le asignará a la Caja fuerte|NUEVA-DESCRIPCION|
|Nueva ubicación de la Caja fuerte|Nueva ubicación que se le asignará a la Caja fuerte|//|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Eliminar Caja fuerte
  
Eliminar Caja fuerte del Vault
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Caja Fuerte|URL ID de la Caja Fuerte|123456|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Obtener todas las cuentas
  
Obtener una lista de todas las cuentas en el Vault
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtrar por nombre|Filtra el resultado por el nombre de la cuenta|nombre|
|Cantidad de resultados|Cantidad de resultados máximos que se retornarán en la variable|25|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Obtener cuenta
  
Obtener información sobre una cuenta identificada por su ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la cuenta|ID de la cuenta|123456|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Añadir Cuenta
  
Añade una nueva cuenta privilegiada o clave SSH al Vault
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la cuenta|Nombre que tendrá la cuenta creada|Nombre|
|PlatformId|Identificador de la plataforma asignada a la cuenta|WinServerLocal|
|Nombre de la Caja fuerte|Nombre de la caja fuerte donde se ubicará la cuenta|CAJA-1|
|Secret type|Tipo de secreto que se almacenará en la cuenta|key|
|Secret|Secreto que se almacenará en la cuenta|********|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Eliminar Cuenta
  
Eliminar Cuenta del Vault
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la cuenta|ID de la cuenta que será eliminada|123456|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Generar contraseña
  
Genera una nueva contraseña para una cuenta existente. La contraseña se genera de acuerdo con la política de contraseñas definida en el sistema de destino.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la cuenta|ID de la cuenta que será eliminada|123456|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Obtener el valor de la contraseña
  
Recupera la contraseña o la clave SSH de una cuenta existente identificada por su ID de cuenta.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la cuenta|ID de la cuenta que será eliminada|123456|
|Asignar resultado a variable|Asignar resultado a variable|result|

### Obtener contraseña del Central Credential Provider
  
Permite a las aplicaciones recuperar secretos del Central Credential Provider
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|URL del Central Credential Provider|100.10.2|
|Puerto|Puerto del servidor|22|
|AppID|Especifica el ID único de la aplicación que emite la solicitud de contraseña.|BillingApp|
|Nombre de la Caja fuerte|Especifica el nombre de la caja fuerte donde se almacena la contraseña.|SAFE-NAME|
|Carpeta|Especifica la carpeta donde se almacena la contraseña.|BILLING|
|Objeto|Especifica el nombre del objeto contraseña a recuperar.|MonthlyBilling|
|Nombre de Usuario|Define criterios de búsqueda según la propiedad de cuenta de nombre de usuario asignada.|user|
|Asignar resultado a variable|Asignar resultado a variable|result|
