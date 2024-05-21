from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.areoporti = DAO.getAllAirports()
        self.idMap = {}
        for areoporto in self.areoporti:
            self.idMap[areoporto.id] = areoporto
        self.grafo = nx.DiGraph()
    def buildGraph(self,distanza):
        listaArchi = DAO.getEdge(distanza)
        for volo in listaArchi:
            self.grafo.add_node(self.idMap[volo.airportP])
            self.grafo.add_edge(self.idMap[volo.airportP],self.idMap[volo.airportA],percorso = volo)
        print(len(self.grafo.nodes))

