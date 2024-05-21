import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        self._view._txt_result.clean()
        self._model.buildGraph(int(self._view._txtIn.value))
        self._view._txt_result.controls.append(ft.Text(f'Il grafo ha {len(self._model.grafo.nodes)} nodi'))
        for arco in self._model.grafo.edges:
            peso = self._model.grafo[arco[0]][arco[1]]['percorso']
            stampa = f'Partenza: {self._model.idMap[peso.airportP]} - Arrivo: {self._model.idMap[peso.airportA]}, Distanza: {peso.distanza}'
            self._view._txt_result.controls.append(ft.Text(stampa))
        self._view.update_page()