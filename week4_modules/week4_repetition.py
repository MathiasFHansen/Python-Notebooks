
import numpy as np
import matplotlib.pyplot as plt


# Exercise 1¶
# 1. Open the file './data/befkbhalderstatkode.csv'
stat_kode = 'befkbhalderstatkode.csv'


# 2. Turn the csv file into a numpy ndarray with `np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)`
dd = np.genfromtxt(stat_kode, delimiter=',', dtype=np.uint, skip_header=1)

# 3. Using this data:
# Find out how many people lived in each of the 11 areas in 2015
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
          10: 'Amager Vest', 99: 'Udenfor'}

#print (dd)
#print(dd[mask])

mask = (dd[:,0] == 2015) & (dd[:,3] == 5100)
def number_of_people_per_neighbourhood(n, mask):
    
    all_people_in_given_n = dd[mask & (dd[:,1] == n)]
    sum_of_people = all_people_in_given_n[:,4].sum()
    return sum_of_people

people_in_areas = np.array([number_of_people_per_neighbourhood(n     , mask) for n in neighb.keys()]) 
#print(people_in_areas)   
sorted_array = np.sort(people_in_areas)
# 4. Make a bar plot to show the size of each city area from the smallest to the largest in 2015
plt.bar(neighb, sorted_array)
# 5. Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
# 6. How many of those were from the other nordic countries (not dk). Hint: see notebook: "04 Numpy"
# 7. Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015
