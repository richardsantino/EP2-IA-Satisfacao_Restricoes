class Restricao():
  def __init__(self, variaveis):
    self.variaveis = variaveis

  def esta_satisfeita(self, atribuicao):
    return True

class SatisfacaoRestricoes():
  def __init__(self, variaveis, dominios):
    self.variaveis = variaveis # Variáveis para serem restringidas
    self.dominios = dominios # Domínio de cada variável
    self.restricoes = {}
    for variavel in self.variaveis:
      self.restricoes[variavel] = []
      if variavel not in self.dominios:
        raise LookupError("Cada variável precisa de um domínio")

  def adicionar_restricao(self, restricao):
    for variavel in restricao.variaveis:
      if variavel not in self.variaveis:
        raise LookupError("Variável não definida previamente")
      else:
        self.restricoes[variavel].append(restricao)

  def esta_consistente(self, variavel, atribuicao):
    for restricoes in self.restricoes[variavel]:
      if not restricoes.esta_satisfeita(atribuicao):
        return False
    return True
  
  def busca_backtrackingMCV(self, atribuicao = {}):
    # retorna sucesso quando todas as variáveis forem atribuídas
    if len(atribuicao) == len(self.variaveis):
      return atribuicao

    # pega todas as variáveis que ainda não foram atribuídas
    variaveis_nao_atribuida  = [v for v in self.variaveis if v not in atribuicao]
    # Filtra as variaveis pra primeira sempre ser a com mais restrições
    variaveis_sorted = self.filtrarRestricoes(variaveis_nao_atribuida)
    primeira_variavel = variaveis_sorted[0]
    for valor in self.dominios[primeira_variavel]:
      atribuicao_local = atribuicao.copy()
      atribuicao_local[primeira_variavel] = valor
      # estamos consistentes, seguir recursão
      if self.esta_consistente(primeira_variavel, atribuicao_local):
        # Faz o forward checking para os outros domínios
        self.forwardChecking(variaveis_sorted, primeira_variavel, valor)
        resultado  = self.busca_backtrackingMCV(atribuicao_local)
        # para o backtracking se não encontra todos os resultados
        if resultado is not None:
          return resultado
    return None

  def filtrarRestricoes(self, varNaoAtribuidas):
    # Bubblesort, mas invertido (decrescente)
    sorting = varNaoAtribuidas.copy()
    i = True
    while i:
      i = False
      for j in range(len(sorting) - 1):
        if sorting[j].nRest < sorting[j+1].nRest:
          sorting[j], sorting[j+1] = sorting[j+1], sorting[j]
          i = True
    return sorting

  def forwardChecking(self, variaveis, atribuida, valor):
    # Verifica se a variável que acabou de ser atribuida um valor está nas restrições de ódio dos outros animais, e caso esteja, o valor é excluido do domínio
    for variavel in variaveis:
      if atribuida.tipo in variavel.restricaoOdio and valor in self.dominios[variavel]:
        self.dominios[variavel].remove(valor)