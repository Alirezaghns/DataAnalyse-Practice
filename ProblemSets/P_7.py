class Piece:
    def __init__(self, sort, color, position):
        self.sort = sort
        self.color = color
        self.position = position


class Board:
    def __init__(self):
        self.position = {
            (10, 10): Piece("K", "black", (10, 10)),
            (-10, -10): Piece("K", "white", (-10, -10))
        }

    def add(self, piece):
        if piece.sort != "K" and piece.position not in self.position.keys():
            self.position[piece.position] = piece
        else:
            print("Invalid query!")

    def remove(self, position):
        if position in self.position.keys() and self.position[position].sort != "K":
            del self.position[position]
        else:
            print("Invalid query!")

    def move(self, piece, position):
        if self.position[piece.position] == piece:
            if position not in self.position.keys():
                del self.position[piece.position]
                self.position[position] = piece
            
            elif self.position[position].color != piece.color and self.position[position].sort != "K":
                del self.position[piece.position]
                self.position[position] = piece
            
            else:
                print("Invalid query!")

    def is_mate(self, color):
        for piece in self.position.values():
            if piece.sort == "K" and piece.color == color:
                king = piece
        
        for col in range(king.position[0]-8, king.position[0]+9):
            for row in range(king.position[1]-8, king.position[1]+9):
                current_position = (col, row)
                if current_position in self.position.keys():
                    if self.position[current_position].sort == "P" and \
                    self.position[current_position].color != color:
                        return True
        return False


white_p_1 = Piece("P", "white", (1, 5))
white_p_2 = Piece("P", "white", (-10, 3))
white_p_3 = Piece("P", "white", (-8, -5))

black_p_1 = Piece("P", "black", (-17, -4))

board = Board()

board.add(white_p_1)
board.add(white_p_2)
board.add(white_p_3)

board.add(black_p_1)


# board.remove((-10, 3))

# board.move(white_p_1, (10, 10))

print(board.is_mate("white"))

# print(*board.position, sep="\n")
