# Goofspiel Solver

### Introduction to Goofspiel 

Goofspiel, or the Game of Pure Strategy, is a psychological game. Each player has a limited hand of cards, and there is a central prize deck (cards worth certain values -- generally, 1 through some integer n inclusive). Players do not know the order of the cards in the prize deck. In each round, a card is flipped face-up from the prize deck, and players play a card from their hand face-down in an attempt to win it. Players flip their cards at the same time, and the player with a higher card takes the prize card (if there is a draw, nobody wins it), and this repeats until the prize deck is empty. The winner is the player with the highest sum of prize card values.

This game has a lot of surprising depth: the obvious 'greedy' strategy (playing the nth highest card when the nth highest prize card is played) loses to a player who shifts the entire sequence by one (playing the n+1th highest card when the nth highest prize card is played, and playing 1 on the highest prize card). 

In fact, every strategy loses to a player who plays n+1 every time their opponent plays n, with the exception of the highest card. 

In practice, players do not enter the game with an exact permutation of cards they wish to play, and end up trying to read their opponent and either beat them by as little as possible, or lose by as much as possible (in order to save higher card values for later). 

Since every strategy has a counter, there is no simple strategy that wins the most times. But this can be represented as a matrix game -- so it is possible to maximize the expected value of the difference between your score and your opponent's score with a little bit (an exaggeration) of dynamic programming.

### The Solver

One of the ORGs (Online Reality Games) I was in had me playing a combination of Gale and Goofspiel against another player. Gale was already mathematically solved. The host's variant of Goofspiel, having different prize card values other than the standard first n integers, was not. So I took it upon myself to code an entire solver from scratch. 

It was too difficult to search through the solutions file during the actual game (even when translated onto Google Sheets) because automated tools, including CTRL-F, weren't allowed. But that's okay -- just the ideal probabilities for the modified initial state gave me such an advantage that it all but won me the game. (I then proceeded to blunder away my advantage, but my opponent wasn't able to capitalize on it, eventually leading to my win.)

I have generalized the code and added additional comments to make things more readable. The prize cards can be adjusted as well as the individual player hands, but the number of prize cards should be equal to the number of cards each player has. This requires, among other things, the GUROBI optimizer, of which a temporary free version is available via "pip3 install gurobipy".

Goofspiel for the first n integers up to n=13 has already been analyzed, and do note that my results for the initial state match up with the results on this site, confirming its validity: http://gcrhoads.byethost4.com/gops.html?i=1.

Output for the 5-card case is currently in solution.txt, in the format:

player cards | opponent cards | prize cards | upcard | additive probability vector

The additive probability vector is an easier way to use a probabiliy vector (say, in an actual game). It also does not have to deal with funny rounding issues and can be expressed compactly. Take the following example into account (which is near the bottom of solution.txt):

1 2 3 4 5|1 2 3 4 5|1 2 3 4 5|4|1: 12 2: 19 3: 38 4: 59 5: 100 

Both players have cards {1, 2, 3, 4, 5} and the deck has prize cards {1, 2, 3, 4, 5}. The current card that gets flipped up is a 4. 

If you roll an 100-sided die, and get less than or equal to 12, play a 1.
Otherwise, if you get less than or equal to 19, play a 2.
Otherwise, if you get less than or equal to 38, play a 3.
Otherwise, if you get less than or equal to 59, play a 4.
Otherwise, play a 5.

Using this throughout a game will maximize the expected value of your score difference against an optimal opponent.

### Sample Output

```python3 goofspiel_solver.py
Restricted license - for non-production use only - expires 2023-10-25
1 0.00017404556274414062
2 0.9584460258483887
3 1.6427948474884033
4 0.36036086082458496
5 0.004511833190917969
1 [(0, 0.0), (1, 0.046988701493370366), (2, 0.8327260280411943), (3, 0.1202852704654353), (4, 0.0), (5, 0.0)]
2 [(0, 0.0), (1, 0.18545955578064546), (2, 0.0), (3, 0.7374907173835069), (4, 0.07704972683584765), (5, 0.0)]
3 [(0, 0.0), (1, 0.11816972506630222), (2, 0.11879904625111658), (3, 0.0), (4, 0.7630312286825812), (5, 0.0)]
4 [(0, 0.0), (1, 0.12259051709006223), (2, 0.07346766284674612), (3, 0.19149836113740445), (4, 0.20433723414426616), (5, 0.4081062247815211)]
5 [(0, 0.0), (1, 0.11230330163341617), (2, 0.024102683112364194), (3, 0.0), (4, 0.0), (5, 0.8635940152542196)]```