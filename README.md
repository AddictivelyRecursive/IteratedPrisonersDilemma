
# Iterated Prisoner's Dilemma with Dynamic Payoff and Noise

This project explores a variant of the Iterated Prisoner's Dilemma (IPD) with dynamic payoff matrices and communication noise, inspired by Robert Alexedro's Strategy Comparison Games. It was developed as part of a competition at APOGEE, the technical fest of BITS Pilani, and secured the 2nd Prize. Below is a detailed description of the problem and our approach.

# Problem Description

The project focused on a twist to the classic Prisoner's Dilemma, incorporating the following unique elements:

Dynamic Payoff Matrix:
\
The payoff matrix evolves based on a streak of successful cooperation.
For every 5 consecutive cooperative interactions, a variable N increases.
N linearly affects the cooperation and defection payoffs, emphasizing the long-term benefits and risks of maintaining trust.

Noise in Communication:
\
Approximately 1-2% of cooperative moves were misinterpreted as defections.
Misinterpreted cooperation halves the streak of trust between players, fostering skepticism but not outright distrust.
A true defection from either party resets the streak entirely.

Human/Institutional Dynamics:
\
The game was designed to mimic real-world relationships where long-term cooperation yields significant benefits but carries the risk of great loss.

# Approach
Our solution employed a modified Tit-for-Tat strategy, carefully adapted to the noisy and dynamic environment:

Generosity Term:
\
Incorporated a generosity factor based on the cooperation streak, adjusting tolerance for noise and misinterpretations.
This factor was governed by an exponentially decaying function of the streak length to balance risk and trust.

Hyperparameter Optimization:
\
Hyperparameters for the generosity term were fine-tuned via extensive experimentation.
This ensured an optimal balance between maintaining cooperation and handling noise effectively.

Streak Accounting:
\
The strategy explicitly accounted for the evolving cooperation streak to maximize payoffs while minimizing unnecessary resets.

## Lessons Learned

This innovative approach proved to be highly effective, leading to a 2nd-place finish at the IEEE Event during APOGEE 2024. The project demonstrated how strategic adjustments to classic game theory models can yield robust results in dynamic, noisy environments.
