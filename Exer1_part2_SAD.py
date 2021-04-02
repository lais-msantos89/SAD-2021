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


'''Exercício 6: Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema, deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

1) Maior e Menor acerto

2) Total de Alunos que utilizaram o sistema

3) A Média das Notas da Turma.'''


#Gabarito:
gab = ('A','B','C','A','D','C','B','B','A','D')
type(gab)
#coletando as respostas:
notas = []
NA = 0
while True:
  print('Há mais alunos para registrar nota?')
  sn = input()
  SN = sn.upper()
  if SN == 'SIM':
    NA = NA+1
    print('Informe o item correto em cada questão:')
    resposta = []
    for i in range(1,11):
      print('Resposta',i)
      r_i = input()
      R_i = r_i.upper()
      resposta.append(R_i)
    print(resposta)
    sol= tuple(resposta)
    print(sol)
    S = 0
    for i in range(0,10):
      if sol[i] == gab[i]:
        S = S+1
      else:
        S= S
    print('O número de acertos é',S)
    notas.append(S)
  else:
    NA= NA
    break
print(notas)
print('Total de alunos:', NA)
print('A menor nota da turma foi', min(notas))
print('A maior nota da turma foi', max(notas))
me = sum(notas)/NA
print('A média da turma é', me) 


