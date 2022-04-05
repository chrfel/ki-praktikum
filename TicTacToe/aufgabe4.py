from random import randrange
from aufgabe3 import TicTacToe

class TicTacToeKI(TicTacToe):
    def get_move_playerB(self):
        zahl = randrange(9)
        print(f"Spieler B zieht automatisch: {zahl}")
        if self.is_field_free(str(zahl)):
            self.board.update({f"{zahl}": "O"})
        else:
            self.get_move_playerB()

if __name__ == "__main__": 
    tic = TicTacToeKI()
    tic.start()