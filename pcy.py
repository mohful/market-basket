from itertools import combinations
import numpy as np

freq_itemsets = open("freq-itemsets.txt", "a")

def pcy_algorithm(dataset, s, bucket_size):
    # Pass 1: Counting and Hashing
    C = {}
    hash_table = [0] * bucket_size

    for row in dataset:
        for item in row:
            if item in C:
                C[item] += 1
            else:
                C[item] = 1
                
        pairs = list(combinations(row, 2))
        for pair in pairs:
            bucket = (int(pair[0]) + int(pair[1])) % bucket_size
            hash_table[bucket] += 1

    frequent_buckets = [1 if count >= s else 0 for count in hash_table]
    
    L_k = frequent_itemset(C, s)
    freq_itemsets.write(", ".join([f"{key}: {value}" for key, value in L_k.items()]))
    frequent_L = [L_k]
    k = 2

    while len(frequent_L[k - 2]) > 0:
        C_k = generate_candidate_itemset(frequent_L[k - 2], dataset, k)
        freq_itemsets.write(", ".join([f"{key}: {value}" for key, value in L_k.items()]))
        L_k = frequent_itemset_with_bitmap(C_k, frequent_buckets, s, bucket_size, k)
        frequent_L.append(L_k)
        k += 1
        
    return frequent_L


def frequent_itemset_with_bitmap(C_k, frequent_buckets, s, bucket_size, k):
    if k == 2:
        L = {}
        for itemset in C_k:
            bucket = (int(itemset[0]) + int(itemset[1])) % bucket_size
            if frequent_buckets[bucket] == 1:
                if C_k[itemset] >= s:
                    L[itemset] = C_k[itemset]
        return L
    else:
        return frequent_itemset(C_k, s)

def frequent_itemset(basket, s):
    L = {}
    for item in basket:
        if (basket[item] >= s):
            L[item] = basket[item]
    return L

def generate_candidate_itemset(L, dataset, k):
    C = {}
    if k == 2:
        pairs = list(combinations(L.keys(), k))
        for pair in pairs:
            for row in dataset:
                tuple_exists = all(item in row for item in pair)
                if (tuple_exists):
                    if pair in C:
                        C[pair] += 1
                    else:
                        C[pair] = 1
        return C
    
    else:
        for itemset1 in L:
            for itemset2 in L:
                candidate = tuple(sorted(set(itemset1 + itemset2)))
                
                if len(candidate) == k and len(set(candidate)) == k:
                    C[candidate] = 0

        for row in dataset:
            for candidate in C:
                if set(candidate).issubset(row):
                    C[candidate] += 1
        
        return C