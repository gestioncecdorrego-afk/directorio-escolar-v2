import pandas as pd
import sys

def excel_to_json(excel_file, json_file):
    # Leer el Excel
    df = pd.read_excel(excel_file)

    # Exportar a JSON (cada fila como objeto)
    df.to_json(json_file, orient="records", force_ascii=False)

    print(f"✅ Archivo {json_file} creado con éxito")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python convert_excel_to_json.py archivo.xlsx salida.json")
    else:
        excel_to_json(sys.argv[1], sys.argv[2])
