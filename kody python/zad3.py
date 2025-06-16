from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

plik = input("Podaj plik do podpisania: ")
key = RSA.generate(2048)

open("private.pem", "wb").write(key.export_key())
open("public.pem", "wb").write(key.publickey().export_key())
dane = open(plik, "rb").read()

podpis = pkcs1_15.new(RSA.import_key(open("private.pem", "rb").read())).sign(SHA256.new(dane))
open(plik + ".sig", "wb").write(podpis)
print("Utworzono podpis")



