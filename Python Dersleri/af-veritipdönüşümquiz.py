'''
Daire Alanı : pi*r*r
Daire Çevresi: 2*pi*r

Yaricapi verilen 
bir dairenin alan ve çevresini hesaplayınız
'''

r = input("Yaricapi giriniz : ")
pi = 3.14

dairealan = int(r) * int(r)*pi
print("Daire alani ", dairealan)
dairecevresi = 2 * pi * int(r)
print("Daire cevresi", dairecevresi)
