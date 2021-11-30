import otimizacao.representa as repre
dados = repre.representacao()

agenda = [1,7, 3,1, 1,1, 6,3, 2,4, 5,3]


def fitness_function(agenda):
  id_voo = -1
  total_preco = 0
  for i in range(len(agenda) // 2):
    origem = dados.pessoas[i][1]
    id_voo += 1
    ida = dados.voos[(origem, dados.destino)][agenda[id_voo]]
    total_preco += ida[2]
    id_voo += 1
    volta = dados.voos[(dados.destino, origem)][agenda[id_voo]]
    total_preco += volta[2]

  print('Preço total: ', total_preco)

fitness_function(agenda)