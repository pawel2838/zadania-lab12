from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

inp = input("Podaj nazwę pliku do zaszyfrowania: ")
output = input("Podaj nazwę pliku wynikowego: ")
haslo = input("Podaj hasło szyfrujące: ")

def szyfrowanie(input, output, haslo):

    klucz = haslo.ljust(16)[:16].encode()
    iv = get_random_bytes(16)
    szyfr = AES.new(klucz, AES.MODE_CBC, iv)

    with open(input, 'rb') as inputf, \
            open(output, 'wb') as outputf:
        outputf.write(iv)
        jawny = inputf.read()
        padding = 16 - (len(jawny) % 16)
        jawny += b' ' * padding
        zaszyfrowany = szyfr.encrypt(jawny)
        outputf.write(zaszyfrowany)

szyfrowanie(inp, output, haslo)