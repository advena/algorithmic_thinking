import random

def er(n, p):
    nodes = [x for x in range(0,n)]
    edges= []
    for i in nodes:
        for j in nodes:
            if i != j:
                a = random.random()
                edge = [i,j]
                edge.sort()
                if a < p and edge not in edges:
                    edges.append(edge)
    return (nodes, len(edges))

print er(10,0)
print er(10,1)
print er(10,2)
