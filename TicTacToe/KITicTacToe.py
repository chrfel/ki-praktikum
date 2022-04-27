import random
from abc import ABC, abstractmethod

class Board():
    board = {
            "0": " ","1": " ","2": " ",
            "3": " ","4": " ","5": " ",
            "6": " ","7": " ","8": " "
    }

    def show_board(self):
        print(f"{self.board.get('0')} | {self.board.get('1')} | {self.board.get('2')}")
        print(f"- + - + -")
        print(f"{self.board.get('3')} | {self.board.get('4')} | {self.board.get('5')}")
        print(f"- + - + -")
        print(f"{self.board.get('6')} | {self.board.get('7')} | {self.board.get('8')}")

    def is_field_free(self, move):
        return self.board.get(move) == " "

    def is_board_full(self):
        return ' ' not in self.board.values()

    def is_tie(self):
        if not self.is_winner("X") and not self.is_winner("O"):
            return True
        return False

    def is_winner(self, player_symbol):
        # Horizontal
        for n in range(3):
            for x in range(3):
                if not self.board.get(str((n*3)+x)) == player_symbol:
                    break
                if x == 2:
                    return True
        # Vertikal
        for n in range(3):
            for x in range(3):
                if not self.board.get(str(n+(x*3))) == player_symbol:
                    break
                if x == 2:
                    return True
        # Diagonal
        if self.board.get(str(0)) == player_symbol and self.board.get(str(4)) == player_symbol and self.board.get(str(8)) == player_symbol:
            return True
        if self.board.get(str(2)) == player_symbol and self.board.get(str(4)) == player_symbol and self.board.get(str(6)) == player_symbol:
            return True
        return False

class Player(ABC):
    @abstractmethod
    def get_move(self, board):
        pass

class HumanPlayer(Player):
    def get_move(self, board):
        return input()

class RandomPlayer(Player):
    def get_move(self, board):
        return random.choice(["0","1", "2","3","4","5","6","7","8",])

class UniformCostSearchPlayer(Player):
    def get_path_cost(self, board):
        pass

    def get_move(self, board):
        node = {board.board : 0}
        frontier = [node]
        explored = []
        pass

class MinMaxPlayer(Player):
    def get_move(self, board):
        pass

        

class TicTacToeKI():
    playerA: Player
    playerB: Player
    board: Board

    def __init__(self) -> None:
        self.board = Board()

    def get_move_playerA(self):
        zug = "9"
        while not self.board.is_field_free(zug):
            print("(X) Bitte Zug auswaehlen: ")
            zug = self.playerA.get_move(self.board)
        print(f"Gewaehlt: {zug}")
        self.board.board.update({f"{zug}": "X"})


    def get_move_playerB(self):
        zug = "9"
        while not self.board.is_field_free(zug):
            print("(O) Bitte Zug auswaehlen: ")
            zug = self.playerB.get_move(self.board)
        print(f"Gewaehlt: {zug}")
        self.board.board.update({f"{zug}": "O"})

    def start(self):
        # Spielerauswahl
        print("h Human, r Random, u Uniform, m MinMax")
        print("Waehle Spieler X: ")
        in1 = input()
        if in1 == 'h':
            self.playerA = HumanPlayer()
        elif in1 == 'r':
            self.playerA = RandomPlayer()
        elif in1 == 'u':
            self.playerA = UniformCostSearchPlayer()
        elif in1 == 'm':
            self.playerA = MinMaxPlayer()
        print("Waehle Spieler O: ")
        in2 = input()
        if in2 == 'h':
            self.playerB = HumanPlayer()
        elif in2 == 'r':
            self.playerB = RandomPlayer()
        elif in2 == 'u':
            self.playerB = UniformCostSearchPlayer()
        elif in2 == 'm':
            self.playerB = MinMaxPlayer()
        # Game
        for x in range(9):
            self.board.show_board()
            if x % 2 == 0:
                self.get_move_playerA()
                if self.board.is_winner("X"):
                    self.board.show_board()
                    print("Spieler A hat gewonnen!")
                    return 1
            else:
                self.get_move_playerB()
                if self.board.is_winner("O"):
                    self.board.show_board()
                    print("Spieler B hat gewonnen!")
                    return 2
            if self.board.is_board_full():
                self.board.show_board()
                print("Es gibt keinen Sieger! Schade Schade")
                return 0

if __name__ == "__main__": 
    tic = TicTacToeKI()
    tic.start()