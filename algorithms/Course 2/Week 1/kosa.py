import os
import sys
import threading

def get_graph(get_file):
    f = open(get_file)
    
    adj = []
    reverse = []
    
    line = f.readline()
    while line != '':
        num1, num2 = line.split()
        vfrom = int(num1)
        vto = int(num2)
        vmax = max(vfrom, vto)
        
        while len(adj) < vmax:
            adj.append([])
        while len(reverse) < vmax:
            reverse.append([])
            
        adj[vfrom-1].append(vto-1)
        reverse[vto-1].append(vfrom-1)
        
        line = f.readline()
            
    return adj, reverse


t = 0
s = None
explored = None
leader = None
scc_size = 0
sort = None

def dfscount(graph_rev, n):
    
    global t, explored, sort
    
    t = 0
    explored = [False]*n
    sort = [None]*n
    
    for i in reversed(range(n)):
        if not explored[i]:
            dfs(graph_rev, i)
                        
            
def dfs(graph_rev, i):
    
    global t, explored
    
    explored[i] = True
    
    for v in graph_rev[i]:
        if not explored[v]:
            dfs(graph_rev, v)
    
    sort[t] = i
    t += 1
    
    
def dfscountnext(graph):
    
    global scc_size, explored, sort
    
    explored = [False]*len(graph)
    res = []
    
    for i in reversed(range(len(graph))):
        if not explored[sort[i]]:
            scc_size = 0
            dfsnext(graph, sort[i])
            res.append(scc_size)
            
    return res
    
    
def dfsnext(graph, i):
    
    global explored, scc_size
    
    explored[i] = True
    
    for v in graph[i]:
        if not explored[v]:
            dfsnext(graph, v)
    
    scc_size += 1
    

def kosa(graph, graph_rev):
    
    dfscount(graph_rev, len(graph))
    res = dfscountnext(graph)
    
    return res


def main():
    
    graph, graph_rev = get_graph('scc.txt')
    
    res = kosa(graph, graph_rev)
    
    print(','.join(map(lambda x: str(x), sorted(res)[::-1][:5])))


if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target = main)
    thread.start()