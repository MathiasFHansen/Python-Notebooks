
import numpy as np
import matplotlib.pyplot as plt
stat_kode = 'befkbhalderstatkode.csv'

if __name__ == '__main__':
    #AAR,BYDEL,ALDER,STATKODE,PERSONER

    neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}
    dd = np.genfromtxt(stat_kode, delimiter=',', dtype=np.uint, skip_header=1)

    mask = (dd[:,0] == 2015) & (dd[:,3] == 5100)

    

    def number_of_people_per_neighbourhood(n, mask):
        all_people_in_given_n = dd[mask & (dd[:,1] == n)]
        sum_of_people = all_people_in_given_n[:,4].sum() # index 4 is no of 'PERSONER'
        return sum_of_people

    danish_neighbourhoods = np.array([number_of_people_per_neighbourhood(n, mask) for n in neighb.keys()])
    #print(danish_neighbourhoods)
    sorted_array = np.sort(danish_neighbourhoods)
    print(sorted_array)
    #plt.bar(list(set(dd[:,1])), sorted_array)
    #plt.show()
    #44744.1, 65846.2, 66715.3, 51898.4, 44868.5, 35666.6, 34300.7, 42662.8, 47873.9, 55452.10,  2590.99
    #plt.bar(list(set(dd[:,1])), list(dd[mask][:,4]))
    #plt.axis([1,10,300,600])

        #2590 = 99, 34300 = 7, 35666 = 6, 42662 = 8, 44744 = 1, 44868 = 5, 47873 = 9, 51898 = 4, 55452 = 10, 65846 = 2, 
        # 66715 = 3