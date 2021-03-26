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
  

