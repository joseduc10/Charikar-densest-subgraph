from networkx import *
import charikar as ch
import time


G = nx.read_gml('test.gml')
Gn, Gm =  G.number_of_nodes() , G.number_of_edges()
print 'graph stats:'
print '# nodes', Gn
print '# edges', Gm
print 'avg degree', 2.0*Gm/Gn

print '-------'
print 'Charikar with dicts:'
tic = time.clock()
S, avg = ch.charikarDicts(G)
toc = time.clock()
print 'time', toc-tic
print 'Average degree', avg
Sn, Sm =  S.number_of_nodes() , S.number_of_edges()
print 'Dense subgraph stats:'
print '# nodes', Sn
print '# edges', Sm
print 'avg degree', 2.0*Sm/Sn

print '-------'
print 'Charikar with heap:'
tic = time.clock()
S, avg = ch.charikarHeap(G)
toc = time.clock()
print 'time', toc-tic
print 'Average degree',avg
Sn, Sm =  S.number_of_nodes() , S.number_of_edges()
print 'Dense subgraph stats:'
print '# nodes', Sn
print '# edges', Sm
print 'avg degree', 2.0*Sm/Sn