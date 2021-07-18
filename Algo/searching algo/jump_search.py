'''
Like Binary Search, Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements (than linear search) by 
jumping ahead by fixed steps or skipping some elements in place of searching all elements.
For example, suppose we have an array arr[] of size n and block (to be jumped) size m.
Then we search at the indexes arr[0], arr[m], arr[2m]…..arr[km] and so on. Once we find the interval (arr[km] < x < arr[(k+1)m]),
we perform a linear search operation from the index km to find the element x.
Let’s consider the following array: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610).
Length of the array is 16. Jump search will find the value of 55 with the following steps assuming that the block size to be jumped is 4. 
STEP 1: Jump from index 0 to index 4; 
STEP 2: Jump from index 4 to index 8; 
STEP 3: Jump from index 8 to index 12; 
STEP 4: Since the element at index 12 is greater than 55 we will jump back a step to come to index 8. 
STEP 5: Perform linear search from index 8 to get the element 55.
'''
import math
def jump_search(lst:list,num:int) -> int:
    low = 0
    high=len(lst)-1

    x = int(math.sqrt(len(lst)))
    while lst[low]<num and low<len(lst)-x:
        low+=x
    
    if lst[low]==num:
        return low
    elif lst[high]==num:
        return high

    if low<len(lst)-x:
        high=low
        low-=x
    else:
        low = low
        high = low+x

    print(low,high)

    for i in range(low,high+1):
        print(i,lst[i])
        if lst[i]==num:
            return i
        elif lst[i]>num:
            return 'Does not exist'

print(jump_search([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84],84))