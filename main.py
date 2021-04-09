import satisfacaoRestricoes as sr
import animais as a

# {"variavel": valor}

class RestricaoOdio(sr.Restricao):
  def __init__(self, x1, x2):
    super().__init__([x1, x2])
    self.variaveis = [x1, x2]

  def esta_satisfeita(self, atribuicao):
    # Não analisa se todos os estados estiverem atribuidos
    if not all(variavel in atribuicao for variavel in self.variaveis):
      return True
    # Os dois não podem ser vizinhos de jaula
    valores = [atribuicao[variavel] for variavel in self.variaveis]
    return len(set(valores)) == 2


class RestricaoExtra(sr.Restricao):
  def __init__(self, x1, x2):
    super().__init__([x1, x2])
    self.variaveis = [x1, x2]

  def esta_satisfeita(self, atribuicao):
    # Não analisa se todos os estados estiverem atribuidos
    if not all(variavel in atribuicao for variavel in self.variaveis):
      return True

    # leao precisa estar na jaula 1
    if self.variaveis[0].tipo == self.variaveis[1].tipo:
      return atribuicao[self.variaveis[0]] == 1

    # Suricate e Javali querem na mesma jaula
    if self.variaveis[0].tipo == "Suricate" and self.variaveis[1].tipo == "Javali":
      return atribuicao[self.variaveis[0]] == atribuicao[self.variaveis[1]]

    # Antilope não pode ser vizinho nem adjacente ao leão e tigre
    if self.variaveis[0].tipo == "Antilope" and (self.variaveis[1].tipo == "Leao" or self.variaveis[1].tipo == "Tigre"):
      return abs(atribuicao[self.variaveis[0]] -  atribuicao[self.variaveis[1]]) > 1

# ----------------------------------------------------------------------- #
variaveis = []

# Passa por todos os animais, adicionando cada um as variaveis do problema
for ani in a.animais:
  variaveis.append(ani)

# Atribui os domínios a cada variável
dominios = {}
for variavel in variaveis:
      dominios[variavel] = [1, 2, 3, 4]
problema = sr.SatisfacaoRestricoes(variaveis, dominios)

# Passa por cada animal, adicionando cada Restricao de Ódio que ele possui
for ani in a.animais:
  for i in ani.restricaoOdio:
    restrito = a.Animal
    for anim in a.animais:
      if anim.tipo == i:
        restrito = anim
        break
    problema.adicionar_restricao(RestricaoOdio(ani, restrito))

# Adiciona as restrições extras
problema.adicionar_restricao(RestricaoExtra(a.leao, a.leao))
problema.adicionar_restricao(RestricaoExtra(a.suricate, a.javali))
problema.adicionar_restricao(RestricaoExtra(a.antilope, a.leao))
problema.adicionar_restricao(RestricaoExtra(a.antilope, a.tigre))

resposta = problema.busca_backtrackingMCV()
if resposta is None:
  print("Nenhuma resposta encontrada")
else:
  print("Leão: Jaula", resposta[a.leao])
  print("Antílope: Jaula", resposta[a.antilope])
  print("Hiena: Jaula", resposta[a.hiena])
  print("Tigre: Jaula", resposta[a.tigre])
  print("Pavão: Jaula", resposta[a.pavao])
  print("Suricate: Jaula", resposta[a.suricate])
  print("Javali: Jaula", resposta[a.javali])

  print("\n\nEP 2: O Zoológico")
  # Imprime jaulas bonitinho
  impressora = a.Imprime()
  impressora.imprime(resposta)
