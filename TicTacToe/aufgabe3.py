from tracemalloc import start


class TicTacToe(object):

    def __init__(self) -> None:
        self.board = {
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

    def get_move_playerA(self):
        print("Zug Spieler A: ")
        zahl = input()
        if self.is_field_free(zahl):
            self.board.update({f"{zahl}": "X"})
        else:
            print("Falscher Zug!")
            self.get_move_playerA()

    def get_move_playerB(self):
        print("Zug Spieler B: ")
        zahl = input()
        if self.is_field_free(zahl):
            self.board.update({f"{zahl}": "O"})
        else:
            print("Falscher Zug!")
            self.get_move_playerB()

    def is_field_free(self, move):
        return self.board.get(move) == " "

    def is_board_full(self):
        return ' ' not in self.board.values()

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

    def start(self):    
        for x in range(9):
            self.show_board()
            if x % 2 == 0:
                self.get_move_playerA()
                if self.is_winner("X"):
                    print("Spieler A hat gewonnen!")
                    break
            else:
                self.get_move_playerB()
                if self.is_winner("O"):
                    print("Spieler B hat gewonnen!")
                    break
            if self.is_board_full():
                print("Es gibt keinen Sieger! Schade Schade")
                break
            
            
if __name__ == "__main__": 
    tic = TicTacToe()
    tic.start()