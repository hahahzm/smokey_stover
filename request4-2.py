import math

class Node:
    def __init__(self):
        self.key = None
        self.parent = None
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        n = self.root
        while True:
            if n.key == None:
                n.key = key
                break
            elif key < n.key:
                if n.left == None:
                    n.left = Node()
                    n.left.parent = n
                n = n.left
            else:
                if n.right == None:
                    n.right = Node()
                    n.right.parent = n
                n = n.right

    def display(self):
        depth = 0
        visit = [self.root]
        while visit:
            for i in range(0, len(visit)):
                n = visit.pop()
                if n.left != None:
                    visit.insert(0, n.left)
                if n.right != None:
                    visit.insert(0, n.right)
                print "%3d " % n.key,
            print
            depth += 1

    def ancestor(parent, child):
        n = self.root
        while True:
            if parent == n.key:
                break
            elif parent < n.key:
                n = n.left
            else:
                n = n.right
        yes = False
        while n != None
            if child == n.key:
                yes =True
                break
            elif child < n.key:
                n = n.left
            else:
                n = n.right

        return yes

def crowd(a, b):
    

def answer(seq):
    # your code here
    # parents first, children second
    bunnies = Tree()

    #insertion takes O(n^2)
    for num in seq:
        bunnies.insert(num)

    bunnies.display()





answer([5, 9, 8, 2, 1])
answer([5, 2, 9, 1, 8])