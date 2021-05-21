import random
import copy


class GameOf2048:
    possible_moves = ["left", "right", "up", "down"]

    @staticmethod
    def create_random_board(size):
        # I should have used add_random_tile here instead
        random_tile_i = random.randrange(size)
        random_tile_j = random.randrange(size)
        return [[GameOf2048.get_random_number() if i == random_tile_i and j == random_tile_j else 0 for i in range(size)]
                for j in range(size)]

    @staticmethod
    def get_random_number():
        return 4 if random.randrange(10) == 0 else 2

    @staticmethod
    def reverse_board(board):
        for i, line in enumerate(board):
            board[i] = list(reversed(line))

    @staticmethod
    def rotate_board_clockwise(board):
        rotated_board = [list(line_as_tuple) for line_as_tuple in zip(*reversed(board))]
        for i in range(len(board)):
            board[i] = rotated_board[i]

    @staticmethod
    def rotate_board_anti_clockwise(board):
        rotated_board = [list(line_as_tuple) for line_as_tuple in reversed(list(zip(*board)))]
        for i in range(len(board)):
            board[i] = rotated_board[i]

    @staticmethod
    def combine_board_elements_to_left(board):
        for i, line in enumerate(board):
            board[i] = GameOf2048.combine_line_elements_to_left(line)

    @staticmethod
    def combine_board_elements_to_right(board):
        GameOf2048.reverse_board(board)
        GameOf2048.combine_board_elements_to_left(board)
        GameOf2048.reverse_board(board)

    @staticmethod
    def combine_board_elements_to_top(board):
        GameOf2048.rotate_board_anti_clockwise(board)
        GameOf2048.combine_board_elements_to_left(board)
        GameOf2048.rotate_board_clockwise(board)

    @staticmethod
    def combine_board_elements_to_bottom(board):
        GameOf2048.rotate_board_clockwise(board)
        GameOf2048.combine_board_elements_to_left(board)
        GameOf2048.rotate_board_anti_clockwise(board)

    @staticmethod
    def combine_line_elements_to_left(line):
        new_line = [element for element in line if element != 0]
        for i in range(len(new_line) - 1):
            if new_line[i] == 0:
                break
            if new_line[i] == new_line[i + 1]:
                new_line[i] *= 2
                new_line.pop(i + 1)
                new_line.append(0)
        new_line.extend([0 for i in range(len(line) - len(new_line))])
        return new_line

    def __init__(self, size):
        self.size = size
        self.board = GameOf2048.create_random_board(self.size)
        self.finished = False
        self.list_of_combined_boards = self.get_list_of_combined_boards()
        self.update_available_moves()

    def resolve_move(self, direction):
        if self.finished:
            raise Exception("Game finished.")
        elif direction not in GameOf2048.possible_moves:
            raise Exception("Incorrect input.")
        elif direction not in self.available_moves:
            raise Exception("Move not allowed.")
        else:
            self.board = self.list_of_combined_boards[GameOf2048.possible_moves.index(direction)]
            empty_tiles_position = self.get_empty_tiles_position()
            self.add_random_tile(empty_tiles_position)
            self.list_of_combined_boards = self.get_list_of_combined_boards()
            self.update_available_moves()
            self.finished = len(self.available_moves) == 0

    def update_available_moves(self):
        self.available_moves = [GameOf2048.possible_moves[i]
                                for i, board in enumerate(self.list_of_combined_boards) if board != self.board]

    def get_list_of_combined_boards(self):
        board_combined_left = copy.deepcopy(self.board)
        GameOf2048.combine_board_elements_to_left(board_combined_left)
        board_combined_right = copy.deepcopy(self.board)
        GameOf2048.combine_board_elements_to_right(board_combined_right)
        board_combined_top = copy.deepcopy(self.board)
        GameOf2048.combine_board_elements_to_top(board_combined_top)
        board_combined_bottom = copy.deepcopy(self.board)
        GameOf2048.combine_board_elements_to_bottom(board_combined_bottom)
        return [board_combined_left, board_combined_right, board_combined_top, board_combined_bottom]

    def get_empty_tiles_position(self):
        return [[i, j] for i, line in enumerate(self.board) for j, tile in enumerate(line) if tile == 0]

    def add_random_tile(self, empty_tiles_position):
        chosen_tile_position = random.choice(empty_tiles_position)
        self.board[chosen_tile_position[0]][chosen_tile_position[1]] = GameOf2048.get_random_number()

    def print_board(self):
        for line in self.board:
            pretty_line = ["  ·   " if tile == 0 else str(tile).center(6) for tile in line]
            print(*pretty_line, end="\n\n\n")
