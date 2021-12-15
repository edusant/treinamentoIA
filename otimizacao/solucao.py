import otimizacao.representa as repre
dados = repre.representacao()

agenda = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3]


def imprimir_voos(agenda):
  id_voo = -1
  total_preco = 0
  for i in range(len(agenda) // 2):
    nome = dados.pessoas[i][0]
    origem = dados.pessoas[i][1]
    id_voo += 1
    ida = dados.voos[(origem, dados.destino)][agenda[id_voo]]
    total_preco += ida[2]
    id_voo += 1
    volta = dados.voos[(dados.destino, origem)][agenda[id_voo]]
    total_preco += volta[2]
    print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                volta[0], volta[1], volta[2]))
  print('Preço total: ', total_preco)

#imprimir_voos(agenda)