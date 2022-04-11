from random import randrange
from aufgabe3 import TicTacToe

class TicTacToeKI(TicTacToe):
    playerAKI: bool
    playerBKI: bool


    def __init__(self, playerAKI, playerBKI) -> None:
        self.playerAKI = playerAKI
        self.playerBKI = playerBKI
        super().__init__()

    def get_move_playerA(self):
        if not self.playerAKI:
            super().get_move_playerA()
        else:
            zahl = randrange(9)
            if self.is_field_free(str(zahl)):
                print(f"Spieler A zieht automatisch: {zahl}")
                self.board.update({f"{zahl}": "X"})
            else:
                self.get_move_playerA()

    def get_move_playerB(self):
        if not self.playerBKI:
            super().get_move_playerB()
        else:
            zahl = randrange(9)
            if self.is_field_free(str(zahl)):
                print(f"Spieler B zieht automatisch: {zahl}")
                self.board.update({f"{zahl}": "O"})
            else:
                self.get_move_playerB()

if __name__ == "__main__": 
    tic = TicTacToeKI(True, True)
    a, b, c = 0,0,0
    for i in range(1000):
        print(i)
        num = tic.start()
        if num == 0:
            c +=1
        elif num == 1:
            a += 1
        else:
            b +=1
    print(a)
    print(b)
    print(c)
