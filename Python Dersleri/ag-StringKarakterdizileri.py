name = 'Selim'
surname = 'Çınar'
age = 36

greeting = "My name is " + name + '  '+surname + \
    'and\n I am ' + str(age) + 'years old.'

length = len(greeting)  # karakter uzunlunu ölçer


print(greeting)
print(greeting[0])
print(greeting[3])
print(len(greeting))
print(greeting[length-1])  # ensondaki karakteri getirir
print(greeting[-1])
print(greeting[2:5])
print(greeting[3:7])
print(greeting[3:])
print(greeting[:15])
print(greeting[2:40:2])
