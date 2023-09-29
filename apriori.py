from itertools import combinations

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
    
    # Read baskets and count in main memory the occurences of pair of items where the individual items are frequent
    pairs = list(combinations(L_1.keys(), 2))
    print(pairs)

    C_2 = {}
    for pair in pairs:
        for row in dataset:
            tuple_exists = all(item in row for item in pair)
            if (tuple_exists):
                if pair in C_2:
                    C_2[pair] += 1
                else:
                    C_2[pair] = 1
    # print(C_2)
    L_2 = frequent_itemset(C_2, s)
    # print(L_2)
    return L_1

def frequent_itemset(basket, s):
    L = {}
    for item in basket:
        if (basket[item] >= s):
            L[item] = basket[item]
    return L

def generateCandidateItemsets(dataset, s, degree):
    if degree >= 2:
        return "Multiple Pair Item Candidate Set"
    else:
        return ""
    return True
