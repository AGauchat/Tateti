class TaTeTi():

    def __init__(self, board=None):
        if board is None:
            self.board = [' ' for _ in range(9)]
        else:
            self.board = board

    def full(self):
        for icon in self.board:
            if icon == ' ':
                return False

        return True

    def win(self):
        try:
            for i in range(9):
                if self.board[i] == self.board[i + 1] == self.board[i + 2] != ' ':
                    return True

                if self.board[i] == self.board[i + 2] == self.board[i + 4] != ' ':
                    return True
                if i < 4:
                    if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ':
                        return True

                if i < 1:
                    if self.board[i] == self.board[i + 4] == self.board[i + 8] != ' ':
                        return True

            return False
        except:
            return False

    def validate(self, position):

        if self.board[position - 1] == ' ':
            return True

        return False

    def assign(self, position, piece):
        if self.board[position - 1] == ' ':
            self.board[position - 1] = piece
        else:
            raise Exception

    def draw_board(self):
        display = "\n"
        for num in range(9):
            if self.board[num] != " ":
                display += " " + self.board[num] + " "
            else:
                display += " " + str(1+num) + " "
            if num == 2 or num == 5:
                display += "\n---+---+---\n"
            elif num == 8:
                display += "\n"
            else:
                display += "|"

        return display
