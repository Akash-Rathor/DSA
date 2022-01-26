class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if current.data>data:
                    if not current.left:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left

                elif current.data<data:
                    if not current.right:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right
                else:
                    break

    # optional function to print binary tree
    def display(self):
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self,node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        if node.right is None and node.left is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

import random
a = BinaryTree()
listed = [16,52,52,6,9,13,15,42,93,176,43,96,54,92,105,634]
for _ in listed:
    a.insert(_)
b = BinaryTree()
listed = [5,4,8,12,56,78,45,19,25,65,14,25,96,35,456,569,589,698,452,563,48]
for _ in listed:
    b.insert(_)
b.display()



# pretty printed binary tree

'''
Output 1 for binary tree - 1
 _____16_____
/            \
6         __52_____
 \       /         \
 9_     42_     __93______     
   \       \   /          \    
  13_     43  54_     ___176_  
     \           \   /       \ 
    15          92  96_     634
                       \       
                      105 
'''



'''
Output 2 for binary tree - 2
 5
/ \
4 8_
    \
   12_____________
                  \
               __56___
              /       \
         ____45_     78_
        /       \   /   \
       19_     48  65  96____
      /   \                  \
     14  25_               _456____        
            \             /        \       
           35            452     _569_     
                                /     \    
                               563   589_  
                                         \ 
                                        698
'''