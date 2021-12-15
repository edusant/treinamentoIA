import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import  otimizacao.funcaodecusto as funcaocusto
import  otimizacao.solucao as solucao


fitness = mlrose.CustomFitness(funcaocusto.fitness_function)

problema = mlrose.DiscreteOpt(length=12, fitness_fn=fitness,
                              maximize = False, max_val = 10)

melhor_solucao, melhor_custo = mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2,
                                                  random_state=1)

solucao.imprimir_voos(melhor_solucao)
