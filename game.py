

class Table:

    def __init__(self):
        self.data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def set(self, x, y, v):
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise IndexError("Position out of bounds.")
        if not self.data[y][x] == 0:
            raise IndexError("Position already in use.")
        self.data[y][x] = v

    def is_full(self):
        for r in self.data:
            for i in r:
                if i == 0:
                    return False
        return True

    def threeinarow(self):
        t = self.data
        return (
            (t[0][0] == t[0][1] == t[0][2]) and (not t[0][0] == 0) or
            (t[1][0] == t[1][1] == t[1][2]) and (not t[1][0] == 0) or
            (t[2][0] == t[2][1] == t[2][2]) and (not t[2][0] == 0) or
            (t[0][0] == t[1][0] == t[2][0]) and (not t[0][0] == 0) or
            (t[0][1] == t[1][1] == t[2][1]) and (not t[0][1] == 0) or
            (t[0][2] == t[1][2] == t[2][2]) and (not t[0][2] == 0) or
            (t[0][0] == t[1][1] == t[2][2]) and (not t[0][0] == 0) or
            (t[2][0] == t[1][1] == t[0][2]) and (not t[2][0] == 0)
        )

    def __str__(self):
        return "\n".join([" ".join([str(v) for v in r]) for r in self.data])


class Game:

    def __init__(self):
        self.table = Table()
        self.value = 1

    def start(self):
        while not self.is_done():
            print(self.table)
            valid = False
            while not valid:
                x, y = self.prompt()
                valid = self.step(x, y)
        print(self.table)
        print("DONE!")

    def step(self, x, y):
        try:
            self.table.set(x, y, self.value)
            self.value = [2, 1][self.value - 1]
            return True
        except IndexError as e:
            print(e.args[0])
            return False

    def prompt(self):
        if self.value == 1:
            return self.prompt_user()
        else:
            return self.prompt_ai()

    def prompt_user(self):
        x = int(input("X: "))
        y = int(input("Y: "))
        return x, y

    def prompt_ai(self):
        return self.prompt_user()

    def is_done(self):
        return self.table.is_full() or self.table.threeinarow()
