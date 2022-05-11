from concurrent.futures import ProcessPoolExecutor
import json
from pprint import pprint

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

    def calculateHeuristik(self, aktuellerKnoten, zielKnoten, alleKnoten): 
        pass

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

    # def calculate_end_note(self, board: Dict[str, str]):
    #     node = PriorityEntry(0, board)
    #     frontier = PriorityQueue()
    #     frontier.put(node)
    #     explored = set()
    #
    #     while True:
    #         if frontier.empty():
    #             print("Frontier is empty - Failure!")
    #             exit(666)
    #         node = frontier.get()
    #         if Board.is_tie(node.data):
    #             return node.data
    #         explored.add(node)
    #
    #         playerChar = Board.get_player_char(node.data)
    #         for i in Board.get_free_fields(node.data):
    #             child_board = deepcopy(node.data)
    #             child_board[i] = playerChar
    #             child_path_cost = node.priority + self.get_path_cost(child_board)
    #             child = PriorityEntry(child_path_cost, child_board)
    #             if child not in explored or child not in frontier.queue:
    #                 print(child_path_cost)
    #                 frontier.put(child)
    #             elif child in frontier.queue:
    #                 for i in frontier.queue:
    #                     if frontier.queue[i].data == child_board and frontier.queue[i].priority > child_path_cost:
    #                         frontier.queue[i].priority = child_path_cost

if __name__ == "__main__":
    var = AStern()
    knoten = var.readJson()
    for i in knoten:
        pprint(i.name)
        for k in i.nachbarn:
            pprint(f"Nachbar: {k.name}")
    #unPlayer = UniformCostSearchWithAStern()
    #self.board = unPlayer.calculate_end_note(self.board)