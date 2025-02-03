import os
import subprocess

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def abrir_en_editor(ruta_script):
    try:
        if os.name == 'nt':
            os.system(f'notepad {ruta_script}')
        else:
            os.system(f'nano {ruta_script}')
    except Exception as e:
        print(f"Error al abrir el editor: {e}")

def eliminar_script(ruta_script):
    try:
        os.remove(ruta_script)
        print(f"El archivo {ruta_script} ha sido eliminado.")
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")

def crear_script_nuevo(ruta_carpeta):
    nombre_nuevo = input("Ingrese el nombre del nuevo script (sin .py): ") + ".py"
    ruta_script = os.path.join(ruta_carpeta, nombre_nuevo)
    try:
        with open(ruta_script, 'w') as archivo:
            archivo.write("# Nuevo script en Python\n")
        print(f"Script {nombre_nuevo} creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el script: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)
    unidades = {'1': 'Unidad 1', '2': 'Unidad 2'}
    while True:
        print("\nMenu Principal - Dashboard")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")
        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")
        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    while True:
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]
        print("\nScripts - Selecciona una opción")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú")
        print("9 - Crear un nuevo script")
        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            break
        elif eleccion == '9':
            crear_script_nuevo(ruta_sub_carpeta)
        else:
            try:
                eleccion = int(eleccion) - 1
                if 0 <= eleccion < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        print("1 - Ejecutar\n2 - Abrir en editor\n3 - Eliminar\n0 - Volver")
                        accion = input("Elige una acción: ")
                        if accion == '1':
                            ejecutar_codigo(ruta_script)
                        elif accion == '2':
                            abrir_en_editor(ruta_script)
                        elif accion == '3':
                            eliminar_script(ruta_script)
                        elif accion == '0':
                            continue
                        else:
                            print("Opción no válida.")
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

if __name__ == "__main__":
    mostrar_menu()


