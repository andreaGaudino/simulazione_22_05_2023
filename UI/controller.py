import warnings

import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self, e):
        self.anno = self._view.txtAnno.value
        self.salario = self._view.txtSalario.value

        if self.anno=="":
            self._view.create_alert("Anno non inserito")
            self._view.update_page()
            return
        if self.salario=="":
            self._view.create_alert("Anno non inserito")
            self._view.update_page()
            return

        try:
            intAnno = int(self.anno)
        except ValueError:
            self._view.create_alert("Anno inserito non numerico")
            self._view.update_page()
            return

        try:
            intSalario = (int(self.salario))*10**6
        except ValueError:
            self._view.create_alert("Salario inserito non numerico")
            self._view.update_page()
            return

        self._model.buildGraph(intAnno, intSalario)
        n,e = self._model.graphDetails()
        self._view.txtResult1.clean()
        self._view.txtResult1.controls.append(ft.Text(f"Grafo creato con {n} nodi e {e} archi"))
        self._view.update_page()


    def handleCalcolaConnesse(self, e):
        num = self._model.calcolaConnesse()
        self._view.txtResult2.controls.append(ft.Text(f"Numero componenti connesse: {num}"))
        self._view.update_page()

    def handleGradoMassimo(self, e):
        elem = self._model.cercaGradoMassimo()
        self._view.txtResult2.controls.append(ft.Text(f"Nodo di grado max: {elem[0]} con grado: {elem[1]}"))
        self._view.update_page()
    def handleDreamTeam(self, e):
        pass