#Crie um programa que converta uma temperatura dada em Celsius para Fahrenheit usando a fórmula: F = C * 9/5 + 32.
c = float(input("Digite a temperatura em Celsius:"))
f = c * 32 + (9/5)
k = c + 273
print("A temperatura em Celsius é:",c,"ºC")
print("A temperatura em Fahrenheit é:",f,"ºF")
print("A temperatura em Kelvin é:",k,"K")