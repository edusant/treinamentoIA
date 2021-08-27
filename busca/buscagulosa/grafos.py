import  busca.buscagulosa.vertice as vertices
import  busca.buscagulosa.Adjacente as adj
import  busca.buscagulosa.VetorOrdenado as vet
import busca.buscagulosa.Gulosa as gula

class Grafo:
  portoUniao = vertices.Vertice("Porto União", 203)
  pauloFrontin = vertices.Vertice("Paulo Frontin", 172)
  canoinhas = vertices.Vertice("Canoinhas", 141)
  irati = vertices.Vertice("Irati", 139)
  palmeira = vertices.Vertice("Palmeira", 59)
  campoLargo = vertices.Vertice("Campo Largo", 27)
  curitiba = vertices.Vertice("Curitiba", 0)
  balsaNova = vertices.Vertice("Balsa Nova", 41)
  araucaria = vertices.Vertice("Araucária", 23)
  saoJose = vertices.Vertice("São José dos Pinhais", 13)
  contenda = vertices.Vertice("Contenda", 39)
  mafra = vertices.Vertice("Mafra", 94)
  tijucas = vertices.Vertice("Tijucas do Sul", 56)
  lapa = vertices.Vertice("Lapa", 74)
  saoMateus = vertices.Vertice("São Mateus do Sul", 123)
  tresBarras = vertices.Vertice("Três Barras", 131)

  portoUniao.adiciona_adjacente(adj.Adjacente(pauloFrontin, 46))
  portoUniao.adiciona_adjacente(adj.Adjacente(canoinhas, 78))
  portoUniao.adiciona_adjacente(adj.Adjacente(saoMateus, 87))

  pauloFrontin.adiciona_adjacente(adj.Adjacente(portoUniao, 46))
  pauloFrontin.adiciona_adjacente(adj.Adjacente(irati, 75))

  canoinhas.adiciona_adjacente(adj.Adjacente(portoUniao, 78))
  canoinhas.adiciona_adjacente(adj.Adjacente(tresBarras, 12))
  canoinhas.adiciona_adjacente(adj.Adjacente(mafra, 66))

  irati.adiciona_adjacente(adj.Adjacente(pauloFrontin, 75))
  irati.adiciona_adjacente(adj.Adjacente(palmeira, 75))
  irati.adiciona_adjacente(adj.Adjacente(saoMateus, 57))

  palmeira.adiciona_adjacente(adj.Adjacente(irati, 75))
  palmeira.adiciona_adjacente(adj.Adjacente(saoMateus, 77))
  palmeira.adiciona_adjacente(adj.Adjacente(campoLargo, 55))

  campoLargo.adiciona_adjacente(adj.Adjacente(palmeira, 55))
  campoLargo.adiciona_adjacente(adj.Adjacente(balsaNova, 22))
  campoLargo.adiciona_adjacente(adj.Adjacente(curitiba, 29))

  curitiba.adiciona_adjacente(adj.Adjacente(campoLargo, 29))
  curitiba.adiciona_adjacente(adj.Adjacente(balsaNova, 51))
  curitiba.adiciona_adjacente(adj.Adjacente(araucaria, 37))
  curitiba.adiciona_adjacente(adj.Adjacente(saoJose, 15))

  balsaNova.adiciona_adjacente(adj.Adjacente(curitiba, 51))
  balsaNova.adiciona_adjacente(adj.Adjacente(campoLargo, 22))
  balsaNova.adiciona_adjacente(adj.Adjacente(contenda, 19))

  araucaria.adiciona_adjacente(adj.Adjacente(curitiba, 37))
  araucaria.adiciona_adjacente(adj.Adjacente(contenda, 18))

  saoJose.adiciona_adjacente(adj.Adjacente(curitiba, 15))
  saoJose.adiciona_adjacente(adj.Adjacente(tijucas, 49))

  contenda.adiciona_adjacente(adj.Adjacente(balsaNova, 19))
  contenda.adiciona_adjacente(adj.Adjacente(araucaria, 18))
  contenda.adiciona_adjacente(adj.Adjacente(lapa, 26))

  mafra.adiciona_adjacente(adj.Adjacente(tijucas, 99))
  mafra.adiciona_adjacente(adj.Adjacente(lapa, 57))
  mafra.adiciona_adjacente(adj.Adjacente(canoinhas, 66))

  tijucas.adiciona_adjacente(adj.Adjacente(mafra, 99))
  tijucas.adiciona_adjacente(adj.Adjacente(saoJose, 49))

  lapa.adiciona_adjacente(adj.Adjacente(contenda, 26))
  lapa.adiciona_adjacente(adj.Adjacente(saoMateus, 60))
  lapa.adiciona_adjacente(adj.Adjacente(mafra, 57))

  saoMateus.adiciona_adjacente(adj.Adjacente(palmeira, 77))
  saoMateus.adiciona_adjacente(adj.Adjacente(irati, 57))
  saoMateus.adiciona_adjacente(adj.Adjacente(lapa, 60))
  saoMateus.adiciona_adjacente(adj.Adjacente(tresBarras, 43))
  saoMateus.adiciona_adjacente(adj.Adjacente(portoUniao, 87))

  tresBarras.adiciona_adjacente(adj.Adjacente(saoMateus, 43))
  tresBarras.adiciona_adjacente(adj.Adjacente(canoinhas, 12))


grafo = Grafo()


busca_gulosa = gula.Gulosa(grafo.curitiba)
busca_gulosa.buscar(grafo.portoUniao)