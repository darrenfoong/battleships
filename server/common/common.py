from enum import Enum
import numpy as np
import time
import uuid


class Cell(Enum):
    EMPTY = 0
    HIT = -1


class Direction(Enum):
    UPDOWN = 0
    LEFTRIGHT = 1


class Game:
    def __init__(self, width, height, current_player):
        self.created = time.time()
        self.current_player = current_player
        self.boards = dict()
        self.ships = dict()
        self.weapons = dict()

        self.boards[0] = Board(width, height)
        self.boards[1] = Board(width, height)

        self.ships[0] = dict()
        self.ships[1] = dict()

        self.weapons[0] = dict()
        self.weapons[1] = dict()

    def perform_action(self, player, x, y, weapon):
        return


class GameDto:
    def __init__(self, dynamo_item):
        self.id = dynamo_item["id"]["S"]
        self.value = dynamo_item["value"]["S"]

    def to_json(self):
        return {"id": self.id, "value": self.value}


class Board:
    def __init__(self, width, height):
        self.state = np.full((height, width), Cell.EMPTY)

    def hit(self, x, y):
        previous_value = self.state[y][x]
        self.state[y][x] = Cell.HIT
        return previous_value

    def place_ship(self, x, y, length, direction, ship_number):
        if direction == Direction.UPDOWN:
            for i in range(y, y + length):
                self.state[i][x] = ship_number

        if direction == Direction.LEFTRIGHT:
            for i in range(x, x + length):
                self.state[y][i] = ship_number
