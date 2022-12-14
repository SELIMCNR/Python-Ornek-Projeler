# dışardan değer girişi olur input() string veri getirir.
x = input("1.Sayı : ")
y = input("1.Sayı : ")
z = input("1.Sayı : ")

print(type(x))
print(type(y))
print(type(z))

toplam = int(x)+int(y)+int(z)
print(toplam)

z = 5
c = 2.5
name = "Çınar"
isOnline = True

print(type(z))
print(type(y))
print(type(name))
print(type(isOnline))

# Type Conversion
# int to float
z = float(z)
print(z)
print(type(z))

# float to int
c = int(c)
print(y)
print(type(y))

# Toplam sonucu
result = z + y
print(result)
print(type(result))

# String birleştir
result = str(z) + str(y)
print(result)
print(type(result))

# bool to int
# false = 0 , true = 1
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))
