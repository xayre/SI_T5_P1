import os
import psutil

 # Nombre del archivo de log generado por el keylogger
log_file = "keylogger_saver.txt"

 # Nombre del script que contiene el keylogger
script_name = "keylogger.py" 

 # Función para encontrar y detener el proceso que ejecuta este script
def detener_keylogger(script_name):
     try:
         # Recorre todos los procesos en ejecución
         for proc in psutil.process_iter(attrs=["pid", "name", "cmdline"]):
             if proc.info["cmdline"] and script_name in " ".join(proc.info["cmdline"]):
                 pid = proc.info["pid"]
                 print(f"Deteniendo proceso con PID {pid} ({script_name})...")
                 
                 # Termina el proceso
                 psutil.Process(pid).terminate()
                 print(f"Proceso {pid} detenido exitosamente.")
                 return
         print(f"No se encontró ningún proceso ejecutando {script_name}.")
     except Exception as e:
         print(f"Error al detener el proceso: {e}")

 # Función para eliminar el archivo de log
def eliminar_archivo_log(log_file):
     try:
         if os.path.exists(log_file):
             os.remove(log_file)
             print(f"Archivo de log '{log_file}' eliminado exitosamente.")
         else:
             print(f"Archivo de log '{log_file}' no encontrado.")
     except Exception as e:
         print(f"Error al eliminar el archivo de log: {e}")

detener_keylogger(script_name)
eliminar_archivo_log(log_file)