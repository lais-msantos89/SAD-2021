'''Lendo aquivos txt'''

emag = "/content/emagrecimento.txt"
file = open(emag,'r',encoding='utf-8')
emag_text = file.readlines()
file.close()

print(emag_text)

Dados_ind = []
for i in range(0,20):
  print(emag_text[i].split(','))
  Dados_ind.append(emag_text[i].split(','))
print(Dados_ind)

'''Exercício 1: Escreva uma função, denominada Individuos que receba o nome de um arquivo texto como resultado da pesquisa, crie e retorne uma tupla ou lista de indivíduos, em que cada indivíduo seja representado como uma tupla ou lista como:

*(número_de_identificação sexo, idade, medicamento,medicamento,(peso 1 peso 2 peso 3), efeito colateral)'''


def Individuos(arg1):
  resp = arg1
  arquivo = open(resp,'r',encoding='utf-8')
  textinp = arquivo.readlines()
  arquivo.close()
  Dados_total = []
  for i in range(0,len(textinp)):
      Dados_total.append(tuple(textinp[i].split(',')))
  return Dados_total


'''**Exercício 2**
Escreva uma função, denominada UmEfeitoColateral que receba a tupla ou lista de indivíduos resultante do item 1 e um efeito colateral, e retorne uma nova tupla ou lista apenas com as tuplas ou listas correspondentes aos indivíduos
que tiveram esse efeito colateral 
Obs não devem ser criadas novas tuplas ou listas para os indivíduos'''

def EfeitoColateral(arg2):
  Total_ec = []
  for i in range(0,len(Individuos('/content/emagrecimento.txt'))):
     if arg2 in set(Individuos('/content/emagrecimento.txt')[i]):
       Total_ec.append(Individuos('/content/emagrecimento.txt')[i])
     else: 
       Total_ec = Total_ec
  return Total_ec
  
  
EfeitoColateral('náusea')
  
  
EfeitoColateral('visão turva')
  
  
''' Exercício 3 Escreva uma função, denominada minMaxPerda que receba a tupla ou lista de indivíduos resultante do item 1 e, considerando perda = peso 3 - peso 1 retorne uma tupla ou lista com

(MenorPerda, indivíduoDeMenorPerda), (MaiorPerda, indivíduoDeMaiorPerda)

OBS: indivíduoDeMenorPerda e indivíduoDeMaiorPerda são a tupla ou lista correspondente ao indivíduoDeMenorPerda e a tupla ou lista correspondente ao indivíduoDeMaiorPerda'''

def minMaxPerda(arg3):
  var_peso = []
  for i in range(0,len(arg3)):
     individ_i = arg3[i]
     perda_i = float(individ_i[6]) - float(individ_i[4])
     var_peso.append(perda_i)
  ind_min = var_peso.index(max(var_peso))
  ind_max = var_peso.index(min(var_peso))
  return arg3[ind_min], arg3[ind_max]
  
  
minMaxPerda(Individuos('/content/emagrecimento.txt'))

'''**Exercício 4** 
Escreva uma função, denominada avaliacaoIndividuo que receba uma tupla ou lista com os dados de um único indivíduo como
descrito no item 1 e retorne um nova tupla ou lista com (número_de_identificação sexo, idade, medicamento, resultado, efeito_colateral)


O resultado é obtido através da análise dos 3 pesos da seguinte forma se peso 3 >= peso 1 então resultado é igual a “SEM PERDA” do contrário  se peso 1 > peso 2 > peso 3 então resultado igual a “PERDA CONTÍNUA”, senão resultado igual a “PERDA OSCILANTE”'''

def avaliacaoIndividuo(arg):
   ficha_ind = arg[0:4] + arg[7:8]
   if float(arg[6]) >= float(arg[4]):
    ficha_ind.insert(4,'SEM PERDA')
   elif float(arg[4]) > float(arg[5]) > float(arg[6]):
    ficha_ind.insert(4,'PERDA CONTÍNUA')
   else:
    ficha_ind.insert(4,'PERDA OSCILANTE')
   return ficha_ind
   
avaliacaoIndividuo(list(Individuos('/content/emagrecimento.txt')[1]))

'''Exercício 5 5. Escreva uma função, denominada criaAvaliacoes , que receba a tupla ou lista de indivíduos retornada no item 1 e retorne uma tupla de tuplas ou lista de listas correspondentes às avaliações dos resultados dos indivíduos. Para isso, deve ser utilizada a função do item 4 .'''

def criaAvaliacoes(arg):
   fichaaval = []
   for i in range(0,len(arg)):
      fichaaval.append(avaliacaoIndividuo(list(arg[i])))
   return fichaaval
   
criaAvaliacoes(Individuos('/content/emagrecimento.txt'))


'''Exercício 6 Escreva uma função, denominada criaDicDeMedicamento , que receba a tupla ou lista de indivíduos retornada no item 1 e retorne um dicionário em que cada elemento seja:

MEDICAMENTO: quantidade_de_individuos_desse_medicamento'''

def criaDicDeMedicamento(arg):
   totalX = 0
   for i in range(0,len(arg)):
     if arg[i][3] == 'X' or arg[i][3] == 'x':
       totalX = totalX +1
     else:
       totalX = totalX
   print(totalX)
   dicionario_medic = {'Medicamento X':totalX, 'Medicamento A': len(arg) - totalX}
   return dicionario_medic
   
criaDicDeMedicamento(Individuos('/content/emagrecimento.txt'))


'''Exercício 7 Escreva uma função, denominada criaDicDeEfeitosColaterais , que receba a tupla ou lista de indivíduos retornada no item 1 e retorne um dicionário em que cada elemento seja:

Efeito_Colateral : lista com os números_de_identificação dos indivíduos que sentiram tal efeito colateral'''

def criaDicDeEfeitosColaterais(arg):
   total_nausea = 0
   total_dorcabeca = 0
   total_diarreia = 0
   total_visaoturva = 0
   total_nenhum = 0
   naus = []
   vistur = []
   diarr = []
   dorcab = []
   nenhum = []
   for i in range(0,len(arg)):
     if arg[i][7] == 'náusea':
       total_nausea = total_nausea +1
       naus.append(arg[i][0])
     elif arg[i][7] == 'dor de cabeça':
       total_dorcabeca = total_dorcabeca +1
       dorcab.append(arg[i][0])
     elif arg[i][7] == 'diarréia':
       total_diarreia = total_diarreia +1
       diarr.append(arg[i][0])
     elif arg[i][7] == 'visão turva':
       total_visaoturva = total_visaoturva +1
       vistur.append(arg[i][0])
     else: 
       total_nenhum = total_nenhum +1
       nenhum.append(arg[i][0])
   dicionario_sint = {'Náusea':naus, 'Dor de Cabeça': dorcab, 'Diarréia': diarr, 'Visão Turva': vistur, 'Nenhum': nenhum}
   return dicionario_sint
   
   
criaDicDeEfeitosColaterais(Individuos('/content/emagrecimento.txt'))