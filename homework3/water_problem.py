GOAL = 2

class Cup(object):

    capacity = 1
    contents = 0

    def __init__(self, cap=1, cont=0):
        if cap < cont:
            raise ValueError('Too much contents')
        if cont < 0:
            raise ValueError('Negative contents')
        self.capacity = cap
        self.contents = cont

    @property
    def space(self):
        return self.capacity - self.contents

    def is_goal(self):
        return self.contents == GOAL

    def __eq__(self, c):
        return self.capacity == c.capacity and self.contents == c.contents

    def pour_into(self, other_cup):
        return (
            Cup(
                cap=self.capacity,
                cont=self.contents-min(self.contents, other_cup.space)
            ),
            Cup(
                cap=other_cup.capacity,
                cont=other_cup.contents+min(self.contents, other_cup.space)
            )
        )

    def __repr__(self):
    	return "<Cup {}/{}>".format(self.contents, self.capacity)

import copy
from functools import reduce

or_reduction = lambda x, y: x or y
and_reduction = lambda x, y: x and y


class Game(object):

    cups = None
    parent = None       # Game that created this one
    children = None

    def __init__(self, sizes=None, parent=None):
        self.cups = []

        if sizes is None:
            # Set up cups with default sizes
            sizes = [(10, 0), (7, 7), (4, 4)]

        for cap, cont in sizes:
            self.cups.append(Cup(cap=cap, cont=cont))

        # Save a pointer to the parent
        self.parent = parent

        # Children starts empty
        self.children = []

    def is_goal(self):
       return reduce(
            or_reduction,
            [cup.is_goal() for cup in self.cups]
        )

    def __eq__(self, g):
        return (
            len(self.cups) == len(g.cups)
            and reduce(
                and_reduction,
                [cup == g.cups[pos] for pos, cup in enumerate(self.cups)]
            )
        )

    def net_has_game(self, g):
        return self.top_parent().has_game(g)

    def top_parent(self):
        return self if self.parent is None else self.parent.top_parent()

    def has_game(self, g):
        return (
            self == g
            or (
                len(self.children) > 0
                and reduce(
                    or_reduction,
                    [game.has_game(g) for game in self.children]
                )
            )
        )

    def make_game(self, c_a, c_b):
        new_game = copy.deepcopy(self)
        new_game.parent = self
        (new_game.cups[c_a],
         new_game.cups[c_b]) = new_game.cups[c_a].pour_into(new_game.cups[c_b])
        return new_game

    def make_children(self):
        for c_a in range(len(self.cups)):
            for c_b in range(len(self.cups)):
                if c_b == c_a:
                    continue
                new_game = self.make_game(c_a, c_b)
                if not self.net_has_game(new_game):
                    self.children.append(new_game)
        return len(self.children)

    def is_solvable(self):
        if self.is_goal():
            self.print_trace()
            return True

        if self.make_children() == 0:
            return False

        return self.solvable_child()

    def solvable_child(self):
        for child in self.children:
            if child.is_solvable():
                return True

        return False

    def print_trace(self):
        if self.parent is not None:
            self.parent.print_trace()
        print(self.cups)

Game()
print_trace()