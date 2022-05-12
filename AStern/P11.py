from concurrent.futures import ProcessPoolExecutor
import json
from pprint import pprint
from queue import PriorityQueue, Queue
import queue
from tracemalloc import start
from webbrowser import Konqueror


from numpy import number


class Knoten():
    name: str
    nachbarn = []
    kosten: number

    def __init__(self, name: str, kosten: number):
        self.name = name
        self.kosten = kosten
        self.nachbarn = []

    def add(self, nachbar):
        self.nachbarn.append(nachbar)

class AStern():

    def sucheKnoten(self, alleKnoten, zuSuchen: str):
        for i in alleKnoten:
            if i.name == zuSuchen:
                return i
        return None

    def calculateHeuristik(self, aktuellerKnoten, zielKnoten, alleKnoten):
        guenstigste = float("inf")
        for i in alleKnoten:
            for k in i.nachbarn:
                guenstigste = min(guenstigste, k.kosten)
        knoten = Queue()
        for i in aktuellerKnoten.nachbarn:
            knoten.put((i, 0))
        while True:
            if knoten.empty():
                return None
            i = knoten.get()
            if i[0].name == zielKnoten.name:
                return i[1]*guenstigste
            for k in alleKnoten:
                if k.name == i[0].name:
                    for p in k.nachbarn:
                        knoten.put((p, i[1]+1))

    def readJson(self):
        knoten = []
        with open("AStern/pfade.json") as file:
            data = json.load(file)
            for i in data["knoten"]:
                k = Knoten(i["name"], 0)
                for j in i["nachbarn"]:
                    nachbar = Knoten(j["name"], j["kosten"])
                    k.add(nachbar)
                knoten.append(k)
        return knoten

    def aStern(self, alleKnoten, startKnoten, zielKnoten):
        # Zu besuchen
        open = set([startKnoten])
        # Schon besucht
        closed = set([])

        # Aktuelle Distanz vom Start zu all anderen Knoten
        poo = {}
        poo[startKnoten] = 0

        # Von welchem Knoten komme ich?
        par = {}
        par[startKnoten] = startKnoten

        while len(open) > 0:
            n = None
            # Geringsten Wert in der Liste finden
            for v in open:
                if n == None or poo[v] + self.calculateHeuristik(v, zielKnoten, alleKnoten) < poo[n] + self.calculateHeuristik(n, zielKnoten, alleKnoten):
                    n = v
            
            if n == None:
                return None
            # Am Zielknoten angekommen
            if n == zielKnoten:
                path = []
                while par[n] != n:
                    path.append(n.name)
                    n = par[n]
                path.append(startKnoten.name)
                path.reverse()
                return path
            # Für alle Nachbarn des aktuellen Knotens
            for i in n.nachbarn:
                knoten = self.sucheKnoten(alleKnoten, i.name)
                # Wenn er noch nicht besucht wurde oder schon in der "zu besuchen" Liste steht
                if knoten not in open and knoten not in closed:
                    open.add(knoten)
                    par[knoten] = n
                    poo[knoten] = poo[n] + i.kosten
                # Schauen, ob die Kosten vom vorherigen Besuch höher sind
                else:
                    if poo[knoten] > poo[n] + i.kosten:
                        poo[knoten] = poo[n] + i.kosten
                        par[knoten] = n
                        # Nochmal besuchen
                        if knoten in closed:
                            closed.remove(knoten)
                            open.add(knoten)
            open.remove(n)
            closed.add(n)

if __name__ == "__main__":
    var = AStern()
    knoten = var.readJson()
    for i in knoten:
        pprint(i.name)
        for k in i.nachbarn:
            pprint(f"--> Nachbar: {k.name} {k.kosten}")
    print(var.aStern(knoten, knoten[0], knoten[5]))
    
