import pandas as pd
import json
import datetime

def convertir_fecha(valor):
    try:
        # Excel guarda fechas como número de días desde 1899-12-30
        base = datetime.datetime(1899, 12, 30)
        return (base + datetime.timedelta(days=int(valor))).strftime("%d/%m/%Y")
    except:
        # Si ya es texto o NaN, lo devuelve tal cual
        return str(valor) if pd.notna(valor) else ""

def normalizar_telefono(valor):
    if pd.isna(valor):
        return ""
    telefono = str(valor)
    telefono = telefono.replace("-", "").replace(" ", "").replace(".", "")
    return telefono

def excel_a_json(archivo_excel, archivo_json):
    # Leer Excel
    df = pd.read_excel(archivo_excel)

    registros = []
    for _, fila in df.iterrows():
        registros.append({
            "ESTABLECIMIENTO": fila.get("ESTABLECIMIENTO", ""),
            "Ubicación": fila.get("Ubicación", ""),
            "Director": fila.get("Director", ""),
            # Ajustá aquí el nombre exacto de la columna de teléfono en tu Excel
            "Teléfono": normalizar_telefono(fila.get("Teléfono part", "")),
            "Domicilio": fila.get("Domicilio", ""),
            "e-mail": fila.get("e-mail", ""),
            "CUE": fila.get("CUE", ""),
            "Edificio": fila.get("Edificio", ""),
            "Creación": convertir_fecha(fila.get("Creación", "")),
            "Nombre": fila.get("Nombre", "")
        })

    # Guardar JSON
    with open(archivo_json, "w", encoding="utf-8") as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    excel_a_json("lista.xlsx", "instituciones.json")
