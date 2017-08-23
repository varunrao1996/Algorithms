def get_graph(get_file):
    
    adj = []
    
    lines = open(get_file).read().splitlines()
    
    for line in lines:
        
        adj.append([])
        data = line.split()
        v = int(data[0])-1
        
        for tpl in data[1:]:
            
            ts, ws = tpl.split(',')
            t = int(ts)-1
            w = int(ws)
            
            adj[v].append((t, w))

    return adj


def extract_min(z, wt):
    
    i = 0
    j = 1
    m = wt[z[0]]
    
    while j < len(z):
        if wt[z[j]] < m:
            i = j
            m = wt[z[j]]
        j += 1
    
    res = z[i]
    
    z[i] = z[-1]
    z.pop()
    
    return res


def spath(graph, s):
    
    infinity = 1000000
    
    wt = [infinity]*len(graph)
    wt[s] = 0
    
    zueue = [i for i in range(len(graph))]
    
    visited = [False]*len(graph)
    
    while len(zueue) > 0:
                
        v = extract_min(zueue, wt)
        visited[v] = True
    
        for inc, w in graph[v]:
            if not visited[inc]:
                wt[inc] = min(wt[inc], wt[v]+w)
                
    return wt


def main():
    
    question = [7,37,59,82,99,115,133,165,188,197]
    
    graph = get_graph('path.txt')
    wt = spath(graph, 0)
    
    res = []
    for i in question:
        res.append(str(wt[i-1]))
        
    print(','.join(res))       
    
    

if __name__ == '__main__':
    main()


#Answer: 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
