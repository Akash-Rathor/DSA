def linear_search(array,num):

    for i in range(len(array)):
        if array[i]==num:
            return i


array = [i for i in range(50)]
num = 45
print(linear_search(array,num))