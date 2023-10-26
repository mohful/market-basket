from itertools import combinations

freq_itemsets = open("freq-itemsets.txt", "a")

def apriori(dataset, s):
    # Read baskets and count in main memory the occurrences of each individual item
    C = {}
    for row in dataset:
        for item in row:
            if item in C:
                C[item] += 1
            else:
                C[item] = 1
    L_1 = frequent_itemset(C, s)
    freq_itemsets.write(", ".join([f"{key}: {value}" for key, value in L_1.items()]))

    frequent_L = [L_1]
    k = 2

    while len(frequent_L[k - 2]) > 0:
        C_k = generate_candidate_itemset(frequent_L[k - 2], dataset, k)
        L_k = frequent_itemset(C_k, s)
        freq_itemsets.write(", ".join([f"{key}: {value}" for key, value in L_k.items()]))
        frequent_L.append(L_k)
        k += 1

    return frequent_L

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