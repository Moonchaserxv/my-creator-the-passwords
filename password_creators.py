import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

charla = int(input("dame un numero para tu clave: "))

password = ""
for i in range(charla):
    password += random.choice(caracteres)


print(password)