from cryptography.fernet import Fernet
import os

if not os.path.exists("key.key"):
    clave = Fernet.generate_key()
    with open("key.key", "wb") as k:
        k.write(clave)
else:
    with open("key.key", "rb") as k:
        clave = k.read()


fern = Fernet(clave)

print("[*] Iniciando desencriptado...\n")
print("--- COMIENZO DEL MENSAJE ---\n")

try:
    
    with open("log_seguro.txt", "rb") as file:
        for linea in file:
            linea = linea.strip()     
            if linea:
                try:
                    mensaje_descifrado = fern.decrypt(linea)
                    print(mensaje_descifrado.decode('utf-8'), end="")
                except Exception as e:
                    print(f"\n[!] Error en una línea: {e}")

    print("\n\n--- FIN DEL MENSAJE ---")

except FileNotFoundError:
    print("[-] El archivo 'log_seguro.txt' aún no existe.")


