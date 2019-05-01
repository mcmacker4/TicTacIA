from random import randrange


class Node:

    def __init__(self, state, action):
        self.state = state
        self.action = action
        self.children = []

    def __str__(self):
        return str(self.state) + " A:" + str(self.action)


def gen_tree():

    def gen_children(current, player):
        for i, v in enumerate(current.state):
            if v == 0:
                state = current.state.copy()
                state[i] = player
                child = Node(state, i)
                current.children.append(child)
                gen_children(child, [2, 1][player - 1])

    node = Node([0 for _ in range(9)], -1)
    gen_children(node, 1)
    return node


def threeinarow(state, player):
    return ((state[0 * 3 + 0] == state[0 * 3 + 1] == state[0 * 3 + 2] == player) or
            (state[1 * 3 + 0] == state[1 * 3 + 1] == state[1 * 3 + 2] == player) or
            (state[2 * 3 + 0] == state[2 * 3 + 1] == state[2 * 3 + 2] == player) or
            (state[0 * 3 + 0] == state[1 * 3 + 0] == state[2 * 3 + 0] == player) or
            (state[0 * 3 + 1] == state[1 * 3 + 1] == state[2 * 3 + 1] == player) or
            (state[0 * 3 + 2] == state[1 * 3 + 2] == state[2 * 3 + 2] == player) or
            (state[0 * 3 + 0] == state[1 * 3 + 1] == state[2 * 3 + 2] == player) or
            (state[2 * 3 + 0] == state[1 * 3 + 1] == state[0 * 3 + 2] == player))


class PlayerAI:

    def __init__(self):
        self.player = 2
        self.node = gen_tree()

    def find_node(self, state):
        for ch in self.node.children:
            if state == ch.state:
                self.node = ch

    def move(self, state):
        self.find_node(state)
        self.node = self.best_move()
        y, x = divmod(self.node.action, 3)
        return x, y

    def best_move(self):

        for i, child in enumerate(self.node.children):
            if threeinarow(child.state, self.player):
                return child

        for i, child in enumerate(self.node.children):
            hypo = child.state.copy()
            hypo[child.action] = 1
            if threeinarow(hypo, 1):
                return child

        def win_count(child):
            if threeinarow(child.state, self.player):
                return 1
            if len(child.children) == 0:
                return 0
            count = 0
            for ch in child.children:
                count = count + win_count(ch)

            return count

        counts = [win_count(ch) for ch in self.node.children]
        best = max(counts)
        indices = []
        for i, v in enumerate(counts):
            if v == best:
                indices.append(i)
        return self.node.children[indices[randrange(len(indices))]]
