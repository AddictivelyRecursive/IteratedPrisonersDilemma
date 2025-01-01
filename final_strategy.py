from agent import BaseAgent
import random
import math
class final_strategy(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if itr >= 4:
            if state["history"][itr - 3][op_id] == 1 and state["history"][itr-2][self.id] == -1 and state["history"][itr - 2][op_id] == 1:
                return 1
            if state["history"][itr - 3][op_id] == 1 and state["history"][itr-2][op_id] == 1:
                return 1
        generosity = 0.25 / math.exp(state["streak"] * 0.07)
        if random.random() < generosity: return 1
        else: return state["history"][itr - 1][op_id] if itr != 1 else 1