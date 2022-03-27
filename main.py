import subprocess
import random
import algorithms


# constants
POP_NUM = 10
BITS_NUM = 5
COEFF_NUM = 33
P_L = -3.0
P_H = 3.0
TOURNAMENT_SIZE = 4
PROBABILITY = 0.2
MAX_ITER = 150


# kompajliranje C programa
def compile_c_program():
    compile_args = ['gcc', '-Wall', 'g.c', '-o', 'g', '-lm']
    subprocess.call(compile_args)


def nn():
    coefficients = [str(round(random.uniform(P_L, P_H), 3)) for _ in range(0, COEFF_NUM)]
    chromosome = algorithms.code(coefficients, P_L, P_H, BITS_NUM)
    chromosome_cost = algorithms.calc_cost(algorithms.decode(chromosome, P_L, P_H, BITS_NUM))

    best_ever_sol = None
    best_ever_f = None

    for i in range(0, 3):
        best = None
        best_f = None
        k = 0

        population = algorithms.create_population(POP_NUM, BITS_NUM*COEFF_NUM, P_L, P_H, BITS_NUM)
        while best_f != 0 and k < MAX_ITER:
            n_population = population[:]
            while len(n_population) < 2*POP_NUM:
                ch1 = algorithms.tournament(population, TOURNAMENT_SIZE, chromosome_cost)
                ch2 = algorithms.tournament(population, TOURNAMENT_SIZE, chromosome_cost)
                ch3, ch4 = algorithms.crossover(ch1, ch2)

                ch3 = algorithms.mutation(ch3, PROBABILITY)
                ch4 = algorithms.mutation(ch4, PROBABILITY)

                n_population.append((algorithms.calc_cost(algorithms.decode(ch3, P_L, P_H, BITS_NUM)), ch3))
                n_population.append((algorithms.calc_cost(algorithms.decode(ch4, P_L, P_H, BITS_NUM)), ch4))

            population = sorted(n_population, key=lambda x: abs(x[0] - chromosome_cost))[:POP_NUM]
            cost = population[0][0]
            if best_f is None or best_f > abs(cost - chromosome_cost):
                best = population[0][1]
                best_f = abs(cost - chromosome_cost)
            k += 1

        if best_ever_f is None or best_ever_f > best_f:
            best_ever_f = best_f
            best_ever_sol = best

    print('COEFF:')
    print(coefficients)
    print('BEST:')
    print(algorithms.decode(best_ever_sol, P_L, P_H, BITS_NUM))
    print('COST1: ' + str(chromosome_cost))
    print('COST2: ' + str(algorithms.calc_cost(algorithms.decode(best_ever_sol, P_L, P_H, BITS_NUM))))
    print(best_ever_f)


if __name__ == '__main__':
    compile_c_program()
    nn()
