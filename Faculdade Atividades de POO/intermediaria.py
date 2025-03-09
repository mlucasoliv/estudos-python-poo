#Questão 4

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

n = int(input("Digite um número: "))

print(fatorial(n))

# Questão 5

def media_lista(numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    resultado = soma/quantidade
    return resultado

numeros = [10, 20, 30, 40]
resultado = media_lista(numeros)

print(resultado)

#Questão 6

def inverte_string(texto):
    invertido = texto[::-1]
    return invertido

texto = input("Digite uma palavra: ")
invertido = inverte_string(texto)
print(invertido)