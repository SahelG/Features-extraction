import os
import glob

def cambiar_nombre_imagenes(directorio, prefijo):
    archivos = glob.glob(os.path.join(directorio, "*.bmp"))

    i = 1
    for archivo in archivos:
        ruta, nombre = os.path.split(archivo)
        nuevo_nombre = f"{prefijo}{i}{os.path.splitext(nombre)[1]}"
        nuevo_archivo = os.path.join(ruta, nuevo_nombre)
        os.rename(archivo, nuevo_archivo)
        print(f"Archivo {archivo} renombrado como {nuevo_archivo}")
        i += 1

directorio = "C:/Users/Apeach/Desktop/DATOS/pollen/2/MASK/MASK_2"
prefijo = "pm"

cambiar_nombre_imagenes(directorio, prefijo)
fc7 =  svg16("multi1.bpm")
