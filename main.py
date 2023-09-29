import matplotlib.pyplot as plt
import numpy as np
from apriori import apriori

retail_file = open("retail.dat", 'r')
netflix_file = open('netflix.data', 'r')

retail_store_data = []
netflix_data = []

for line in retail_file:
    retail_store_data.append(line[:-2].split(" "))

print(retail_store_data)

for line in netflix_file:
    netflix_data.append(line[:-2].split(" "))

# Retail Store Analysis
s_1 = int(len(retail_store_data) / 100)
one_percent_retail = apriori(retail_store_data, s_1)
print(one_percent_retail)

# s_2 = int(len(retail_store_data) / 50)
# two_percent_retail = apriori(retail_store_data, s_2)
# print(two_percent_retail)

# # Netflix Analysis

# # to find the subsets
# twenty = int(len(netflix_data) * 20 / 100)
# forty = int(len(netflix_data) * 40 / 100)
# sixty = int(len(netflix_data) * 60 / 100)
# eighty = int(len(netflix_data) * 80 / 100)
# hundred = int(len(netflix_data))

# # one percent and two percent of the data
# netflix_s1 = int(len(netflix_data) / 100)
# netflix_s2 = int(len(netflix_data) / 50)

# # 
# ss_1 = netflix_data[:twenty]
# twenty_netflix_s1 = apriori(ss_1, netflix_s1)
# print(twenty_netflix_s1)

# twenty_netflix_s2 = apriori(ss_1, netflix_s2)
# print(twenty_netflix_s2)

# #
# ss_2 = netflix_data[:forty]
# forty_netflix = apriori(ss_2, s_2)
# print(forty_netflix)

# #
# ss_3 = netflix_data[:sixty]
# sixty_netflix = apriori(ss_3, s_2)
# print(sixty_netflix)

# #
# ss_4 = netflix_data[:eighty]
# eighty_netflix = apriori(ss_4, s_2)
# print(eighty_netflix)

# #
# hundred_netflix = apriori(netflix_data, s1)


