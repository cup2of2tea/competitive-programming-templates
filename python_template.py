'''           Collaborative CP template by h25

  https://github.com/h25io/competitive-programming-templates

   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-
  / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \
 `-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'''

MOD = 10**9+7
MOD_EDU = 998244353 # Used in CodeForces educational rounds

# TODO :
### Data structures
# Graph/tree
# Segment tree
### Algorithms
# isPrime
# getDivisors/getPrimeDivisors
# Binary search
# Iterative BFS/DFS
# Matrix fastpow

def iinput():
    return int(input())
    
def linput():
    return list(map(int, input().split()))

def arr2d(nrows, ncols, default=0):
    return [[default for c in range(ncols)] for r in range(nrows)]

# This function handles multiple testcases and Google Code Jam formatting
def codejam():
    nTestcases = iinput()
    for testcaseId in range(1, nTestcases + 1):
        print(f'Case #{testcaseId}: ', end='')
        solve()

class MergeFind(object):
    def __init__(self):
        self.parent = collections.defaultdict(lambda:None)
    def find(self,x):
        path=[]
        while x is not None:
            path.append(x)
            x = self.parent[x]
        x = path.pop()
        for e in path:
            self.parent[e] = x
        return x
    def merge(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.parent[xroot] = yroot
        return yroot
        
# Get a sorted list of primes up to uplimit (included).
# Takes around 50ms for primes below 1M.
def generatePrimes(uplimit):
    factors=[0]*(uplimit+1)   
    primes=[2] if uplimit>=2 else []
    for i in range(3,uplimit+1,2): #on va passer en revue tous les impairs
        if not factors[i]:
            primes.append(i)
            for j in range(3*i,uplimit+1,i<<1):  #seuls les facteurs k*p avec p premier et k impair méritent d'être marqués
                factors[j]=1
    return primes

'''.-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-
  / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \
 `-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'''

### Useful imports (uncomment only when needed to save performance)

#import collections
#import fractions
#import math
#import random
#import sys

def solve():
    print(int(input()))

if __name__ == '__main__':
    solve()