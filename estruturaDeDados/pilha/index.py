import estruturaDeDados.pilha.classepilha as Pilhas
pilha = Pilhas.classepilha(5)

pilha.empilhar(1)
print(pilha.ver_topo())

pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)

pilha.empilhar(5)


print(pilha.ver_topo())

pilha.desempilhar()

print(pilha.ver_topo())