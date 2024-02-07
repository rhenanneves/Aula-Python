dolares = float(input("Digite o valor em dólares: "))
euro = float(input("Digite a taxa de conversão para euros: "))
libra = float(input("Digite a taxa de conversão para libras: "))

valoreuros = dolares * euro
valorlibras = dolares * libra

print(f"O valor em euros é: {valoreuros}")
print(f"O valor em libras é: {valorlibras}")

#Variáveis e Operações com Números:
#Crie três variáveis, a, b e c, representando os coeficientes de uma equação quadrática (ax^2 + bx + c). Calcule as raízes da equação usando a fórmula de Bhaskara.

a = 4
b = -6
c = -8



delta = (b) **2 - 4 * a *(c)
print (delta)
if a == 0:
    print("o valor de a, deve ser diferente de 0")
elif delta <0:
    print("sem raizes reais")
else:
    x1 = (-b+(delta**(1/2))) / 2 * a 
    x2 = (-b-(delta**(1/2))) / 2 * a 

print (f"O valor do x1 é: {x1}")
print (f"O valor do x2 é: {x2}")