from agent import BaseAgent
import random

class GTFT(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        coop_streak = 0
        
        # Calculate the adjusted coop_streak based on continuous cooperation
        for i in range(len(state["history"]) - 1, 0, -1):
            if state["history"][i][1] == 1 and state["history"][i][2] == 1:
                coop_streak += 1
            else:
                break
                
        # Adjust coop_streak as per the rule (increase by 1 for every 5 continuous cooperations)
        coop_streak = (coop_streak + 4) // 5
        
        itr = state["current_iter"]
        
        if itr == 1:
            return 1  # Cooperate in the first round
        
        # Extract opponent's last move
        opponent_last_move = state["history"][-1][op_id]
        
        # Extract own last move
        own_last_move = state["history"][-1][self.id]
        
        # Adjusted payoff matrix values based on streak
        coop_win = 20 + 5 * coop_streak
        betrayal_win = 45
        betrayal_lose = -10 * coop_streak
        defect = -5 * coop_streak
        
        # Determine action based on opponent's last move
        if opponent_last_move == -1:  # Opponent defected
            return -1  # Retaliate with defection
        
        # Misinterpretation of cooperation as defection
        elif opponent_last_move == 1 and own_last_move == -1:
            # Halve the streak if cooperation is misinterpreted as defection
            coop_streak = max(0, coop_streak // 2)
            return -1  # Retaliate with defection
        
        elif random.random() < 0.01:  # 1-2% chance of misinterpreting cooperation as defection
            # Halve the streak if cooperation is misinterpreted as defection
            coop_streak = max(0, coop_streak // 2)
            return -1  # Retaliate with defection
        
        elif own_last_move == 1 and opponent_last_move == 1:  # Both cooperate
            return 1
        
        elif own_last_move == 1 and opponent_last_move == -1:  # You cooperate, opponent defects
            return -1
        
        elif own_last_move == -1 and opponent_last_move == 1:  # You defect, opponent cooperates
            return 1
        
        else:  # Both defect
            return -1
