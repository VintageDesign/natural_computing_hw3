import numpy as np

arr = np.zeros((10, 10))
arr[0][0] = 1
arr[1][1] = 2
arr[2][2] = 3
arr[3][3] = 4
arr[4][4] = 5
arr[5][5] = 6
arr[6][6] = 7
arr[7][7] = 8
arr[8][8] = 9
arr[9][9] = 10
print(arr)

arr1 = arr[2:8, 2:8]
print(arr1)
unique, count = np.unique(arr1, return_counts = True)

sub_dict = dict(zip(unique, count))
print(sub_dict[-1])
