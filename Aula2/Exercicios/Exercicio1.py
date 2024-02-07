a = 4
b = 3

soma = (a + b )
subtracao = (a - b)
divisao = (a/b)
multiplicacao = (a*b)
divisaoInteira = (a//b)
restodivisao = (a%b)
potenciacao = (a**b)

print(soma, subtracao, divisao, multiplicacao, divisaoInteira, restodivisao, potenciacao)

pi = 3.14  # Aproximação de pi
raio = 5  # Exemplo de valor do raio

# Calcula a área do círculo
area = (pi * raio) ** 2
print("A área do círculo é:", area)

#Manipulação de Strings:
nome = "rhenan"
sobrenome = "neves"
nomecompleto = nome +" "+ sobrenome
print(nome + " " + sobrenome)

#Crie uma string que represente uma frase e use métodos de string para:
nome_upper = nomecompleto.upper()
print(nome_upper)

#Listas e Tuplas:

# Listas (mutáveis)
frutas = ["verde", "vermelho", "amarelo"]
numeros = [1, 2, 3, 4, 5]

# Adicionando elementos a uma lista
frutas.append("laranja")
frutas.append("preto")
print(frutas[3])


coordenadas = (40.7128, -74.0060)

latitude, longitude = coordenadas
print("Latitude:", latitude)
print("Longitude:", longitude)

#boolean
tem_sol = True
tem_chuva = False

# Expressões booleanas
dia_agradavel = tem_sol or tem_chuva
dia_desagradavel = tem_sol and tem_chuva

print(dia_agradavel)
print(dia_desagradavel)

#Solicite ao usuário dois números e use operadores lógicos para verificar se ambos são números pares. Imprima o resultado.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

num_par = (num1 % 2 == 0) and (num2 % 2 == 0)

if num_par:
    print("Os numeros são pares")
else: 
    print("Os numeros são ímpares")

#Crie uma lista de números e use uma estrutura de repetição para percorrer a lista. Utilize operadores lógicos para verificar e imprimir quais números são múltiplos de 3 e ímpares.

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for num in numeros:
    if num % 3 == 0 and num % 2 != 0:
        print(f"{num} é múltiplo de 3 e ímpar.")

#Peça ao usuário para digitar a sua idade e verifique se ela está dentro do intervalo de 18 a 65 anos. Imprima uma mensagem correspondente.

idade = int(input("Digite sua idade: "))
if idade >= 18 and idade <= 65:
    print("Sua idade é entre 18 e 65 anos")
else:
    print("Sua idade não é entre 18 e 65 anos")
