name = 'Selim'
surname = "Çınar"
age = 22
print("My name is {} ".format(name))
print("My name is {0} {1}".format(name, surname))
print("My name is {1} {0}".format(name, surname))
print("My name is {s} {n} and I'm {a} years old".format(
    n=name, s=surname, a=age))

result = 200 / 500
print("The result is {r:7.4}".format(r=result))

print(f"My name is {name} {surname} and I'm {age}years old.")
