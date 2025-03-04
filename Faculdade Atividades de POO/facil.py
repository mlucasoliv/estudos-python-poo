# #Questão 1

def soma(n1, n2):
    return n1 + n2

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

resultado = soma(n1, n2)

print("A soma dos números {} + {} é igual a {}".format(n1, n2, resultado))

# Questão 2

def eh_par(n):
    if n % 2 == 0:
        print('O número {} é par.'.format(n))
    else:
        print('O número {} é ímpar.'.format(n))
    return n

n = (int(input('Digite um número: ')))

eh_par(n)

# Questão 3

def conta_vogais(palavra):
    letras = ["a", "e", "i", "o", "u"]
    contagem = 0
    for letra in palavra:
        if letra in letras:
            contagem += 1
    return contagem

palavra = (input('Digite uma palavra: '))

print(conta_vogais(palavra))