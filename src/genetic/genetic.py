import sys
import random
from operator import itemgetter
sys.path.append("../../src/communication")
from communication import Communicator


POOL_SIZE = 30
SELECTION_SIZE = 10
GENERATION_SIZE = 15
comm = Communicator()
KEYS = "ABCDEFGHIJKLMNOP"


# do all the necessary stuff
def solve():
    # default pool of genes for QWOP.
    # TODO should use random strings later on

    pool = initiate()

    for _ in range(GENERATION_SIZE):

        # select genes from our pool
        chosen = select(pool)

        # crossover chosen genes
        replacement = crossover(chosen)

        # mutate genes
        mutate(replacement)

        # replace them
        pool = replacement

        print(pool)

    # return target string
    return "ABCD"


# randomly populate our pool for start of algorithm
def initiate():
    ret = []
    for _ in range(POOL_SIZE):
        length = random.randint(20, 30)  # length of each sequence
        seq = ''.join(random.choice(KEYS) for _ in range(length))
        ret.append(seq)
    return ret


def evaluate(pool):
    ret = []
    for seq in pool:
        dist, dur = comm.run(seq)
        ret.append((seq, dist, dur))

    return ret


#  fitness function that returns a value when given distance, and duration.
def fitness(dist, dur):
    #  as of now we are only going to use distance as a fitness value.
    return dist


def select(pool):
    buf = []

    # actually run with our sequences
    ret = evaluate(pool)

    # calculate fitness for each gene(sequence).
    for e in ret:
        seq, dist, dur = e
        buf.append((seq, fitness(dist, dur)))

    buf.sort(key=itemgetter(1), reverse=True)

    # current selection strategy will be to choose top 10.
    return [tup[0] for tup in buf[:SELECTION_SIZE]]


# crossover strategy would be to splice the sequence randomly and join them
def crossover(pool):
    ret = []

    # we will have to crossover POOL_SIZE times to populate our new pool.
    for _ in range(POOL_SIZE):
        x = random.choice(pool)
        y = random.choice(pool)

        idx = random.randint(0, min(len(x), len(y))-1)

        child = x[:idx] + y[idx:]
        ret.append(child)

    return ret


# mutation strategy would be to
# replace one character of one sequence from our pool.
def mutate(pool):
    idx = random.randint(0, len(pool)-1)
    seq = pool[idx]

    mut_idx = random.randint(0, len(seq)-1)
    mut_char = random.choice(KEYS)

    pool[idx] = seq[:mut_idx] + mut_char + seq[mut_idx+1:]
