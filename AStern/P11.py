import json
from pprint import pprint
from queue import Queue
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
        # Guenstigsten Pfad raussuchen
        for i in alleKnoten:
            for k in i.nachbarn:
                guenstigste = min(guenstigste, k.kosten)
        knoten = Queue()
        # Nachbarn des aktuellen Knotens
        for i in aktuellerKnoten.nachbarn:
            knoten.put((i, 0))
        # Wenn ein Nachbar nicht Zielknoten ist, dann seine Nachbarn zur Liste mit Weg+1 hinzufügen.
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
        with open("pfade.json") as file:
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
        distanz = {}
        distanz[startKnoten] = 0

        # Von welchem Knoten komme ich?
        vorgaengerKnoten = {}
        vorgaengerKnoten[startKnoten] = startKnoten

        while len(open) > 0:
            n = None
            # Geringsten Wert in der Liste finden
            for v in open:
                if n == None or distanz[v] + self.calculateHeuristik(v, zielKnoten, alleKnoten) < distanz[n] + self.calculateHeuristik(n, zielKnoten, alleKnoten):
                    n = v
            
            if n == None:
                return None
            # Am Zielknoten angekommen
            if n == zielKnoten:
                path = []
                while vorgaengerKnoten[n] != n:
                    path.append(n.name)
                    n = vorgaengerKnoten[n]
                path.append(startKnoten.name)
                path.reverse()
                return path
            # Für alle Nachbarn des aktuellen Knotens
            for i in n.nachbarn:
                knoten = self.sucheKnoten(alleKnoten, i.name)
                # Wenn er noch nicht besucht wurde oder schon in der "zu besuchen" Liste steht
                if knoten not in open and knoten not in closed:
                    open.add(knoten)
                    vorgaengerKnoten[knoten] = n
                    distanz[knoten] = distanz[n] + i.kosten
                # Schauen, ob die Kosten vom vorherigen Besuch höher sind
                else:
                    if distanz[knoten] > distanz[n] + i.kosten:
                        distanz[knoten] = distanz[n] + i.kosten
                        vorgaengerKnoten[knoten] = n
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
    print("Start eingeben: ")
    startString = input()
    print("Ziel eingeben: ")
    zielString = input()
    print(var.aStern(knoten, var.sucheKnoten(knoten, startString), var.sucheKnoten(knoten, zielString)))
    
