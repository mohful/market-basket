# HOW TO RUN THE PROGRAM
If you do not have numpy installed, or itertools, please do that before running the program. These libraries are necessary in order to extract results.

Here is the breakdown of all the files:
main.py: The main file that runs every algorithm. This is what you are supposed to run. I have divided this file into two parts. The first part is for Retail, and the second is for Netflix. I have commented the beginning of the netflix dataset, so you can run every algorithm for each dataset individually or together. 

apriori.py: Apriori algorithm
PCY.py: PCY algorithm
randomsamp.py: Random Sampling Algorithm
SON.py: SON algorithm
multihash.py: Multihash algorithm

Just run main.py

Also, for the netflix dataset, I have commented out some code in apriori, pcy and multihash that writes partial itemsets to the file. If you want to try that out, please uncomment them and run the code, otherwise it wont write anything since itll take a while to process. If you have a fast machine then that might make a difference and you wont have to uncomment.

ALSO, I HAVE NOT INCLUDED THE DATA FILES IN MY SUBMISSION BECAUSE OF THE SIZE LIMITATION ON ECLASS. PLEASE INCLUDE THE DATASETS BEFORE YOU RUN MAIN.PY!