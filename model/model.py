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


    def calcolaDreamTeam(self, anno, salario):
        self.solBest = []
        self.salarioMax = 0

        for n in list(self.graph.nodes):
            parziale = []
            if len(list(self.graph.neighbors(n)))>0:
                parziale.append(n)
                squadre = self.trovaSquadre(n.id, anno)
                self.ricorsione(parziale, n, anno, salario, squadre)
        print(self.solBest)
        return self.solBest, self.salarioMax
    def ricorsione(self, parziale, nodo, anno, salario, squadrePresenti):
        nodi = list(self.graph.nodes)
        nodiAmmissibili = self.getAmmissibili(nodi, squadrePresenti, anno, parziale)
        if len(nodiAmmissibili) == 0:
            if len(parziale) == 1:
                return
            totSalari = self.getTotSalari(parziale)
            if totSalari>self.salarioMax:
                print(parziale)
                self.salarioMax = totSalari
                self.solBest = copy.deepcopy(parziale)
        else:
            for v in nodiAmmissibili:
                parziale.append(v)
                squadre = self.trovaSquadre(v.id, anno)
                s = copy.deepcopy(squadrePresenti)
                for i in squadre:
                    s.append(i)
                self.ricorsione(parziale, v, anno, salario, s)
                parziale.pop()

    def trovaSquadre(self, nodo, anno):
        dizio = DAO.getSquadreGiocatore(nodo, anno)
        if len(dizio) == 0:
            return []
        return dizio[nodo]


    def getTotSalari(self, parziale):
        tot = 0
        for i in parziale:
            tot += i.salary
        return tot

    def getAmmissibili(self, vicini, squadrePresenti, anno, parziale):
        ammisibili = []
        s = copy.deepcopy(squadrePresenti)
        for v in vicini:
            if v not in parziale:
                boolean = False
                squadre = self.trovaSquadre(v.id, anno)
                for i in squadre:
                    if i in s:
                        boolean = True
                if not boolean:
                    ammisibili.append(v)
                    for i in squadre:
                        if i not in s:
                            s.append(i)
        return ammisibili

    def graphDetails(self):
        return len(self.graph.nodes), len(self.graph.edges)