from Board import Board
from Player import *

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
            unPlayer = UniformCostSearch()
            self.board = unPlayer.calculate_end_note(self.board)
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
        elif in1 == 'mp':
            self.playerA = MinMaxPlayerWithPruning()
        print("Waehle Spieler O: ")
        in2 = input()
        if in2 == 'h':
            self.playerB = HumanPlayer()
        elif in2 == 'r':
            self.playerB = RandomPlayer()
        elif in2 == 'm':
            self.playerB = MinMaxPlayer()
        elif in2 == 'mp':
            self.playerA = MinMaxPlayerWithPruning()
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