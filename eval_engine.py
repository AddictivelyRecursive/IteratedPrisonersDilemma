import time, threading, random, math, json, copy
from agent import BaseAgent
import player1,player2
program_names = ['agent1', 'agent2']

COOP = 1
DEFECT = -1

player1 = player1.p1(1)
player2 = player2.p2(2)
players: list[BaseAgent] = [player1, player2]

move_queue = [0, 0]

coop_win = lambda x: 20 + 5 * (x // 5)
betrayal_win = lambda x: 50
betrayal_lose = lambda x: -10 * (x // 5)
defect = lambda x: -5 * (x // 5)
payoff_matrx = [[coop_win, coop_win], [betrayal_win, betrayal_lose], [defect, defect]]

error = 0.05
time_limit = 0.01  # seconds
rounds = 100

streak = 0
history = {}

player_threads = []

iteration = 1
streak = 0
score = {1: 0, 2: 0}


def threaded_player_call(player, streak, iteration):
    global move_queue
    state = {"current_iter": iteration, "history": history, "streak": streak}
    state = copy.deepcopy(state)
    move = players[player].next_move(state)
    # print(f"Player {player}:", move, iteration, history)
    if not iteration in history:
        move_queue[player] = move


def event_loop():
    global iteration, streak, score, move_queue, history
    while iteration <= rounds:
        # Starts threads to wait for agents to update move_queue and then waits for time limit
        threading.Thread(target=threaded_player_call, args=(0, None, iteration)).start()
        threading.Thread(target=threaded_player_call, args=(1, None, iteration)).start()
        time.sleep(time_limit)

        # If TLE on first then random, else repeat last move
        if not move_queue[0] or move_queue[0] not in [COOP, DEFECT]:
            if iteration == 1:
                move_queue[0] = random.choice([COOP, DEFECT])
            else:
                move_queue[0] = history[iteration - 1][1]

        if not move_queue[1] or move_queue[1] not in [COOP, DEFECT]:
            if iteration == 1:
                move_queue[1] = random.choice([COOP, DEFECT])
            else:
                move_queue[1] = history[iteration - 1][2]

        # errors in communication with agents
        is_err1 = random.random() < error
        is_err2 = random.random() < error

        if is_err1:
            move_queue[0] = -move_queue[0]
        if is_err2:
            move_queue[1] = -move_queue[1]

        """
        Payoff matrix calculations
        Streak is not reset to 0 if rift in communication is caused by errors
        """

        if move_queue[0] == COOP and move_queue[1] == COOP:
            score[1] += payoff_matrx[0][0](streak)
            score[2] += payoff_matrx[0][1](streak)
            streak += 1
        elif move_queue[0] == DEFECT and move_queue[1] == COOP:
            score[1] += payoff_matrx[1][0](streak)
            score[2] += payoff_matrx[1][1](streak)
            streak = math.ceil(streak / 2) if (is_err1 or is_err2) else 0
        elif move_queue[0] == COOP and move_queue[1] == DEFECT:
            score[1] += payoff_matrx[1][1](streak)
            score[2] += payoff_matrx[1][0](streak)
            streak = math.ceil(streak / 2) if (is_err1 or is_err2) else 0
        else:
            score[1] += payoff_matrx[2][0](streak)
            score[2] += payoff_matrx[2][1](streak)
            streak = math.ceil(streak / 2) if (is_err1 and is_err2) else 0

        history[iteration] = {
            1: move_queue[0],
            2: move_queue[1],
            "score": copy.deepcopy(score),
        }
        move_queue = [0, 0]

        iteration += 1


event_loop()
print(json.dumps(history, indent=4))
