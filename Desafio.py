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