import subprocess
import random
import algorithms


# kompajliranje C programa
compile_args = ['gcc', '-Wall', 'g.c', '-o', 'g', '-lm']
subprocess.call(compile_args)

# constants
POP_NUM = 10
BITS_NUM = 5
COEFF_NUM = 33
P_L = -3.0
P_H = 3.0
TOURNAMENT_SIZE = 4
PROBABILITY = 0.2

coefficients = [str(round(random.uniform(P_L, P_H), 3)) for i in range(0, COEFF_NUM)]
chromosome = algorithms.code(coefficients, P_L, P_H, BITS_NUM)
chromosome_cost = algorithms.calc_cost(algorithms.decode(chromosome, P_L, P_H, BITS_NUM))

population = algorithms.create_population(POP_NUM, BITS_NUM*COEFF_NUM, P_L, P_H, BITS_NUM)
# population = sorted(population, key=lambda x: abs(x[0] - chromosome_cost))
