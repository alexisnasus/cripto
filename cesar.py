def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_original = ord(caracter)
            ascii_cifrado = ascii_original + corrimiento
            if caracter.islower():
                if ascii_cifrado > ord('z'):
                    ascii_cifrado -= 26
                elif ascii_cifrado < ord('a'):
                    ascii_cifrado += 26
            elif caracter.isupper():
                if ascii_cifrado > ord('Z'):
                    ascii_cifrado -= 26
                elif ascii_cifrado < ord('A'):
                    ascii_cifrado += 26
            caracter_cifrado = chr(ascii_cifrado)
            texto_cifrado += caracter_cifrado
        else:
            #si no es una letra, mantener el mismo caracter
            texto_cifrado += caracter
    return texto_cifrado

def obtener_entrada():
    import sys
    if len(sys.argv) != 3:
        print("Uso: python3 cesar.py <texto> <corrimiento>")
        sys.exit(1)
    texto = sys.argv[1]
    corrimiento = int(sys.argv[2])
    return texto, corrimiento

if __name__ == "__main__":
    texto, corrimiento = obtener_entrada()
    texto_cifrado = cifrar_cesar(texto, corrimiento)
    print(texto_cifrado)


