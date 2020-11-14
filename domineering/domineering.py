from abc import ABCMeta, abstractmethod
from random import choice
from time import time

import sys


def invoke_error(other, message):
    print("Error in {} passiert.\nMessage: {}".format(other.__name__,
                                                      message))


def get_enemy(player):
    return "v" if player == "h" else "h"


class Game(metaclass=ABCMeta):
    def __init__(self, length=8):
        """
        Ereugt ein neues Spielfeld:
        :param length: Größe des Spielfelds
        :type length: int
        :return: None
        :rtype:
        """
        self.length = length
        self.spielfeld = []
        self.player_to_move = "v"
        self.player_to_move = "h"
        self.moves_h = set()
        self.moves_v = set()

    @abstractmethod
    def make_move(self, row, column, player):
        pass

    @abstractmethod
    def unmake_move(self, row, column, player):
        pass

    @abstractmethod
    def available_moves(self, player) -> set:
        pass

    def is_endstate(self, player) -> bool:
        if player == "v":
            for i in range(self.length - 1):
                for j in range(self.length):
                    if self.spielfeld[i][j] == "-" and \
                                    self.spielfeld[i + 1][j] == "-":
                        return False
            return True
        if player == "h":
            for i in range(self.length):
                for j in range(self.length - 1):
                    if self.spielfeld[i][j] == "-" and \
                                    self.spielfeld[i][j + 1] == "-":
                        return False
            return True

    @abstractmethod
    def update_moves(self, row, column, add, player):
        pass


class Domino(Game):
    def __init__(self, length=8, spielfeld=None, player_to_move=None):
        """
        Ereugt ein neues Spielfeld:
        - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        :param length: Größe des Spielfelds
        :type length: int
        :return: None
        :rtype:
        """
        self.length = length
        if not spielfeld:
            self.spielfeld = [["-" for i in range(length)] for i in
                              range(length)]
        else:
            self.spielfeld = spielfeld
        if not player_to_move:
            self.player_to_move = "v"
        else:
            self.player_to_move = player_to_move

        self.moves_v = set()
        self.moves_h = set()
        self.available_moves("v")
        self.available_moves("h")

    def __str__(self):
        s = []
        for i in range(self.length):
            for j in range(self.length):
                s.append(self.spielfeld[i][j] + ' ')
            s.append('\n')
        s.append('\n')
        return ''.join(s)

    def print_board(self):
        for i in range(self.length):
            for j in range(self.length):
                print(self.spielfeld[i][j], end=" ")
            print()
        print()

    def make_move(self, row: int, column: int, player: str) -> bool:
        try:
            if player == "v":
                if self.spielfeld[row][column] == "-" and \
                                self.spielfeld[row + 1][column] == "-":
                    self.spielfeld[row][column] = "v"
                    self.spielfeld[row + 1][column] = "v"
                    self.update_moves(row, column, add=True, player=player)
                else:
                    invoke_error(self.make_move,
                                 "{} oder {} schon besetzt"
                                 .format(row, row + 1))
                    exit()
                    return False
            elif player == "h":
                if self.spielfeld[row][column] == "-" and \
                                self.spielfeld[row][column + 1] == "-":
                    self.spielfeld[row][column] = "h"
                    self.spielfeld[row][column + 1] = "h"
                    self.update_moves(row, column, add=True, player=player)
                else:
                    invoke_error(self.make_move, "{} oder {} schon besetzt"
                                 .format(column, column + 1))
                    return False
            return True
        except IndexError:
            invoke_error(self.make_move, "ungültiger Zug")
            return False

    def unmake_move(self, row: int, column: int, player: str) -> bool:
        if player == "v":
            self.spielfeld[row][column] = "-"
            self.spielfeld[row + 1][column] = "-"
            self.update_moves(row, column, add=False, player=player)
        elif player == "h":
            self.spielfeld[row][column] = "-"
            self.spielfeld[row][column + 1] = "-"
            self.update_moves(row, column, add=False, player=player)
        return True

    def available_moves(self, player: str):
        if player == "v":
            for i in range(self.length - 1):
                for j in range(self.length):
                    if self.spielfeld[i][j] == "-" and \
                                    self.spielfeld[i + 1][j] == "-":
                        self.moves_v.add((i, j))
        if player == "h":
            for i in range(self.length):
                for j in range(self.length - 1):
                    if self.spielfeld[i][j] == "-" and \
                                    self.spielfeld[i][j + 1] == "-":
                        self.moves_h.add((i, j))

    def update_moves(self, row, column, add, player) -> None:
        # Stein wird in row, column, row2, column2 hinzugefügt
        if add:
            try:
                self.moves_v.remove((row - 1, column))
            except KeyError:
                pass
            try:
                self.moves_h.remove((row, column - 1))
            except KeyError:
                pass
            try:
                self.moves_v.remove((row, column))
            except KeyError:
                pass
            try:
                self.moves_h.remove((row, column))
            except KeyError:
                pass

            if player == "v":
                try:
                    self.moves_h.remove((row + 1, column - 1))
                except KeyError:
                    pass
                try:
                    self.moves_h.remove((row + 1, column))
                except KeyError:
                    pass
                try:
                    self.moves_v.remove((row + 1, column))
                except KeyError:
                    pass
            else:
                try:
                    self.moves_v.remove((row - 1, column + 1))
                except KeyError:
                    pass
                try:
                    self.moves_v.remove((row, column + 1))
                except KeyError:
                    pass
                try:
                    self.moves_h.remove((row, column + 1))
                except KeyError:
                    pass

        # Stein wird von row, column entfernt
        else:
            if row > 0:
                if self.spielfeld[row - 1][column] == "-":
                    self.moves_v.add((row - 1, column))
            try:
                if self.spielfeld[row + 1][column] == "-":
                    self.moves_v.add((row, column))
            except IndexError:
                pass
            if column > 0:
                if self.spielfeld[row][column - 1] == "-":
                    self.moves_h.add((row, column - 1))
            try:
                if self.spielfeld[row][column + 1] == "-":
                    self.moves_h.add((row, column))
            except IndexError:
                pass
            if player == "v":
                if column > 0:
                    if self.spielfeld[row + 1][column - 1] == "-":
                        self.moves_h.add((row + 1, column - 1))
                try:
                    if self.spielfeld[row + 1][column + 1] == "-":
                        self.moves_h.add((row + 1, column))
                except IndexError:
                    pass
                try:
                    if self.spielfeld[row + 2][column] == "-":
                        self.moves_v.add((row + 1, column))
                except IndexError:
                    pass

            else:
                if row > 0:
                    if self.spielfeld[row - 1][column + 1] == "-":
                        self.moves_v.add((row - 1, column + 1))
                try:
                    if self.spielfeld[row + 1][column + 1] == "-":
                        self.moves_v.add((row, column + 1))
                except IndexError:
                    pass
                try:
                    if self.spielfeld[row][column + 2] == "-":
                        self.moves_h.add((row, column + 1))
                except IndexError:
                    pass

    def is_endstate(self, player):
        if player == "v":
            if len(self.moves_v) == 0:
                return True
        else:
            if len(self.moves_h) == 0:
                return True
        return False

    def next_move(self):
        move = determine(self, self.player_to_move)
        return move


def alpha_beta_search(game: Game, player: str, *args, **kwargs):
    max_depth = kwargs.get("max_depth") if kwargs.get("max_depth") else 5

    def max_value(player, alpha, beta, depth):
        if depth == max_depth or game.is_endstate(player):
            return eval_func(game, player)

        v = float("-inf")
        available_moves = game.moves_h.copy() if player == "h" \
            else game.moves_v.copy()
        for move in available_moves:
            game.make_move(move[0], move[1], player)
            v = max(v, min_value(get_enemy(player), alpha, beta, depth + 1))
            game.unmake_move(move[0], move[1], player)
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(player, alpha, beta, depth):
        if depth == max_depth or game.is_endstate(player):
            return eval_func(game, player)

        v = float("inf")
        available_moves = game.moves_h.copy() if player == "h" \
            else game.moves_v.copy()
        for move in available_moves:
            game.make_move(move[0], move[1], player)
            v = min(v, max_value(get_enemy(player), alpha, beta, depth + 1))
            game.unmake_move(move[0], move[1], player)
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    return min_value(player, float("-infinity"), float("infinity"), 0)


def determine(game: Game, player):
    choices = new_choices = []
    sortedMoves = {}  # collections.OrderedDict()
    i = 2
    t = Timer(1)
    t.start()
    while t.is_running():
        a = float("-infinity")
        # print("i:", i)
        if len(sortedMoves) == 0:
            available_moves = game.moves_h.copy() if player == "h" \
                else game.moves_v.copy()
        else:
            available_moves = sorted(sortedMoves, key=sortedMoves.get,
                                     reverse=True)
        for move in available_moves:
            game.make_move(move[0], move[1], player)
            val = alpha_beta_search(game, get_enemy(player), max_depth=i)
            game.unmake_move(move[0], move[1], player)
            if val == 100:
                print(100, file=sys.stderr)
                return move
            if val > a:
                a = val
                new_choices = [move]
            elif val == a:
                new_choices.append(move)
            sortedMoves[move] = val
            if not t.is_running():
                return choice(choices)
        choices = new_choices
        new_choices = []
        i += 1
        if a == -100:
            print(-100, file=sys.stderr)
            return choice(choices)
    # print(a)
    return choice(choices)


def eval_func(game: Game, player):
    if game.is_endstate(player):
        if player == game.player_to_move:
            return -100
        else:
            return 100
    else:
        if game.is_endstate(get_enemy(player)):
            if player == game.player_to_move:
                return 100
            else:
                return -100
        to_move = game.player_to_move
        enemy = get_enemy(to_move)
        player_1 = game.moves_h if to_move == "h" else game.moves_v
        player_2 = game.moves_h if enemy == "h" else game.moves_v
        verhaeltnis = len(player_1) / len(player_2)
        return verhaeltnis


class Timer:
    def __init__(self, duration=5):
        self.t1 = 0
        self.duration = duration

    def start(self):
        self.t1 = time()

    def is_running(self):
        if time() - self.t1 < self.duration:
            return True
        else:
            return False


def game_master():
    d = Domino(6)
    d.player_to_move = "v"
    while not d.is_endstate(d.player_to_move):
        move = determine(d, d.player_to_move)
        d.make_move(move[0], move[1], d.player_to_move)
        print(d)
        d.player_to_move = get_enemy(d.player_to_move)
    print("--------------------")
    print(d)
    print("Sieger ist: {}".format(get_enemy(d.player_to_move)))
