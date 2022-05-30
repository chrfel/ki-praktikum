import time
from typing import List, Dict

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
    def get_player_char(board: Dict[str,str]) -> str:
        if len(Board.get_free_fields(board)) % 2 == 1:
            return"X"
        return "O"

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