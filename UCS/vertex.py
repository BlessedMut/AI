class Vertex:

    def __init__(self,key):

        self.id = key

        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):

        self.connectedTo[nbr] = weight

    def __str__(self):

        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):

        return self.connectedTo.keys()

    def getId(self):

        return self.id

    def getWeight(self,nbr):

        return self.connectedTo[nbr]

S = Vertex('S')
S.addNeighbor('A',1)
S.addNeighbor('B',4)

A = Vertex('A')
A.addNeighbor('C',3)
A.addNeighbor('D',2)

B = Vertex('B')
B.addNeighbor('G',5)

C = Vertex('C')
C.addNeighbor('E',5)

E = Vertex('E')
E.addNeighbor('G',5)





