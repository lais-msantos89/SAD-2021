# Observação: Ainda sobre o exercicio 2

li_respostas = []
resp1 = input('Telefonou para a vítima?')
Resp1 = resp1.upper()
li_respostas.append(Resp1)
resp2 = input('Mora perto da vítima?')
Resp2 = resp2.upper()
li_respostas.append(Resp2)
resp3 = input('Devia para a vítima?')
Resp3 = resp3.upper()
li_respostas.append(Resp3)
resp4 = input('Já trabalhou com a vítima?')
Resp4 = resp4.upper()
li_respostas.append(Resp4)
resp5 = input('Mora perto da vítima?')
Resp5 = resp5.upper()
li_respostas.append(Resp5)

total = li_respostas.count('SIM')
print(total)
if total == 2:
  print('Suspeita')
elif total == 3 or total== 4: 
  print('Cúmplice')
elif total == 5:
  print('Culpado')
else: 
  print('Inocente')
  

'''Exercício 5: Faça um programa que leia uma quantidade indeterminada de 
números positivos e conte quantos deles estão nos seguintes intervalos 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.'''

print('Forneça uma lista de números e ao final digite a palavra "sair":')
try:
    conj = []     
    while True: 
        conj.append(float(input()))           
# if the input is not-number, just print the list 
except: 
    print(conj) 
conj1 = []
for x in conj:
  if x >=0 and x <= 25:
    conj1.append(x)
tconj1 = set(conj1)
print('O número de elementos no conjunto 1 é:',len(tconj1))
conj2 = []
for x in conj:
  if x >=26 and x <= 50:
    conj2.append(x)
tconj2 = set(conj2)
print('O número de elementos no conjunto 2 é:',len(tconj2))
