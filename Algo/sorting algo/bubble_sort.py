class bubbleSort:

    def __init__(self,array:list,key:str):
        self.array=array
        if len(self.array)>0:
            if key=='ASC':
                self.sort = self.sortASC(self.array)
            elif key=='DESC':
                self.sort = self.sortDESC(self.array)

    def sortASC(self,array):
        for _ in array:
            swapped = False
            for i in range(0,len(array)-1):
                j = i+1
                if array[i]>array[j]:
                    array[i],array[j]=array[j],array[i]
                    swapped = True
            if not swapped:
                return self.array

        return self.array

    def sortDESC(self,array):
        for _ in array:
            swapped = False
            for i in range(0,len(array)-1):
                j = i+1
                if array[i]<array[j]:
                    array[i],array[j]=array[j],array[i]
                    swapped = True
            if not swapped:
                return self.array

        return self.array

#input array
array = [386, 1833, 445, 72, 603, 233, 1036, 622, 1357, 531, 1609, 475, 1284, 171, 463, 398, 111, 1745, 189, 1176, 146, 1942, 896, 1276, 118]

# sorting in accending order
x = bubbleSort(array,'ASC').sort
print(x)
# ouput = [72, 111, 118, 146, 171, 189, 233, 386, 398, 445, 463, 475, 531, 603, 622, 896, 1036, 1176, 1276, 1284, 1357, 1609, 1745, 1833, 1942]

# sorting in descending order
x = bubbleSort(array,'DESC').sort
print(x)
# ouput = [1942, 1833, 1745, 1609, 1357, 1284, 1276, 1176, 1036, 896, 622, 603, 531, 475, 463, 445, 398, 386, 233, 189, 171, 146, 118, 111, 72]