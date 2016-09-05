import math
import operator
import itertools

cache = dict()
cache2 = dict()
cache3 = dict()

class Node:
    def __init__(self):
        self.key = None
        self.parent = None
        self.right = None
        self.left = None
        self.population = 1 #number of nodes under itself, self-inclusive
        self.sets = 0

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        """ building the tree"""
        n = self.root
        while True:
            if n.key == None:
                n.key = key
                break
            elif key < n.key:
                n.population += 1
                if n.left == None:
                    n.left = Node()
                    n.left.parent = n
                n = n.left
            else:
                n.population += 1
                if n.right == None:
                    n.right = Node()
                    n.right.parent = n
                n = n.right

    def bottomup(self):
        """ traverse the tree with BFS in a bottomup order
            combine and update the sets value for each node"""
        depth = 0
        visit = [self.root]
        trip = [self.root]
        while visit:
            for i in range(0, len(visit)):
                n = visit.pop()
                if n.left != None:
                    visit.insert(0, n.left)
                    trip.insert(0, n.left)
                if n.right != None:
                    visit.insert(0, n.right)
                    trip.insert(0, n.right)
            depth += 1
        for n in trip:
            if (n.left == None) and (n.right == None):
                n.sets = 1
            elif (n.right == None):
                n.sets = n.left.sets
            elif (n.left == None):
                n.sets = n.right.sets
            else:
                n.sets = n.left.sets * n.right.sets * joint(n.left.population, n.right.population)

    def ancestor(self, a, b):
        n = self.root
        while True:
            if n.key == a:
                break
            elif a < n.key:
                n = n.left
            else:
                n = n.right
        result = False
        while True:
            if n == None:
                break
            elif n.key == b:
                result = True
                break
            elif b < n.key:
                n = n.left
            else:
                n = n.right
        return result

    def satisfy(self, query):
        for i in range(0, len(query)):
            for j in range(0, i):
                if self.ancestor(query[i], query[j]):
                    return False
        return True

    def rootSets(self):
        """returns number of possible sets under root node"""
        return self.root.sets 



def crowd(a, b):
    """ stirling number of the second kind
        reference: 
            https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
        """
    n = max(a,b)
    k = min(a,b)
    if (n,k) in cache:
        return cache[n,k]
    result = 0
    if n == k:
        result = 1
    elif (n == 0) or (k == 0):
        result = 0
    else:
        result = k * crowd(n - 1, k) + crowd(n - 1, k - 1)
    cache[n, k] = result
    return result

def crowd(a, b):
    return combination(a - 1, b - 1)

def combination(n, r):
    """ combination number with cache for performance boost
        """
    if n < r: return 0
    r = min(r, n-r)
    if r == 0: return 1
    if (n,r) in cache2:
        return cache2[n,r]
    numer = reduce(operator.mul, xrange(n, n-r, -1))
    denom = reduce(operator.mul, xrange(1, r+1))
    result = numer//denom
    cache2[n,r] = result
    return result


def joint(a, b):
    """ possible permutation of two sets of length a and b without
        changing the original order of each set
        cache for performance increase"""
    x = max(a,b)
    y = min(a,b)
    if (x,y) in cache3:
        return cache3[x,y]
    result = 0
    for m in range(1, y + 1):
        result += combination(x + 1, m) * crowd(y, m)
    cache3[x,y] = result
    return result

def answer(seq):
    # your code here
    bunnies = Tree()

    #insertion takes O(n^2)
    for num in seq:
        bunnies.insert(num)

    bunnies.bottomup()

    perms = itertools.permutations(seq, len(seq))

    perms = list(perms)

    count = 0

    for l in perms:
        if bunnies.satisfy(l):
            print l
            count += 1

    print count
    print joint(3,3)
    return str(bunnies.rootSets())

print answer([5,7,8,2,4,6,1])