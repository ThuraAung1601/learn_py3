#!/bin/python3

def hourglass(arr):
    sum_list = []
    R, C = len(arr), len(arr[0])
    # window size is 3 x 3
    for i in range(0, R-2): 
        for j in range(0, C-2):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sum_list.append(sum)
    return max(sum_list)
    
if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    print(hourglass(arr))
