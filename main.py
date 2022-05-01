class Board:
    data = list()
    vals = [i for i in range(9)]  # all index value

    def __init__(self):
        self.data = list('-'*9)

    def set_val(self, val, index):
        assert self.data[index] == '-', f"תפוס"
        self.data[index] = val

    def show_board(self):

        d = self.data
        msg = f"[{d[0]}] [{d[1]}] [{d[2]}]\n[{d[3]}] [{d[4]}] [{d[5]}]\n[{d[6]}] [{d[7]}] [{d[8]}]"
        print(msg)

    def is_game_end(self):
        if self.data[0] != '-' and self.data[0] == self.data[1] == self.data[2]:
            return f"player {self.data[0]} is the WINNER"
        if self.data[3] != '-' and self.data[3] == self.data[4] == self.data[5]:
            return f"player {self.data[3]} is the WINNER"
        if self.data[6] != '-' and self.data[6] == self.data[7] == self.data[8]:
            return f"player {self.data[6]} is the WINNER"
        if self.data[0] != '-' and self.data[0] == self.data[3] == self.data[6]:
            return f"player {self.data[0]} is the WINNER"
        if self.data[1] != '-' and self.data[1] == self.data[4] == self.data[7]:
            return f"player {self.data[1]} is the WINNER"
        if self.data[2] != '-' and self.data[2] == self.data[5] == self.data[8]:
            return f"player {self.data[2]} is the WINNER"
        if self.data[0] != '-' and self.data[0] == self.data[4] == self.data[8]:
            return f"player {self.data[0]} is the WINNER"
        if self.data[2] != '-' and self.data[2] == self.data[4] == self.data[6]:
            return f"player {self.data[2]} is the WINNER"

        if '-' not in self.data:
            return f"No one won. TEKO"


game = Board()
counter = 0
while counter < 9:

    # X starting first, so every "even" turn, its x
    val_turn = "O" if counter % 2 else 'X'

    cont = True;
    while cont:
        try:
            game.show_board()
            tx = input(f"{val_turn} Turn! - choose location 1-9 : ")
            tx = int(tx)
            assert tx-1 in game.vals
            game.set_val(val_turn, tx-1)
        except Exception as e:
            print(f"\nError. sorry! try again ({str(e)})\n")
            continue
        cont = False

    counter += 1
    msg = game.is_game_end()
    if msg is None:
        continue
    else:
        print("\n\n*******************")
        print(msg)
        game.show_board()
        print(msg)
        print("*******************\n\n")
        break
