import matplotlib.pyplot as plt
import numpy as np
from apriori import apriori
import time
from randomsamp import random_sample
import pandas as pd
from son import SON
from pcy import pcy_algorithm
from multihash import multihash

retail_file = open("retail.dat", 'r')
netflix_file = open('netflix.data', 'r')

retail_store_data = []
netflix_data = []

for line in retail_file:
    retail_store_data.append(line[:-2].split(" "))

for line in netflix_file:
    netflix_data.append(line[:-2].split(" "))

s_1 = int(len(retail_store_data) / 100)
s_2 = int(len(retail_store_data) / 50)

freq_itemsets = open("freq-itemsets.txt", "a")

freq_itemsets.write("---------------- APRIORI RETAIL STORE ONE PERCENT SUPPORT ----------------------------------- \n")
# Retail Store Analysis
start = time.time()
one_percent_retail = apriori(retail_store_data, s_1)
for row in one_percent_retail:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")  # Add a newline for separation between entries        
end = time.time()
freq_itemsets.write("AP 1% Time:: " + str(end - start) + "\n")

freq_itemsets.write("---------------- APRIORI RETAIL STORE TWO PERCENT SUPPORT ----------------------------------- \n")
start = time.time()
two_percent_retail = apriori(retail_store_data, s_2)
for row in two_percent_retail:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")  
end = time.time()
freq_itemsets.write("AP 2% Time:: " + str(end - start) + "\n")

freq_itemsets.write("---------------------- RANDOM SAMPLING RETAIL ONE PERCENT -------------------------------- \n")
start = time.time()
one_percent_rand = random_sample(retail_store_data, s_1, 0.1)
for row in one_percent_rand:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write("RS 1% Time:: " + str(end - start) + "\n")


freq_itemsets.write("---------------------- RANDOM SAMPLING RETAIL TWO PERCENT -------------------------------- \n")
start = time.time()
two_percent_rand = random_sample(retail_store_data, s_2, 0.1)
for row in two_percent_rand:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write("RS 2% Time:: " + str(end - start) + "\n")

freq_itemsets.write("---------------------- SON RETAIL ONE PERCENT -------------------------------- \n")
start = time.time()
SON_r1 = SON(retail_store_data, s_1, 10)
for chunk in SON_r1:
    for row in chunk:
        entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
        freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write("SON 1% Time: " + str(end - start) + "\n")


freq_itemsets.write("---------------------- SON RETAIL TWO PERCENT -------------------------------- \n")
start = time.time()
SON_r2 = SON(retail_store_data, s_2, 10)
for chunk in SON_r1:
    for row in chunk:
        entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
        freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write("SON 2% Time:: " + str(end - start) + "\n")

freq_itemsets.write("---------------------- PCY RETAIL ONE PERCENT -------------------------------- \n")
start = time.time()
pcy_r1 = pcy_algorithm(retail_store_data, s_1, 10000)
for row in pcy_r1:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write("PCY 1% Time:: " + str(end - start) + "\n")


freq_itemsets.write("---------------------- PCY RETAIL TWO PERCENT -------------------------------- \n")
start = time.time()
pcy_r2 = pcy_algorithm(retail_store_data, s_2, 10000)
for row in pcy_r2:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write("PCY 2% Time:: " + str(end - start) + "\n")

freq_itemsets.write("---------------------- MULTIHASH RETAIL ONE PERCENT -------------------------------- \n")
start = time.time()
mh_r1 = multihash(retail_store_data, s_1, 10000)
for row in mh_r1:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write("MH 1% Time:: " + str(end - start) + "\n")


freq_itemsets.write("---------------------- MULTIHASH RETAIL TWO PERCENT -------------------------------- \n")
start = time.time()
mh_r2 = multihash(retail_store_data, s_2, 10000)
for row in mh_r2:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write("MH 2% Time:: " + str(end - start) + "\n")

# Netflix Analysis

# to find the subsets
twenty = int(len(netflix_data) * 20 / 100)
forty = int(len(netflix_data) * 40 / 100)
sixty = int(len(netflix_data) * 60 / 100)
eighty = int(len(netflix_data) * 80 / 100)

# one percent and two percent of the data
netflix_s1 = int(len(netflix_data) / 100)
netflix_s2 = int(len(netflix_data) / 50)

freq_itemsets.write("-------------NETFLIX ONE PERCENT SUPPORT----------------------------- \n")
start = time.time()
one_percent_netflix = apriori(netflix_data[:int(len(netflix_data) * 20 / 100)], netflix_s1)
for row in one_percent_netflix:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write(end - start)

freq_itemsets.write("-------------NETFLIX TWO PERCENT SUPPORT----------------------------- \n")
start = time.time()
two_percent_netflix = apriori(netflix_data, netflix_s2)
for row in two_percent_netflix:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write(end - start)

print("---------------- APRIORI NETFLIX TWENTY PERCENT DATA ----------------------------------- \n")

ss_1 = netflix_data[:twenty]
twenty_netflix_s1 = apriori(ss_1, netflix_s1)
print(twenty_netflix_s1)

print("---------------- APRIORI NETFLIX FORTY PERCENT DATA ----------------------------------- \n")

ss_2 = netflix_data[:forty]
forty_netflix = apriori(ss_2, netflix_s1)
print(forty_netflix)

print("---------------- APRIORI NETFLIX SIXTY PERCENT DATA ----------------------------------- \n")

ss_3 = netflix_data[:sixty]
sixty_netflix = apriori(ss_3, netflix_s1)
print(sixty_netflix)

print("---------------- APRIORI NETFLIX EIGHTY PERCENT DATA ----------------------------------- \n")


ss_4 = netflix_data[:eighty]
eighty_netflix = apriori(ss_4, netflix_s1)
print(eighty_netflix)

print("---------------- APRIORI NETFLIX HUNDRED PERCENT DATA ----------------------------------- \n")

hundred_netflix = apriori(netflix_data, netflix_s1)
print(hundred_netflix)

freq_itemsets.write("---------------------- RANDOM SAMPLING NETFLIX ONE PERCENT -------------------------------- \n")
start = time.time()
one_percent_Nrand = random_sample(netflix_data, netflix_s1, 0.05)
for row in one_percent_Nrand:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write(str(end - start))


freq_itemsets.write("---------------------- RANDOM SAMPLING NETFLIX TWO PERCENT -------------------------------- \n")
start = time.time()
two_percent_Nrand = random_sample(netflix_data, netflix_s2, 0.05)
for row in two_percent_Nrand:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write(str(end - start))

freq_itemsets.write("---------------------- SON NETFLIX ONE PERCENT -------------------------------- \n")
start = time.time()
SON_n1 = SON(netflix_data, netflix_s1, 10)
for chunk in SON_n1:
    for row in chunk:
        entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
        freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write(str(end - start))

freq_itemsets.write("---------------------- SON NETFLIX TWO PERCENT -------------------------------- \n")
start = time.time()
SON_n2 = SON(netflix_data, netflix_s2, 10)
for chunk in SON_n2:
    for row in chunk:
        entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
        freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write(str(end - start))

freq_itemsets.write("---------------------- PCY NETFLIX ONE PERCENT -------------------------------- \n")
start = time.time()
pcy_n1 = pcy_algorithm(netflix_data, netflix_s1, 2**20)
for row in pcy_n1:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write(str(end - start))


freq_itemsets.write("---------------------- PCY NETFLIX TWO PERCENT -------------------------------- \n")
start = time.time()
pcy_n2 = pcy_algorithm(netflix_data, netflix_s2, 2**20)
for row in pcy_n2:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write(str(end - start))

freq_itemsets.write("---------------------- MULTIHASH NETFLIX ONE PERCENT -------------------------------- \n")
start = time.time()
mh_n1 = multihash(netflix_data, netflix_s1, 10000)
for row in mh_n1:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write(str(end - start))


freq_itemsets.write("---------------------- MULTIHASH NETFLIX TWO PERCENT -------------------------------- \n")
start = time.time()
mh_n2 = multihash(netflix_data, netflix_s2, 10000)
for row in mh_n2:
    entry_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
    freq_itemsets.write(entry_str + "\n")
end = time.time()
freq_itemsets.write(str(end - start))
