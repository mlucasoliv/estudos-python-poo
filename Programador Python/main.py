nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(type(nome))
print(type(idade))
print(type(peso))

idade = int(input("Informe a sua idade: "))

if idade >= 18:
    print("Permitido!")
else:
    print("Bloqueado!")

salario = float(input("Digite o seu salário: "))
  
if salario <= 3000:
   print("Programador Junior")
elif salario > 3000 and salario <= 6000:
    print("Programador Pleno")
elif salario > 6000 and salario <= 15000:
    print("Programador Pleno")
else:
    print("Gerente de Projetos")
