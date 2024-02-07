# Números de ponto flutuante
preco_unitario = 29.99
pi = 3.14159

# Strings (Cadeias de Caracteres):

# Strings simples
nome = "Alice"
mensagem = 'Olá, seja bem-vindo!'

# Concatenação de strings
nome_completo = nome + " Wonderland"

# Formatação de strings
idade = 23
mensagem_formatada = f"Olá, {nome}! Você tem {idade} anos."

#Listas e Tuplas:

# Listas (mutáveis)
frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4, 5]

# Adicionando elementos a uma lista
frutas.append("laranja")
frutas.append("morango")
print(frutas[2])

# Tuplas (imutáveis)
coordenadas = (4, 5)
cores_rgb = (255, 0, 0)


# Dicionários:

# Dicionário chave-valor
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "engenheiro"
}

# Acessando valores
print(pessoa["nome"])
print(pessoa.get("idade"))


# Adicionando novo par chave-valor
pessoa["cidade"] = "São Paulo"

# Variáveis booleanas
tem_cafe = True
tem_cha = False

# Expressões booleanas
tem_bebida_quente = tem_cafe or tem_cha
tem_as_dois = tem_cafe and tem_cha

print(tem_as_dois)
print(tem_bebida_quente)

