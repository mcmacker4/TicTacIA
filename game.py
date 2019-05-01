from ai import PlayerAI


class Table:

    def __init__(self):
        self.data = [0 for _ in range(9)]

    def set(self, x, y, v):
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise IndexError("Position out of bounds.")
        if not self.data[y * 3 + x] == 0:
            raise IndexError("Position already in use.")
        self.data[y * 3 + x] = v

    def get(self, x, y):
        return self.data[y * 3 + x]

    def is_full(self):
        for i in self.data:
            if i == 0:
                return False
        return True

    def threeinarow(self, player):
        return ((self.get(0, 0) == self.get(0, 1) == self.get(0, 2) == player) or
                (self.get(1, 0) == self.get(1, 1) == self.get(1, 2) == player) or
                (self.get(2, 0) == self.get(2, 1) == self.get(2, 2) == player) or
                (self.get(0, 0) == self.get(1, 0) == self.get(2, 0) == player) or
                (self.get(0, 1) == self.get(1, 1) == self.get(2, 1) == player) or
                (self.get(0, 2) == self.get(1, 2) == self.get(2, 2) == player) or
                (self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == player) or
                (self.get(2, 0) == self.get(1, 1) == self.get(0, 2) == player))

    def __str__(self):
        value = ""
        value = value + " ".join(str(i) for i in self.data[0:3]) + "\n"
        value = value + " ".join(str(i) for i in self.data[3:6]) + "\n"
        value = value + " ".join(str(i) for i in self.data[6:9])
        return value


class Game:

    def __init__(self):
        self.table = Table()
        self.player = 1
        self.done = False
        self.winner = 0
        self.playerai = PlayerAI()

    def start(self):
        while not self.is_done():
            valid = False
            while not valid:
                try:
                    print("PLAYER %s'S TURN" % self.player)
                    print(self.table)
                    x, y = self.prompt()
                    valid = self.step(x, y)
                    self.player = [2, 1][self.player - 1]
                except ValueError:
                    print("Input should be a number")
        if not self.winner == 0:
            print("WINNER IS PLAYER %d" % self.winner)
        else:
            print("GAME WAS A TIE")
        print(self.table)

    def step(self, x, y):
        try:
            self.table.set(x, y, self.player)
            self.done = self.table.threeinarow(self.player)
            if self.done:
                self.winner = self.player
            return True
        except IndexError as e:
            print(e.args[0])
            return False

    def prompt(self):
        if self.player == 1:
            return self.prompt_user()
        else:
            return self.prompt_ai()

    def prompt_user(self):
        x = int(input("X: "))
        y = int(input("Y: "))
        return x, y

    def prompt_ai(self):
        return self.playerai.move(self.table.data)

    def is_done(self):
        return self.table.is_full() or self.done
