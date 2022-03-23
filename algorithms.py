import math
import subprocess
import random


# svaki gen se koduje na bits_num binarnih cifara
def code(genes, p_l, p_h, bits_num):
    chromosomes = []
    for gen in genes:
        p_norm = round((float(gen) - p_l) / (p_h - p_l), 3)
        coded_gen = []

        for m in range(0, bits_num):
            genes_sum = 0
            for i in range(0, m):
                genes_sum += coded_gen[i] * 2**(-(i+1))
            coded_gen.append(math.ceil(p_norm - 2**(-(m+1)) - genes_sum))
        chromosomes += coded_gen

    return chromosomes


# dekodovanje hromozoma, svaki gen dekodujemo sa bits_num binarnih cifara
def decode(ch, p_l, p_h, bits_num):
    genes = []
    n = int(len(ch) / bits_num)

    for i in range(0, n):
        p_norm = 0
        for m in range(0, bits_num):
            p_norm += ch[i*bits_num + m] * 2**(-(m+1))

        p_norm += 2**(-(bits_num + 1))
        genes.append(str(round(p_norm*(p_h - p_l) + p_l, 3)))

    return genes


# racunanje troska
def calc_cost(genes):
    args = ['./g'] + genes
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()

    return float(stdout)


# kreiranje populacije
def create_population(pop_num, ch_size, p_l, p_h, bits_num):
    population = [[random.randint(0, 1) for _ in range(0, ch_size)] for _ in range(0, pop_num)]
    population_tuple = []

    for p in population:
        population_tuple.append((calc_cost(decode(p, p_l, p_h, bits_num)), p))

    return population_tuple


# biranje hromozoma za parenje
def tournament(population, size, ch_cost):
    picked = []
    for _ in range(0, size):
        picked.append(random.choice(population))

    best = None
    best_cost = None
    for p in picked:
        cost = abs(p[0] - ch_cost)
        if best_cost is None or best_cost > cost:
            best = p[1]
            best_cost = cost

    return best


# ukrstanje hromozoma - jednotackasto
def crossover(ch1, ch2):
    r = random.randrange(1, len(ch1) - 1)
    ch3 = ch1[:r] + ch2[r:]
    ch4 = ch2[:r] + ch1[r:]

    return ch3, ch4


# mutiranje hromozoma - flipovanje proizvoljno bitova
def mutation(ch, probability):
    for i in range(0, len(ch)):
        if random.random() <= probability:
            if ch[i] == 1:
                ch[i] = 0
            else:
                ch[i] = 1

    return ch
