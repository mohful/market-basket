import numpy as np
import random as rd
from apriori import apriori

def SON(dataset, s, num_chunks):
    chunks = chunk_data(dataset, num_chunks)
    frequent = []
    for chunk in chunks:
        apriori_algo = apriori(chunk, s / num_chunks)
        frequent.append(apriori_algo)
    return frequent

def chunk_data(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    return chunks