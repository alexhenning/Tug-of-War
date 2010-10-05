
import random, math

class Action(dict):
    def __init__(self, action, **kwargs):
        self.action = action
        super(Action, self).__init__(**kwargs)

class SimpleAI(object):
    def __init__(self, player):
        self.player = player
    def tick(self, world):
        return Action("move", dest=self.player.dest)
