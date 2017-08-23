import sys
import math
import random

class UndirectedGraph:
    
    def __init__(self, vertices):
        self.adjacent = []
        while vertices > 0:
            self.adjacent.append([])
            vertices -= 1
        
        
    def copy(self):
        res = UndirectedGraph(0)
        for l in self.adjacent:
            res.adjacent.append(l[:])
        return res
        
        
    def add_edge(self, i, j):
     
        self.adjacent[i].append(j)
    
    def n(self):
        return len(self.adjacent)
    
    
    def merge(self, i, j):
        
        i_adj = self.adjacent[i]
        k = 0
        while k < len(i_adj):
            if i_adj[k] == j:
                i_adj.pop(k)
                k -= 1
            k += 1
        
        for v in self.adjacent[j]:
            if (v != i):
                self.add_edge(i, v)
                v_adj = self.adjacent[v]
                k = 0
                l = len(v_adj)
                while k < l:
                    if(v_adj[k] == j):
                        v_adj[k] = i
                        break
                    k += 1

        self.adjacent[j] = self.adjacent[self.n()-1]
        for v in self.adjacent[j]:
            v_adj = self.adjacent[v]
            k = 0
            l = len(v_adj)
            while k < l:
                if(v_adj[k] == (self.n()-1)):
                    v_adj[k] = j
                    break
                k += 1
        self.adjacent.pop()

    

def kargerr(graph, seed):

    random.seed(seed)
        
    while graph.n() > 2:
        i = random.randint(0, graph.n()-1)
        adj = graph.adjacent[i]
        j = random.choice(adj)
        
        graph.merge(i, j)

    return len(graph.adjacent[0])
    

def kargerMinCut(graph, N):

    i = 0

    min_res = kargerr(graph.copy(), i)
    while i < N:
        t = kargerr(graph.copy(), i)
        print(str(i)+': '+str(t))
        if t < min_res: min_res = t
        i += 1
        
    return min_res

if __name__ == '__main__':
    
    fileopen = open('karger_min_cut_input.txt')

    lines = fileopen.read().splitlines()
    fileopen.close()
    
    graph = UndirectedGraph(200)

    for line in lines:
        lst = line.split('\t')
        t = int(lst[0])-1
        for i in lst[1:-1]:
            v = int(i)-1
            graph.add_edge(t, v)
    
    N = math.log(graph.n())
    print(kargerMinCut(graph, N))
