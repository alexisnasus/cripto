import sys
import os
from scapy.all import *
import time
import struct

def get_timestamp():
    return int(time.time())

def enviar_paquetes_icmp(texto):
    ip_destino = "127.0.0.1"
    id_paquete = os.getpid() & 0xFFFF  # Identificador único basado en el PID del proceso
    seq = 1
    for caracter in texto:
	    timestamp = get_timestamp()
	    timestamp_bytes = struct.pack('<Q', timestamp)  # Convertir el timestamp a bytes en Little Endian
	    timestamp_hex = ''.join([f'\\x{byte:02x}' for byte in timestamp_bytes])  # Formatear los bytes como '\xHH'
	    payload_3_bytes = b'\x62\x09'
	    payload_5_bytes = b'\x00\x00\x00\x00\x00'
	    payload_variado = bytes(range(0x10, 0x38))
	    paquete_icmp = IP(dst=ip_destino) / ICMP(type=8, code=0, id=id_paquete, seq=seq) / bytes(timestamp_bytes) / bytes([ord(caracter)]) / payload_3_bytes / payload_5_bytes / payload_variado
	    print(".")
	    send(paquete_icmp, verbose=False)
	    seq += 1
	    print("Sent 1 packets.")
	    time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: sudo python3 pingv4.py <texto>")
        sys.exit(1)
    texto = sys.argv[1]
    enviar_paquetes_icmp(texto)
