Aquí tienes un borrador de un README para GitHub.

<br>

📟 Sistema de Impresoras 3D D-HIVE
Este proyecto es una solución en Python para la gestión de impresoras 3D en entornos colaborativos como el laboratorio D-HIVE. El sistema facilita el control y la asignación de impresoras, optimizando el flujo de trabajo y la organización.

✨ Características Principales
Consulta de estado en tiempo real: Los usuarios pueden ver la disponibilidad de cada impresora.

Solicitud simplificada: Permite a los usuarios reservar una impresora disponible.

Códigos de uso únicos: Cada reserva genera un código único para seguimiento y verificación.

🚀 Funcionalidades Detalladas
Ver estado de impresoras
Muestra una lista completa de todas las impresoras 3D. El estado se indica de la siguiente manera:

DISPONIBLE: La impresora está libre y lista para ser utilizada.

OCUPADA: Muestra el nombre del usuario y el código de asignación, lo que permite identificar quién la está utilizando.

Solicitar una impresora
El proceso de solicitud es sencillo:

El usuario introduce su nombre.

El sistema presenta las impresoras que están DISPONIBLE.

Al seleccionar una, se genera automáticamente un código de uso único, que funciona como comprobante de la reserva.

🖨️ Impresoras Soportadas
El sistema está configurado para gestionar las siguientes impresoras:

Ultimaker 1

Ultimaker 2

Ultimaker 3

Ultimaker 4

Bambu Lab

Creativity

▶️ Guía de Uso
Para ejecutar el programa, clona este repositorio e inicia el script de Python:
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
python impresoras.py
<br>
Esperamos que este sistema sea de gran utilidad en el laboratorio. ¡A imprimir! 🚀
