class Animal:
  tipo = ""             # Qual animal ele é
  nRest = 0             # Quantidade total de restrições daquele animal
  restricaoOdio = []    # Todas as restrições de ódio que ele tem
  restricaoExtra = []   # Se tiver, a restrição extra que ele tem

  def __init__(self, nome, restricoes, extra):
    self.tipo = nome
    self.restricaoOdio = restricoes
    self.restricaoExtra = extra
    self.nRest = len(self.restricaoOdio) + len(self.restricaoExtra)

leao = Animal("Leao", ["Tigre", "Antilope", "Hiena", "Pavao"], ["1"])
tigre = Animal("Tigre", ["Leao", "Suricate", "Javali", "Pavao", "Antilope"], [])
suricate = Animal("Suricate", ["Tigre", "Hiena"], ["Javali"])
javali = Animal("Javali", ["Tigre", "Hiena"], ["Suricate"])
hiena = Animal("Hiena", ["Leao", "Suricate", "Javali", "Pavao", "Antilope"], [])
pavao = Animal("Pavao", ["Leao", "Tigre", "Hiena"], [])
antilope = Animal("Antilope", ["Leao", "Tigre", "Hiena"], ["Leao", "Tigre"])

animais = [leao, tigre, suricate, javali, hiena, pavao, antilope]

# ------------------------------------------------------------------------ #
class Imprime:
  def imprime(self,resposta):
    j1 = []
    j2 = []
    j3 = []
    j4 = []
    for i in resposta:
      if resposta[i] == 1: j1.append(i.tipo)
      elif resposta[i] == 2: j2.append(i.tipo)
      elif resposta[i] == 3: j3.append(i.tipo)
      elif resposta[i] == 4: j4.append(i.tipo)

    blank = ""
    bottom = "|__________"
    bars = f'| {blank:^9}'
    
    while True:
      index = max(len(j1), len(j2), len(j3), len(j4))
      if len(j1) != index: j1.append(blank)
      if len(j2) != index: j2.append(blank)
      if len(j3) != index: j3.append(blank)
      if len(j4) != index: j4.append(blank)
      if len(j1) + len(j2) + len(j3) + len(j4) == index*4: break

    print(" ___________________________________")
    for i in range(len(j1)):
      print(f'| {j1[i]:^10}| {j2[i]:^10}| {j3[i]:^10}|')
    print(bottom,bottom,bars,bottom)
    for i in range(len(j4)):
      print(f' {blank:^23}{bars:^12}|{j4[i]:^10}|')
    print(f' {blank:^23}{bottom:^12}{bottom:^10}|')