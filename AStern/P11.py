import json
from pprint import pprint

class Knoten():
    name: str
    nachbarn = []

    def __init__(self, name: str):
        self.name = name

    def add(self, nachbar: Knoten):
        self.nachbarn.append(nachbar)


class UniformCostSearchWithAStern():

    # def get_path_cost(self, board: Dict[str, str]):
    #     if Board.no_winner(board):
    #         return 1
    #     return 10

    def readJson(self):
        with open("pfade.json") as file:
            #pfade_dict = json.loads(file.read())
            data = json.load(file)
            for i in data["knoten"]:

                for j in i["nachbarn"]:
                    pprint(j)
            #pprint(pfade_dict)
            #for k, v in pfade_dict.items():
               # pprint(f"{k}- {v}")

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
    var = UniformCostSearchWithAStern()
    var.readJson()
    #unPlayer = UniformCostSearchWithAStern()
    #self.board = unPlayer.calculate_end_note(self.board)