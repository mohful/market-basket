import numpy as np
import random as rd
from apriori import apriori


def random_sample(dataset, s, rate):
    random_sample = rd.sample(dataset, int(rate * len(dataset)))
    apriori_algo = apriori(random_sample, s * rate)
    return apriori_algo
