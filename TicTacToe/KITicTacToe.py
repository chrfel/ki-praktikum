from copy import deepcopy
import random
from queue import PriorityQueue
from abc import ABC, abstractmethod
from typing import List, Dict
from numpy import argmax

class Board():
    @staticmethod
    def show_board(board: Dict[str,str]) -> None:
        print(f"{board.get('0')} | {board.get('1')} | {board.get('2')}")
        print(f"- + - + -")
        print(f"{board.get('3')} | {board.get('4')} | {board.get('5')}")
        print(f"- + - + -")
        print(f"{board.get('6')} | {board.get('7')} | {board.get('8')}")

    @staticmethod
    def is_field_free(move: str, board: Dict[str,str]) -> bool:
        return board.get(move) == " "

    @staticmethod
    def get_free_fields(board: Dict[str,str]) -> List[str]:
        free = []
        for i in range(9):
            if board.get(str(i)) == " ":
                free.append(str(i))
        return free

    @staticmethod
    def is_board_full(board: Dict[str,str]) -> bool:
        return " " not in board.values()

    @staticmethod
    def is_tie(board: Dict[str,str]) -> bool:
        if Board.is_board_full(board) and Board.no_winner(board):
            return True
        return False

    @staticmethod
    def no_winner(board: Dict[str,str]) -> bool:
        if not Board.is_winner("X", board) and not Board.is_winner("O", board):
            return True
        return False
    
    @staticmethod
    def is_winner(player_symbol: str, board: Dict[str,str]) -> bool:
        # Horizontal
        for n in range(3):
            for x in range(3):
                if not board.get(str((n*3)+x)) == player_symbol:
                    break
                if x == 2:
                    return True
        # Vertikal
        for n in range(3):
            for x in range(3):
                if not board.get(str(n+(x*3))) == player_symbol:
                    break
                if x == 2:
                    return True
        # Diagonal
        if board.get(str(0)) == player_symbol and board.get(str(4)) == player_symbol and board.get(str(8)) == player_symbol:
            return True
        if board.get(str(2)) == player_symbol and board.get(str(4)) == player_symbol and board.get(str(6)) == player_symbol:
            return True
        return False

class Player(ABC):
    @abstractmethod
    def get_move(self, board: dict):
        pass

class HumanPlayer(Player):
    def get_move(self, board: dict):
        return input()

class RandomPlayer(Player):
    def get_move(self, board: dict):
        return random.choice(["0","1", "2","3","4","5","6","7","8",])

class PriorityEntry(object):
    def __init__(self, priority: int, data: Dict[str,str]):
        self.data = data
        self._priority = priority

    @property
    def priority(self):
        return self._priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, __o: object) -> bool:
        return self.data == __o.data

    def __hash__(self) -> int:
        return hash(self.priority)
class UniformCostSearchPlayer():

    def get_path_cost(self, board: Dict[str,str]):
        if Board.no_winner(board):
            return 1
        return 10

    def get_move(self, board: Dict[str,str]):
        return self.calculate_end_note(board)

    def calculate_end_note(self, board: Dict[str,str]):
        node = PriorityEntry(0, board)
        frontier = PriorityQueue()
        frontier.put(node)
        explored = set()

        while True:
            if frontier.empty():
                print("Frontier is empty - Failure!")
                exit(666)
            node = frontier.get()
            if Board.is_tie(node.data):
                return node.data
            explored.add(node)

            if len(Board.get_free_fields(node.data)) % 2 == 1:
                playerChar = "X"
            else:
                playerChar = "O"
            for i in Board.get_free_fields(node.data):
                child_board = deepcopy(node.data)
                child_board[i] = playerChar
                child_path_cost = node.priority + self.get_path_cost(child_board)
                child = PriorityEntry(child_path_cost, child_board)
                if child not in explored or child not in frontier.queue:
                    frontier.put(child)
                elif child in frontier.queue:
                    for i in frontier.queue:
                        if frontier.queue[i].data == child_board and frontier.queue[i].priority > child_path_cost:
                            frontier.queue[i].priority = child_path_cost



class MinMaxPlayer(Player):

    def get_move(self, board: dict):
        if len(Board.get_free_fields(board)) % 2 == 1:
            playerChar = "X"
        else:
            playerChar = "O"
        action_res = []
        for i in range(9):
            if (Board.is_field_free(str(i), board)):
                board[str(i)] = playerChar
                action_res.append(self.min(playerChar ,board))
                board[str(i)] = " "
        print(action_res)
        return Board.get_free_fields(board)[argmax(action_res)]

    def utility(self, playerChar: str, board: Dict[str,str]):
        if Board.is_winner(playerChar, board):
            return 1
        if Board.is_tie(board):
            return 0
        else:
            return -1

    def min(self, orginalPlayer: str , board: Dict[str,str]):
        if Board.is_tie(board) or Board.is_winner("X", board) or Board.is_winner("O", board):
            return self.utility(orginalPlayer, board)
        _v = 2
        for i in range(9):
            if (Board.is_field_free(str(i), board)):
                if len(Board.get_free_fields(board)) % 2 == 1:
                    board[str(i)] = "X"
                else:
                    board[str(i)] = "O"
                _v = min(_v, self.max(orginalPlayer, board))
                board[str(i)] = " "
        return _v
    
    def max(self, orginalPlayer: str, board: Dict[str,str]):
        if Board.is_tie(board) or Board.is_winner("X", board) or Board.is_winner("O", board):
            return self.utility(orginalPlayer, board)
        _v = -2
        for i in range(9):
            if (Board.is_field_free(str(i), board)):
                if len(Board.get_free_fields(board)) % 2 == 1:
                    board[str(i)] = "X"
                else:
                    board[str(i)] = "O"
                _v = max(_v, self.min(orginalPlayer, board))
                board[str(i)] = " "
        return _v


class TicTacToeKI():
    playerA: Player
    playerB: Player
    board = {
            "0": " ","1": " ","2": " ",
            "3": " ","4": " ","5": " ",
            "6": " ","7": " ","8": " "
    }

    def get_move_playerA(self):
        zug = "9"
        while not Board.is_field_free(zug, self.board):
            print("(X) Bitte Zug auswaehlen: ")
            zug = self.playerA.get_move(self.board)
        print(f"Gewaehlt: {zug}")
        self.board.update({f"{zug}": "X"})


    def get_move_playerB(self):
        zug = "9"
        while not Board.is_field_free(zug, self.board):
            print("(O) Bitte Zug auswaehlen: ")
            zug = self.playerB.get_move(self.board)
        print(f"Gewaehlt: {zug}")
        self.board.update({f"{zug}": "O"})

    def start(self):
        # Spielerauswahl
        print("h Human, r Random, m MinMax")
        print("Uniform Cost Simulation? y/n ")
        if input() == 'y':
            unPlayer = UniformCostSearchPlayer()
            self.board = unPlayer.get_move(self.board)
            Board.show_board(self.board)
            return 0
        print("Waehle Spieler X: ")
        in1 = input()
        if in1 == 'h':
            self.playerA = HumanPlayer()
        elif in1 == 'r':
            self.playerA = RandomPlayer()
        elif in1 == 'm':
            self.playerA = MinMaxPlayer()
        print("Waehle Spieler O: ")
        in2 = input()
        if in2 == 'h':
            self.playerB = HumanPlayer()
        elif in2 == 'r':
            self.playerB = RandomPlayer()
        elif in2 == 'm':
            self.playerB = MinMaxPlayer()
        # Game
        for x in range(9):
            Board.show_board(self.board)
            if x % 2 == 0:
                self.get_move_playerA()
                if Board.is_winner("X", self.board):
                    Board.show_board(self.board)
                    print("Spieler A hat gewonnen!")
                    return 1
            else:
                self.get_move_playerB()
                if Board.is_winner("O", self.board):
                    Board.show_board(self.board)
                    print("Spieler B hat gewonnen!")
                    return 2
            if Board.is_board_full(self.board):
                Board.show_board(self.board)
                print("Es gibt keinen Sieger! Schade Schade")
                return 0

if __name__ == "__main__": 
    tic = TicTacToeKI()
    tic.start()