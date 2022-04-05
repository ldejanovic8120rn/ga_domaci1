import subprocess
import algorithms
import matplotlib.pyplot as plt


# constants
params = {
    'POP_NUM': 10,
    'NPOP_NUM': 10,
    'BITS_NUM': 8,
    'COEFF_NUM': 33,
    'P_L': -10.0,
    'P_H': 10.0,
    'TOURNAMENT_SIZE': 4,
    'PROBABILITY': 0.2,
    'MAX_ITER': 150
}


# kompajliranje C programa
def compile_c_program():
    compile_args = ['gcc', '-Wall', 'g.c', '-o', 'g', '-lm']
    subprocess.call(compile_args)


def read_config_file():
    global params

    while True:
        print('Do you want to forward the config file? [y/n]: ')
        choice = input()
        if choice == 'y':
            print('Please, insert path to the config file: ')
            path = input()
            try:
                f = open(path, 'r')
                lines = f.read().splitlines()
                for line in lines:
                    key, value = line.split('=')
                    if key == 'P_L' or key == 'P_H' or key == 'PROBABILITY':
                        params[key] = float(value)
                    else:
                        params[key] = int(value)

                f.close()
                break
            except FileNotFoundError:
                print('File not found!')

        elif choice == 'n':
            break
        else:
            print('Bad command!')


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
    print('Please, insert the output file: ')
    output_file = input()
    f = open(output_file, 'w')

    average_cost_all = []
    best_cost_all = []

    best_ever_f = None

    for i in range(0, 3):
        f.write('TEST CASE: ' + str(i+1) + '\n\n')
        average_cost = []
        best_cost = []
        best_f = None
        k = 0

        population = algorithms.create_population(params['POP_NUM'], params['COEFF_NUM']*params['BITS_NUM'],
                                                  params['P_L'], params['P_H'], params['BITS_NUM'])
        while best_f != 0 and k < params['MAX_ITER']:
            n_population = population[:]
            while len(n_population) < params['POP_NUM'] + params['NPOP_NUM']:
                ch1 = algorithms.tournament(population, params['TOURNAMENT_SIZE'])
                ch2 = algorithms.tournament(population, params['TOURNAMENT_SIZE'])
                ch3, ch4 = algorithms.crossover(ch1, ch2)

                ch3 = algorithms.mutation(ch3, params['PROBABILITY'])
                ch4 = algorithms.mutation(ch4, params['PROBABILITY'])

                n_population.append((algorithms.calc_cost(algorithms.decode(ch3, params['P_L'], params['P_H'],
                                                                            params['BITS_NUM'])), ch3))
                n_population.append((algorithms.calc_cost(algorithms.decode(ch4, params['P_L'], params['P_H'],
                                                                            params['BITS_NUM'])), ch4))

            population = sorted(n_population, key=lambda x: x[0])[:params['POP_NUM']]

            cost = population[0][0]
            average = sum([p[0] for p in population])/params['POP_NUM']
            average_cost.append((k, average))
            best_cost.append((k, cost))

            f.write(str(k+1) + '. - best = ' + str(round(cost, 2)) + ', average = ' + str(round(average, 2)) + '\n')

            if best_f is None or best_f > cost:
                best_f = cost
            k += 1

        if best_ever_f is None or best_ever_f > best_f:
            best_ever_f = best_f

        best_cost_all.append(best_cost)
        average_cost_all.append(average_cost)
        f.write('----------------------------------------------------------\n')

    f.write('BEST EVER: ' + str(round(best_ever_f, 2)) + '\n')
    f.close()
    draw(best_cost_all, 'BEST')
    draw(average_cost_all, 'AVERAGE')


if __name__ == '__main__':
    print('Program started!')
    # compile_c_program()
    read_config_file()
    print('PARAMS: ' + str(params))
    nn()
