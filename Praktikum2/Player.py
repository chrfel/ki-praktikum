from copy import deepcopy
from Board import Board
import random
from queue import PriorityQueue
from abc import ABC, abstractmethod
from typing import Dict
from numpy import argmax


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

class UniformCostSearch():

    def get_path_cost(self, board: Dict[str,str]):
        if Board.no_winner(board):
            return 1
        return 10

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
            
            playerChar = Board.get_player_char(node.data)
            for i in Board.get_free_fields(node.data):
                child_board = deepcopy(node.data)
                child_board[i] = playerChar
                child_path_cost = node.priority + self.get_path_cost(child_board)
                child = PriorityEntry(child_path_cost, child_board)
                if child not in explored or child not in frontier.queue:
                    print(child_path_cost)
                    frontier.put(child)
                elif child in frontier.queue:
                    for i in frontier.queue:
                        if frontier.queue[i].data == child_board and frontier.queue[i].priority > child_path_cost:
                            frontier.queue[i].priority = child_path_cost



class MinMaxPlayer(Player):

    def get_move(self, board: dict):
        playerChar = Board.get_player_char(board)
        action_res = []
        for i in Board.get_free_fields(board):
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
        for i in Board.get_free_fields(board):
            board[str(i)] = Board.get_player_char(board)
            _v = min(_v, self.max(orginalPlayer, board))
            board[str(i)] = " "
        return _v
    
    def max(self, orginalPlayer: str, board: Dict[str,str]):
        if Board.is_tie(board) or Board.is_winner("X", board) or Board.is_winner("O", board):
            return self.utility(orginalPlayer, board)
        _v = -2
        for i in Board.get_free_fields(board):
            board[str(i)] = Board.get_player_char(board)
            _v = max(_v, self.min(orginalPlayer, board))
            board[str(i)] = " "
        return _v