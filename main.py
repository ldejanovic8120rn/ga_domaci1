import subprocess
import algorithms
import matplotlib.pyplot as plt


# constants
POP_NUM = 10
BITS_NUM = 5
COEFF_NUM = 33
P_L = -10.0
P_H = 10.0
TOURNAMENT_SIZE = 4
PROBABILITY = 0.2
MAX_ITER = 150


# kompajliranje C programa
def compile_c_program():
    compile_args = ['gcc', '-Wall', 'g.c', '-o', 'g', '-lm']
    subprocess.call(compile_args)


def draw(datas, title):
    cnt = 1
    for data in datas:
        xs = [d[0] for d in data]
        ys = [d[1] for d in data]
        plt.plot(xs, ys, label=str(cnt))
        cnt += 1

    plt.xlabel('generations')
    plt.ylabel('cost')
    plt.legend()
    plt.title(title)
    plt.show()


def nn():
    average_cost_all = []
    best_cost_all = []

    best_ever_sol = None
    best_ever_f = None

    for i in range(0, 3):
        average_cost = []
        best_cost = []
        best = None
        best_f = None
        k = 0

        population = algorithms.create_population(POP_NUM, COEFF_NUM*BITS_NUM, P_L, P_H, BITS_NUM)
        while best_f != 0 and k < MAX_ITER:
            n_population = population[:]
            while len(n_population) < POP_NUM + 10:
                ch1 = algorithms.tournament(population, TOURNAMENT_SIZE)
                ch2 = algorithms.tournament(population, TOURNAMENT_SIZE)
                ch3, ch4 = algorithms.crossover(ch1, ch2)

                ch3 = algorithms.mutation(ch3, PROBABILITY)
                ch4 = algorithms.mutation(ch4, PROBABILITY)

                n_population.append((algorithms.calc_cost(algorithms.decode(ch3, P_L, P_H, BITS_NUM)), ch3))
                n_population.append((algorithms.calc_cost(algorithms.decode(ch4, P_L, P_H, BITS_NUM)), ch4))

            population = sorted(n_population, key=lambda x: x[0])[:POP_NUM]
            cost = population[0][0]

            best_cost.append((k, cost))
            average_cost.append((k, sum([p[0] for p in population])/POP_NUM))

            if best_f is None or best_f > cost:
                best = population[0][1]
                best_f = cost
            k += 1

        if best_ever_f is None or best_ever_f > best_f:
            best_ever_f = best_f
            best_ever_sol = best

        best_cost_all.append(best_cost)
        average_cost_all.append(average_cost)

    print(best_ever_f)

    draw(best_cost_all, 'BEST')
    draw(average_cost_all, 'AVERAGE')


if __name__ == '__main__':
    # compile_c_program()
    nn()
