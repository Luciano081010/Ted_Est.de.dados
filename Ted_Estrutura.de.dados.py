#questão 01:

print("Questão 1:")
nota1 = float(input('\nDigite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota:'))
nota3 = float(input('Digite sua terceira nota:'))

media = (nota1 + nota2 + nota3) / 3
print('Sua média foi: ',  media)

if media == 10:
    print('Aprovado com distinção. Parabéns!!')
elif media >= 7 and media < 10:
    print('Parabéns, você foi aprovado!!')
else:
    print('Você foi reprovado.')

print("\nQuestão 2:")

#Questao 02:

nota = float(input("\nInforme uma nota de 0 a 10:"))

while(nota < 0 or nota > 10):
    print("Nota inválida. Digite novamente!")
    nota = float(input("Informe uma nota de 0 a 10:"))

print("\nQuestão 3:")

#Questao 03:

temperatura = float(input("\nDigite a temperatua em graus Fahrenheit:"))
print(temperatura)

C = 5 * ((temperatura-32) / 9)
print("A temperatura convertida em graus Celsius é: ", C)

print("\nQuestão 4:")

#questao 04:

ano = int(input("\nDigite o ano que deseja:"))

if (ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
    print("O ano ", ano ,", é um ano Bissexto")
else:
    print("O ano ", ano ,", não é um ano Bissexto")

print("\nQuestão 5:")
#Questao 05:
num = int(input("\nDigite um número inteiro:"))
lista = []
print(num)

for i in range(num + 1):
     if i % 2 == 1 and i != 2:
         lista.append(i)


print(lista)

print("\nQuestão 6:")

#questao 06:
idades = []
alturas = []

for i in range(1 , 6):
    print('%dº Pessoa' % i)
    idade = int(input("Informe a sua idade: "))
    altura = float(input("Informa a sua altura: "))
    idades.append(idade)
    alturas.append(altura)


print("Ordem inversa das idades:")
print(idades[:: -1])

print("Ordem inversa das alturas:")
print(alturas[:: -1])

print("\nQuestão 7:")

#questao 07:
def reverso(num):
    return str(num[:: -1])

num = str(input("Digite um número: ")).strip()
print(reverso(num))

