import estruturaDeDados.VetorOrdenado.VetorOrdenado as vtn


vetor = vtn.VetorOrdenado(10)

vetor.insere(6)
vetor.insere(5)
vetor.insere(3)
vetor.insere(2)
vetor.insere(0)
vetor.insere(12)
vetor.insere(60)
vetor.insere(78)
vetor.insere(79)
vetor.insere(81)
vetor.insere(15)
vetor.imprime()
print('================')
print(vetor.pesquisa_linear(6))
vetor.excluir(81)
vetor.insere(15)


print('=============')
vetor.imprime()