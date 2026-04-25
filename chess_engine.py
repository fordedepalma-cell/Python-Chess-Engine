# Python Chess Engine v1.0.0
# Copyright Forde DePalma, 2026

class Piece:
    def __init__(self, piece, color, column, rank):
        self.piece = piece
        self.color = color
        self.column = column
        self.rank = int(rank)


class Engine:
    def __init__(self):
        self.starting_board = [
            [Piece("rook", "black", "a", "8"), Piece("knight", "black", "b", "8"), Piece("bishop", "black", "c", "8"),
             Piece("queen", "black", "d", "8"), Piece("king", "black", "e", "8"), Piece("bishop", "black", "f", "8"),
             Piece("knight", "black", "g", "8"), Piece("rook", "black", "h", "8")],
            [Piece("pawn", "black", "a", "7"), Piece("pawn", "black", "b", "7"), Piece("pawn", "black", "c", "7"),
             Piece("pawn", "black", "d", "7"), Piece("pawn", "black", "e", "7"), Piece("pawn", "black", "f", "7"),
             Piece("pawn", "black", "g", "7"), Piece("pawn", "black", "h", "7")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Piece("pawn", "white", "a", "2"), Piece("pawn", "white", "b", "2"), Piece("pawn", "white", "c", "2"),
             Piece("pawn", "white", "d", "2"), Piece("pawn", "white", "e", "2"), Piece("pawn", "white", "f", "2"),
             Piece("pawn", "white", "g", "2"), Piece("pawn", "white", "h", "2")],
            [Piece("rook", "white", "a", "1"), Piece("knight", "white", "b", "1"), Piece("bishop", "white", "c", "1"),
             Piece("queen", "white", "d", "1"), Piece("king", "white", "e", "1"), Piece("bishop", "white", "f", "1"),
             Piece("knight", "white", "g", "1"), Piece("rook", "white", "h", "1")],
        ]

        self.board = [
            [Piece("rook", "black", "a", "8"), Piece("knight", "black", "b", "8"), None,
             Piece("queen", "black", "d", "8"), Piece("king", "black", "e", "8"), Piece("bishop", "black", "f", "8"),
             Piece("knight", "black", "g", "8"), Piece("rook", "black", "h", "8")],
            [Piece("pawn", "black", "a", "7"), Piece("pawn", "black", "b", "7"), Piece("pawn", "black", "c", "7"),
             Piece("pawn", "black", "d", "7"), Piece("pawn", "black", "e", "7"), Piece("pawn", "black", "f", "7"),
             Piece("pawn", "black", "g", "7"), Piece("pawn", "black", "h", "7")],
            [None, None, Piece("pawn", "white", "c", "2"), None, None, None, None, None],
            [Piece("pawn", "white", "a", "2"), None, None, None, None, None, None, Piece("bishop", "black", "c", "8")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, Piece("pawn", "white", "b", "2"), None, Piece("pawn", "white", "d", "2"),
             Piece("pawn", "white", "e", "2"), Piece("pawn", "white", "f", "2"), Piece("pawn", "white", "g", "2"),
             Piece("pawn", "white", "h", "2")],
            [Piece("rook", "white", "a", "1"), Piece("knight", "white", "b", "1"), Piece("bishop", "white", "c", "1"),
             Piece("queen", "white", "d", "1"), Piece("king", "white", "e", "1"), Piece("bishop", "white", "f", "1"),
             Piece("knight", "white", "g", "1"), Piece("rook", "white", "h", "1")],
        ]

        self.horizontal_indices = {
            '1': 7, '2': 6, '3': 5, '4': 4,
            '5': 3, '6': 2, '7': 1, '8': 0,
        }

        self.vertical_indices = {
            'h': 7, 'g': 6, 'f': 5, 'e': 4,
            'd': 3, 'c': 2, 'b': 1, 'a': 0,
        }

        self.horizontal_squares = {v: k for k, v in self.horizontal_indices.items()}
        self.vertical_squares = {v: k for k, v in self.vertical_indices.items()}
        self.horizontal_squares_for_neg_indices = {-v: k for k, v in self.horizontal_indices.items()}
        self.vertical_squares_for_neg_indices = {-v: k for k, v in self.vertical_indices.items()}

    def square_playable_or_empty(self, hor_i, ver_i, current_piece):
        if hor_i < 0 or hor_i > 7 or ver_i < 0 or ver_i > 7:
            return False
        try:
            if self.board[hor_i][ver_i] is None:
                return True
            elif isinstance(self.board[hor_i][ver_i], Piece):
                return self.board[hor_i][ver_i].color != current_piece.color
            else:
                return False
        except IndexError:
            return False

    def square_capturable(self, hor_i, ver_i, current_piece):
        if hor_i < 0 or hor_i > 7 or ver_i < 0 or ver_i > 7:
            return False
        try:
            if isinstance(self.board[hor_i][ver_i], Piece):
                return self.board[hor_i][ver_i].color != current_piece.color
            return False
        except IndexError:
            return False

    def square_empty(self, hor_i, ver_i, piece):
        if hor_i < 0 or hor_i > 7 or ver_i < 0 or ver_i > 7:
            return False
        return self.board[hor_i][ver_i] is None

    def convert_indices_to_square(self, hor_i, ver_i):
        try:  # Bug 6 fix: use tuple syntax so both exception types are caught
            return f"{self.vertical_squares[ver_i]}{self.horizontal_squares[hor_i]}"
        except (IndexError, KeyError):
            return None

    def create_move(self, current_square_tuple: tuple, new_square_str: str):
        origin = self.convert_indices_to_square(*current_square_tuple)
        if origin is None or new_square_str is None:
            return None
        return f"{origin}-{new_square_str}"

    def check_and_add_move(self, function, curr_indices, move, piece):
        if function(*move, piece):
            return self.create_move(curr_indices, self.convert_indices_to_square(*move))
        else:
            return None

    @staticmethod
    def remove_all_none_type_vals(move_list):
        return list(set(move for move in move_list if move is not None))

    def get_playable_squares_for_pawn(self, pawn, horizontal_index, vertical_index, current_indices, legal_moves, up,
                                      up_2, starting_rank):

        _a = (horizontal_index + up, vertical_index)
        legal_moves.append(self.check_and_add_move(self.square_empty, current_indices, _a, pawn))

        if pawn.rank == starting_rank and self.board[horizontal_index + up][vertical_index] is None:
            _b = (horizontal_index + up_2, vertical_index)
            legal_moves.append(self.check_and_add_move(self.square_empty, current_indices, _b, pawn))

        _c = (horizontal_index + up, vertical_index - 1)
        legal_moves.append(self.check_and_add_move(self.square_capturable, current_indices, _c, pawn))

        _d = (horizontal_index + up, vertical_index + 1)
        legal_moves.append(self.check_and_add_move(self.square_capturable, current_indices, _d, pawn))

        return legal_moves

    def get_legal_moves_for_pawn(self, pawn, horizontal_index, vertical_index, current_indices, legal_moves):
        if pawn.color == "white":
            return self.remove_all_none_type_vals(
                self.get_playable_squares_for_pawn(pawn, horizontal_index, vertical_index, current_indices, legal_moves,
                                                   -1, -2, 2))
        if pawn.color == "black":
            return self.remove_all_none_type_vals(
                self.get_playable_squares_for_pawn(pawn, horizontal_index, vertical_index, current_indices, legal_moves,
                                                   1, 2, 7))
        return None

    def get_legal_moves_for_knight(self, knight, horizontal_index, vertical_index, current_indices, legal_moves):
        possible_moves = [
            (horizontal_index - 2, vertical_index - 1),
            (horizontal_index - 2, vertical_index + 1),
            (horizontal_index + 2, vertical_index - 1),
            (horizontal_index + 2, vertical_index + 1),
            (horizontal_index - 1, vertical_index - 2),
            (horizontal_index - 1, vertical_index + 2),
            (horizontal_index + 1, vertical_index - 2),
            (horizontal_index + 1, vertical_index + 2),
        ]

        for move in possible_moves:
            legal_moves.append(self.check_and_add_move(self.square_playable_or_empty, current_indices, move, knight))

        return self.remove_all_none_type_vals(legal_moves)

    def legal_moves_for_bishop(self, bishop, horizontal_index, vertical_index, current_indices, legal_moves):
        directions_for_bishop = [
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
        ]

        for direction in directions_for_bishop:
            hor_step, ver_step = direction
            hor_i = hor_step  # Bug 3 fix: start at first step, not (0, 0)
            ver_i = ver_step
            moves_available = True
            while moves_available:
                move = (horizontal_index + hor_i, vertical_index + ver_i)
                if self.square_playable_or_empty(*move, bishop):  # Bug 1 fix: check candidate move square, not origin
                    legal_moves.append(
                        self.check_and_add_move(self.square_playable_or_empty, current_indices, move, bishop))
                    if self.board[move[0]][move[1]] is not None:  # Bug 2 fix: stop sliding after a capture
                        moves_available = False
                else:
                    moves_available = False
                ver_i += ver_step
                hor_i += hor_step

        return self.remove_all_none_type_vals(legal_moves)

    def legal_moves_for_rook(self, rook, horizontal_index, vertical_index, current_indices, legal_moves):
        for hor_step in (-1, 1):
            hor_i = hor_step
            moves_available = True
            while moves_available:
                move = (horizontal_index + hor_i, vertical_index)
                if self.square_playable_or_empty(*move, rook):
                    legal_moves.append(
                        self.check_and_add_move(self.square_playable_or_empty, current_indices, move, rook))
                    if self.board[move[0]][
                        move[1]] is not None:  # Bug 4 fix: stop after capture, not after empty square
                        moves_available = False
                else:
                    moves_available = False
                hor_i += hor_step

        for ver_step in (-1, 1):
            ver_i = ver_step
            moves_available = True
            while moves_available:
                move = (horizontal_index, vertical_index + ver_i)
                if self.square_playable_or_empty(*move, rook):
                    legal_moves.append(
                        self.check_and_add_move(self.square_playable_or_empty, current_indices, move, rook))
                    if self.board[move[0]][
                        move[1]] is not None:  # Bug 4 fix: stop after capture, not after empty square
                        moves_available = False
                else:
                    moves_available = False
                ver_i += ver_step

        return self.remove_all_none_type_vals(legal_moves)

    def legal_moves_for_a_piece(self, piece):
        legal_moves = []
        horizontal_index = self.horizontal_indices[str(piece.rank)]
        vertical_index = self.vertical_indices[piece.column]
        current_indices = (horizontal_index, vertical_index)
        compressed_args = (horizontal_index, vertical_index, current_indices, legal_moves)  # For readability

        if piece.piece == "pawn":
            legal_moves = self.get_legal_moves_for_pawn(piece, *compressed_args)
        elif piece.piece == "knight":
            legal_moves = self.get_legal_moves_for_knight(piece, *compressed_args)
        elif piece.piece == "bishop":
            legal_moves = self.legal_moves_for_bishop(piece, *compressed_args)  # Bug 5 fix: was calling knight method
        elif piece.piece == "rook":
            legal_moves = self.legal_moves_for_rook(piece, *compressed_args)

        return legal_moves

    def get_legal_moves(self):
        pass

    def find_best_move(self):
        pass

    def move(self, move: str):
        pass

engine = Engine()
print(engine.legal_moves_for_a_piece(engine.board[3][-1]))