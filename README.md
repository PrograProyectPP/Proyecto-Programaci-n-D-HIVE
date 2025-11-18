🖨️ Sistema de Gestión de Impresoras 3D — D-HIVE
Registro de uso | Control de impresoras | Historial CSV

Desarrollado con Streamlit y pensado para el laboratorio D-HIVE.

📌 Descripción del proyecto

Este sistema permite gestionar el uso de las impresoras 3D del laboratorio D-HIVE.
Incluye asignación de impresoras, liberación mediante código único, registro histórico y control de material utilizado (PLA en metros).

Este proyecto fue actualizado para mejorar el control del laboratorio y agregar registros automáticos en archivos CSV.

🆕 Nuevos cambios incluidos
✅ 1. Integración de base de datos en CSV para registros

Ahora el sistema guarda automáticamente en registros.csv:

Carné del usuario

Impresora asignada

Código único de liberación

Cantidad de filamento utilizado (en metros)

Estos datos permiten un historial organizado y exportable.

✅ 2. Nuevo registro de usuarios

Cada vez que un estudiante solicita una impresora:

Se registra su número de carné

Se asocia con la impresora utilizada

Se genera un código único de liberación

Se guarda su sesión en un archivo CSV

Esto permite un control más profesional y auditable.

✅ 3. Nuevo campo: “Metros de filamento PLA”

El usuario ahora ingresa:

Cantidad de filamento PLA (m)


El sistema guarda esos metros en el archivo CSV.

Esto permite controlar consumo de material para cálculo de costos, inventario y mantenimiento.

✅ 4. Actualización de archivos de estado

El archivo impresoras.txt guarda:

Nombre de impresora | Estado | Código de liberación


Esto permite mantener persistencia al reiniciar la app.

📂 Archivos incluidos
Archivo	Descripción
app.py (tu código)	Código principal en Streamlit
impresoras.txt	Estado actual de cada impresora
registros.csv	Historial completo de uso
impresoras.csv	(Opcional según tus pruebas)
🧠 Cómo funciona el sistema
🔹 1. Ver estado de impresoras

Muestra una tabla con:

Impresoras libres

Impresoras ocupadas

Nombre del usuario que la está utilizando

🔹 2. Solicitar impresora

El estudiante ingresa:

Carné

Metros de PLA a usar

El sistema:

Verifica disponibilidad

Asigna impresora

Genera un código de liberación

Guarda todo en impresoras.txt

Registra la sesión en registros.csv

🔹 3. Liberar impresora

El usuario:

Selecciona la impresora ocupada

Ingresa el código de liberación

El sistema:

Valida el código

Libera la impresora

Actualiza impresoras.txt

🔹 4. Registros anteriores

Lee el CSV y muestra el historial en una tabla con:

Carné

Impresora

Código

Metros utilizados

🚀 Cómo ejecutar
pip install streamlit pandas
streamlit run app.py

❤️ Créditos

Proyecto creado para el laboratorio D-HIVE
