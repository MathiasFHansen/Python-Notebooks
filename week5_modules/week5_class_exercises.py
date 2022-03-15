from ast import Index
import pandas as pd
import numpy as np

if __name__ == '__main__':
    data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])

    our_dataset = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])
    Index(['Row1', 'Row2', 'Row3'], dtype='object')
    Index(['Col1', 'Col2', 'col3'], dtype='object')

    #1
    #print(our_dataset['Col2'])

    #2
    third_row = our_dataset.iloc[0:3,2]
    #print(third_row)
    #3
    element_3row_2col = our_dataset.iloc[2,1]
    print(element_3row_2col)




