import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import otimizacao.representa as repre
import  otimizacao.funcaodecusto as funcaocusto
import  otimizacao.solucao as solucao


fitness = mlrose.CustomFitness(funcaocusto.fitness_function)

problema = mlrose.DiscreteOpt(length=12, fitness_fn=fitness,
                              maximize = False, max_val = 10)

melhor_solucao, melhor_custo = mlrose.hill_climb(problema, random_state = 1)

solucao.imprimir_voos(melhor_solucao)
