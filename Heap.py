class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def addNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    # Operation to swap two node of minHeap
    def swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    # Heapify operation 
    def heapify(self, nodeX):
        smallest = nodeX
        l_child = 2*nodeX+1
        r_child = 2*nodeX+2

        if l_child < self.size and self.array[l_child][1] < self.array[smallest][1]:
            smallest = l_child

        if r_child < self.size and self.array[r_child][1] < self.array[smallest][1]:
            smallest = r_child

        if smallest != nodeX:
            self.pos[self.array[smallest][0]] = nodeX
            self.pos[self.array[nodeX][0]] = smallest
            self.swap(smallest, nodeX)
            self.heapify(smallest)

    #Operation to adjust heap elements 
    def decreaseKey(self, v, dist):
        i = self.pos[v]
        self.array[i][1] = dist
        
        while i > 0 and self.array[i][1] < self.array[(i-1)//2][1]:
            j = int((i-1)//2)
            self.pos[self.array[i][0]] = j
            self.pos[self.array[j][0]] = i
            self.swap(i, j)
            i = j
    
    #Operation to add new node in a heap
    def addToHeap(self, x, temp):
        self.array.append(self.addNode(x, temp))
        self.size += 1
        for x in range(self.size, -1, -1):
            self.heapify(x)
    
    #Operation to check whether a node is present in the heap
    def isPresent(self, v):
        if int(self.pos[v]) < int(self.size):
            return True
        return False
    
    # Operation to extract minimum node from minHeap
    def extractMin(self):
        if self.size == 0:
            return
        root = self.array[0]
        lastNode = self.array[self.size - 1]  # Replace root node with last node
        self.array[0] = lastNode
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
        self.size -= 1
        self.heapify(0)
        return root
