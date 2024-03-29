from scapy.all import *
from langdetect import detect

def obtener_caracter_en_posicion(file_path, posicion):
    caracteres = ""
    packets = rdpcap(file_path)

    for packet in packets:
        if ICMP in packet:
            load = bytes(packet[Raw].load)
            if 0 <= posicion < len(load):
                caracter = chr(load[posicion])
                caracteres += caracter

    return caracteres

def cesar(descifrar, mensaje, corrimiento):
    resultado = ""

    for caracter in mensaje:
        if caracter.isalpha():
            if descifrar:
                resultado += chr((ord(caracter) - corrimiento - ord('a')) % 26 + ord('a'))
            else:
                resultado += chr((ord(caracter) + corrimiento - ord('a')) % 26 + ord('a'))
        else:
            resultado += caracter

    return resultado

def mostrar_combinaciones(file_path, posicion):
    mensaje_cifrado = obtener_caracter_en_posicion(file_path, posicion)
    print("Mensaje cifrado:", mensaje_cifrado)
    print("Todas las combinaciones posibles de descifrado:")
    mejor_opcion = None
    for corrimiento in range(26):
        texto_descifrado = cesar(True, mensaje_cifrado, corrimiento)
        try:
            if detect(texto_descifrado) == "es":
                if mejor_opcion is None:
                    mejor_opcion = (corrimiento, texto_descifrado)
                print(f"\033[32m{corrimiento} {texto_descifrado}\033[0m")
            else:
                print(f"{corrimiento} {texto_descifrado}")
        except:
            print(f"{corrimiento} {texto_descifrado}")
    if mejor_opcion:
        print("\nMensaje descifrado más probable:")
        print(f"\033[32m{mejor_opcion[0]} {mejor_opcion[1]}\033[0m")


if __name__ == "__main__":
    posicion = 8
    if len(sys.argv) != 2:
        print("Uso: sudo python3 readyv2.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    mostrar_combinaciones(file_path, posicion)

