'''
Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval,
narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
'''

def find_element(lst:list,num:int) ->int:
    
    low = 0
    high = len(lst)
    while low<high:
        mid = (low+high)//2
        if lst[mid]==num:
            return mid
        elif lst[mid]<=num:
            low=mid
        else:
            high=mid
        
    return "Does not exist"


while True:
    try:
        lst = list(map(int,input('Enter space seperated sequential numbers : ').split()))
        num = int(input('Enter any number to search from the sequence : '))
    except Exception as e:
        print(e)
    print(find_element(lst,num))
