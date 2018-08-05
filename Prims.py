from random import choice
import sys
from Heap import Heap
from Graph import Graph
        
def prims(graph, n, m, startVertex):    
    minHeap = Heap()
    dist = {}
    parent=[]
    for x in graph.vertices1:
        minHeap.array.append(minHeap.addNode(x[0], sys.maxsize))
        dist[x[0]] = int(sys.maxsize)
        minHeap.pos.append(x[0])
        parent.append(-1)
        
    minHeap.pos[startVertex] = startVertex
    dist[startVertex]=0
    minHeap.decreaseKey(startVertex,dist[startVertex])
    minHeap.size=n
    while minHeap.size != 0:
        root = minHeap.extractMin()
        u = root[0]
        for adj in graph.graph[u]:
            v = adj[0]
            distV =int(adj[1])
            if minHeap.isPresent(v) and (distV<dist[v]):
                dist[v] = distV
                parent[v]=u
                minHeap.decreaseKey(v, dist[v])
    
    graph.printMSTEdges(dist,parent,n,startNode)

#Start 
#Read input from file
f='input.txt' # can use input.txt, input2.txt, input3.txt
global vertices1
start=-1
path = []
startNode=''
vertices = []
edges=[]
with open(f) as fp:
    line = fp.readline()
    line1 = line.split()
    n=int(line1[0]) #Number of vertices
    m=int(line1[1]) #Number of edges
    if(line1[2] != 'U'):
        print("Please enter an undirected graph.")
        sys.exit()
    graph = Graph(n)    
    for i in range(0,m):
        line = fp.readline()
        line1 = line.split()        
        if line1[0] not in vertices:
            vertices.append(line1[0])
        if line1[1] not in vertices:
            vertices.append(line1[1])        
        edges.append([line1[0], line1[1], line1[2]])
    line = fp.readline()
    if line:
        s_node = line[0]
        if s_node!='\n':
            startNode = s_node 
       
    graph.vertices1 = list(enumerate(sorted(set(vertices)),0))
    
    for edge in edges:
        node1 = graph.getNum(edge[0])
        node2 = graph.getNum(edge[1])
        graph.addEdge(node1, node2, edge[2])
        graph.addEdge(node2, node1, edge[2])
    
if(startNode==''):
    #Randomly pick any node as a start node
    startNode=choice(vertices)
    start= graph.getNum(startNode)
    prims(graph,n, m, start)
    
    '''#Logic for printing MST Cost from each node if start node is not provided
    for x in range(n):
        print("Source Vertex is ",graph.vertices1[x][1])
        startNode=graph.vertices1[x][1]
        prims(graph,n, m, getNum(startNode))
        print("\n")'''
else:
    start= graph.getNum(startNode)           
    if(start==-1):
        print("Please enter a valid start point")
    else:
        prims(graph,n, m, start)