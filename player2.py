from agent import BaseAgent
from random import randint

class p2(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        i = randint(1, 100)
        if i>80:
            return -1
        return 1