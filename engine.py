from piece import Piece

class Engine:
    def __init__(self):
        self.board = [
            [Piece("rook", "black", "a", "8"), Piece("knight", "black", "b", "8"), Piece("bishop", "black", "c", "8"), Piece("queen", "black", "d", "8"), Piece("king", "black", "e", "8"), Piece("bishop", "black", "f", "8"), Piece("knight", "black", "g", "8"), Piece("rook", "black", "h", "8")],
            [Piece("pawn", "black", "a", "7"), Piece("pawn", "black", "b", "7"), Piece("pawn", "black", "c", "7"), Piece("pawn", "black", "d", "7"), Piece("pawn", "black", "e", "7"), Piece("pawn", "black", "f", "7"), Piece("pawn", "black", "g", "7"), Piece("pawn", "black", "h", "7")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Piece("pawn", "white", "a", "2"), Piece("pawn", "white", "b", "2"), Piece("pawn", "white", "c", "2"), Piece("pawn", "white", "d", "2"), Piece("pawn", "white", "e", "2"), Piece("pawn", "white", "f", "2"), Piece("pawn", "white", "g", "2"), Piece("pawn", "white", "h", "2")],
            [Piece("rook", "white", "a", "1"), Piece("knight", "white", "b", "1"), Piece("bishop", "white", "c", "1"), Piece("queen", "white", "d", "1"), Piece("king", "white", "e", "1"), Piece("bishop", "white", "f", "1"), Piece("knight", "white", "g", "1"), Piece("rook", "white", "h", "1")],
        ]

        self.horizontal_indices = {
            '1': 7, '2': 6, '3': 5, '4': 4,
            '5': 3, '6': 2, '7': 1, '8': 0,
        }

        self.vertical_indices = {
            'h': 7, 'g': 6, 'f': 5, 'e': 4,
            'd': 3, 'c': 2, 'b': 1, 'a': 0,
        }

        '''
        When evaluating coordinates:
        -1 on horizontal and vertical indices translate to up and to the right,
        +1 on horizontal and vertical indices translate to down and to the left
        '''

        self.horizontal_squares = {v: k for k, v in self.horizontal_indices.items()}
        self.vertical_squares = {v: k for k, v in self.vertical_indices.items()}

    def square_empty(self, hor_i, ver_i):
        if hor_i < 0 or hor_i > 7 or ver_i < 0 or ver_i > 7:
            return False
        return self.board[hor_i][ver_i] is None

    def convert_indices_to_square(self, hor_i, ver_i):
        return f"{self.vertical_squares[ver_i]}{self.horizontal_squares[hor_i]}"

    def get_legal_moves_for_pawn(self, pawn):
        legal_moves = []
        horizontal_index = self.horizontal_indices[str(pawn.rank)]
        vertical_index = self.vertical_indices[pawn._file]
        print(horizontal_index, vertical_index)

        if pawn.color == "white":

            _a = (horizontal_index - 1, vertical_index)
            if self.square_empty(*_a):
                legal_moves.append(self.convert_indices_to_square(*_a))

                _b = (horizontal_index - 2, vertical_index)
                if pawn.rank == 2 and self.square_empty(*_b):
                    legal_moves.append(self.convert_indices_to_square(*_b))
            else:
                _c = (horizontal_index, vertical_index - 1)
                _d = (horizontal_index, vertical_index + 1)


        return legal_moves

    def legal_moves_for_a_piece(self, piece):
        if piece.piece == "pawn":
            return self.get_legal_moves_for_pawn(piece)
        return None

    def get_legal_moves(self):
        pass

    def find_best_move(self):
        pass

    def move(self, move: str):
        pass