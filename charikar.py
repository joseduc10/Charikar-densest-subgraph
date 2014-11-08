from networkx import *
import fibonacci_heap_mod

def charikarHeap(G):
         
    E = G.number_of_edges()
    N = G.number_of_nodes()
    fib_heap = fibonacci_heap_mod.Fibonacci_heap()
    entries = {}
    order = []
    S = copy.deepcopy(G)
    
    for node, deg in S.degree_iter():
        entries[node] = fib_heap.enqueue(node, deg)
        
    best_avg = 0.0    
    iter = 0
    
    while fib_heap:
        avg_degree = (2.0 * E)/N
        
        if best_avg <= avg_degree:
            best_avg = avg_degree
            best_iter = iter
            
        min_deg_obj = fib_heap.dequeue_min()
        min_deg_node = min_deg_obj.get_value()
        order.append(min_deg_node)
        #print min_deg_obj.get_priority(), min_deg_node
            
        for n in S.neighbors_iter(min_deg_node):
            fib_heap.decrease_key(entries[n], 1)
            #E -= 1
            
        S.remove_node(min_deg_node)
        E -= min_deg_obj.get_priority()
        N -= 1
        iter += 1
        
    S = copy.deepcopy(G)       
    for i in xrange(best_iter):
        S.remove_node(order[i])
    return S, best_avg
    
    
def charikarDicts(G):
 
    S = copy.deepcopy(G)
    
    #E = sum((G.degree(weight = attr)).values())
    
    E = G.number_of_edges()
    N = G.number_of_nodes()
    
    nodes = {}
    best_avg = 0.0    
    iter = 0
    order = []
    
    for node, deg in G.degree_iter():
        nodes[node] = S[node]
        
    while nodes.keys():
        avg_degree = (2.0 * E)/N
        
        if best_avg <= avg_degree:
            best_avg = avg_degree
            best_iter = iter
            
        min_deg = N
        for n, neigh in nodes.iteritems():
            if min_deg > len(neigh):
                min_deg = len(neigh)
                min_deg_node = n
                
        #print min_deg, min_deg_node
        
        order.append(min_deg_node)
            
        for neigh in nodes[min_deg_node].keys():
            #E -= nodes[neigh][min_deg_node] if attr else 1
            #E -= 1
            del nodes[neigh][min_deg_node] 
            
        del nodes[min_deg_node]
        E -= min_deg
        N -= 1
        iter += 1
    
    S = copy.deepcopy(G)
    for i in xrange(best_iter):
        S.remove_node(order[i])
    return S, best_avg
    
