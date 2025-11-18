# Código modificado con nuevo campo PLA y registros CSV

import streamlit as st
import os
import csv

ARCHIVO = "impresoras.txt"
ARCHIVO_CSV = "registros.csv"

# Lista de impresoras
impresoras = [
    ["Ultimaker 1", "LIBRE", ""],
    ["Ultimaker 2", "LIBRE", ""],
    ["Ultimaker 3", "LIBRE", ""],
    ["Ultimaker 4", "LIBRE", ""],
    ["Bambu Lab", "LIBRE", ""],
    ["Creativity", "LIBRE", ""]
]

def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for imp in impresoras:
            f.write(",".join(imp) + "\n")

def cargar_datos():
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r") as f:
                lineas = f.readlines()
            for i in range(min(len(lineas), len(impresoras))):
                partes = lineas[i].strip().split(",")
                if len(partes) >= 3:
                    impresoras[i] = partes
                else:
                    impresoras[i] = [impresoras[i][0], "LIBRE", ""]
        except Exception as e:
            st.error(f"Error al cargar datos: {e}.")

def guardar_registro_csv(nombre, impresora, codigo, filamento):
    encabezado = ["carnet", "impresora", "codigo", "filamento_metros"]
    existe = os.path.exists(ARCHIVO_CSV)
    with open(ARCHIVO_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(encabezado)
        writer.writerow([nombre, impresora, codigo, filamento])

cargar_datos()

st.set_page_config(page_title="Sistema de Impresoras 3D D-HIVE", page_icon="🖨️")
st.title("🖨️ Sistema de Impresoras 3D D-HIVE")

menu = st.sidebar.radio("Menú", ["Ver estado de impresoras", "Solicitar impresora", "Liberar impresora", "Registros anteriores"])

if menu == "Ver estado de impresoras":
    st.subheader("📋 Estado actual de las impresoras")
    data = []
    for imp in impresoras:
        estado = "✅ LIBRE" if imp[1] == "LIBRE" else f"🚫 OCUPADA por {imp[1]}"
        data.append([imp[0], estado])
    st.dataframe(data, use_container_width=True, hide_index=True)

elif menu == "Solicitar impresora":
    st.subheader("🧾 Solicitud de impresora")

    nombre = st.text_input("Ingrese su número de carné:")
    filamento = st.number_input("Cantidad de filamento PLA (m)", min_value=0.0, step=0.1)

    libres = [i for i in range(len(impresoras)) if impresoras[i][1] == "LIBRE"]

    if len(libres) == 0:
        st.warning("⚠️ No hay impresoras disponibles en este momento.")
    else:
        opciones = [impresoras[i][0] for i in libres]
        seleccion = st.selectbox("Seleccione una impresora disponible:", opciones)

        if st.button("Solicitar impresora"):
            if not nombre.strip():
                st.error("Debe ingresar un número de carné.")
            else:
                idx = libres[opciones.index(seleccion)]
                codigo = str((idx + 1) * 1111)

                impresoras[idx][1] = nombre.strip()
                impresoras[idx][2] = codigo

                guardar_datos()
                guardar_registro_csv(nombre.strip(), impresoras[idx][0], codigo, filamento)

                st.balloons()
                st.success(f"✅ {impresoras[idx][0]} asignada a {nombre.strip()}.")
                st.info(f"🚨 CÓDIGO DE LIBERACIÓN: {codigo}")

elif menu == "Liberar impresora":
    st.subheader("🔓 Liberar impresora")

    ocupadas = [i for i in range(len(impresoras)) if impresoras[i][1] != "LIBRE"]

    if len(ocupadas) == 0:
        st.info("Todas las impresoras están libres.")
    else:
        opciones = [f"{impresoras[i][0]} (Carné: {impresoras[i][1]})" for i in ocupadas]
        seleccion = st.selectbox("Seleccione la impresora a liberar:", opciones)
        codigo = st.text_input("Ingrese el código de liberación:")

        if st.button("Liberar impresora"):
            idx = ocupadas[opciones.index(seleccion)]
            if codigo == impresoras[idx][2]:
                impresoras[idx][1] = "LIBRE"
                impresoras[idx][2] = ""
                guardar_datos()
                st.success(f"✅ {impresoras[idx][0]} ha sido liberada.")
            else:
                st.error("❌ Código incorrecto.")

elif menu == "Registros anteriores":
    st.subheader("📜 Registros anteriores")
    import pandas as pd
    if os.path.exists(ARCHIVO_CSV):
        df = pd.read_csv(ARCHIVO_CSV, header=0)
        df.columns = ["Carné", "Impresora", "Clave de desbloqueo", "Metros"]
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No hay registros guardados.")

st.markdown("---")
st.caption("Desarrollado para D-HIVE con ❤️ en Streamlit")
