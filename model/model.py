import copy
import random
from math import sqrt
#from geopy.distance import geodesic

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.idMap = {}

    def buildGraph(self, anno, salario):
        players = DAO.getGiocatori(anno, salario)
        self.graph.clear()
        for i in players:
            self.graph.add_node(i)
            self.idMap[i.id] = i
        archi = DAO.getArchi(anno, salario)
        for a in archi:
            self.graph.add_edge(self.idMap[a[0]], self.idMap[a[1]])

    def calcolaConnesse(self):
        return len(list(nx.connected_components(self.graph)))

    def cercaGradoMassimo(self):
        lista = []
        for i in list(self.graph.nodes):
            lista.append((i, len(list(self.graph.neighbors(i)))))
        lista.sort(key=lambda x: x[1], reverse=True)
        return lista[0]

    def graphDetails(self):
        return len(self.graph.nodes), len(self.graph.edges)