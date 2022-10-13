# This program maximizes the expected value won from a Goofspiel game.
# Algorithm modified from https://mdpi-res.com/games/games-03-00150/article_deploy/games-03-00150.pdf?version=1352361394
# Written by pseudonam

# Various imports

from itertools import combinations
import pulp as p
import time

# These variables can be freely modified. Note that heavy GPU utilization will be required for hands larger than size 7.
# score_list is the deck containing the prize cards, and your_hand and opponent_hand are self-explanatory

score_list = (1,2,3,4,5)
your_hand = (1,2,3,4,5)
opponent_hand = (1,2,3,4,5)

# Create a file to print results out to.

fout = open('solution.txt', 'w')

m = p.apis.GUROBI(msg=False)

def computeStrategy(state, upcard, f, optimal, solver, file): # Computes a strategy given a given state and upcard.
    # state is the (V, Y, P) triple -- that is, your cards, your opponent's cards, and the remaining deck cards. optimal is the dictionary of all optimal moves.
    # the upcard is the current face-up prize card.
    # also, this returns the expected score if played optimally. more importantly, this adds the optimal move vector into the dictionary named optimal.
    lp_prob = p.LpProblem('problem', p.LpMaximize)
    lp_dict = {} # maps integers to variables, which are used for the linear programming solution
    lp_dict[0] = p.LpVariable("v")
    for i in state[0]:
        lp_dict[i] = (p.LpVariable(str(i), lowBound = 0))
    lp_prob += lp_dict[0]
    # adds each individual variable to the problem. they must all be >=0.
    # add the various other conditions
    pstate = list(state[2][:])
    pstate.remove(upcard) # decides p in advance
    pstate = tuple(pstate)
    # this may seem a bit complicated, but it simply converts goofspiel into a matrix game based off of previous optimal play and feeds it to the solver.
    # the following generates every possible player and opponent card combination. 
    for i in range(len(state[1])):
        summer = 0
        y = list(state[1][:])
        enemy_card = y.pop(i)
        y = tuple(y)
        for j in range(len(state[0])):
            v = list(state[0][:])
            player_card = v.pop(j)
            v = tuple(v)
            # the score of a new position is the score of the previous position plus or minus the upcard, depending on who wins.
            f_constant = f[(v, y, pstate)]
            if player_card > enemy_card:
                f_constant += upcard
            elif enemy_card > player_card:
                f_constant -= upcard
            summer += f_constant*lp_dict[state[0][j]] # the constant * x[i]
        # the generic matrix game linear programming formula.
        lp_prob += summer-lp_dict[0] >= 0
    # note that we want a probability vector; a list n of probabilities detailing the card you should play
    # the probabilities have to sum to 1, so add that to the LP.
    summer = 0
    for i in lp_dict:
        if i != 0:
            summer += lp_dict[i]
    lp_prob += summer == 1
    # now solve
    status = lp_prob.solve(solver)
    # now that the matrix is solved, the place the following in the dictionary which details optimal moves
    optimal[(state, upcard)] = ([(i, p.value(lp_dict[i])) for i in lp_dict])
    # place optimal moves in a special format in the output file
    dict_to_string = ""
    summer = 0
    for i in lp_dict:
        if i != 0:
            summer += p.value(lp_dict[i])*100
            dict_to_string += str(i) + ": " + str(int(summer)) + " "
    fout.write(" ".join([str(x) for x in state[0]]) + "|" + " ".join([str(x) for x in state[1]]) + "|" + " ".join([str(x) for x in state[2]]) + "|" + str(upcard) + "|" + dict_to_string + "\n")
    # and finally return the value of the given position
    return p.value(lp_dict[0])

# compute base cases
f = {} # the expected score value for any triple (V, Y, P)
optimal = {} # optimal moves for said triple yee

# generates the expected point gain when one card remains for every set of cards and prize cards.

t = time.time()

for psub in your_hand:
    for esub in opponent_hand:
        for card in score_list:
            if psub > esub:
                # if your card wins, you score points equal to the prize card's value
                f[((psub,), (esub,), (card,))] = card 
            elif esub > psub:  
                # if the opponent wins, they score points (equivalent to you losing points) equal to the prize card's value
                f[((psub,), (esub,), (card,))] = card * -1
            else: 
                f[((psub,), (esub,), (card,))] = 0

# compute cases recursively with larger number of cards remaining. also, prints the amount of time it takes to find n.
print (1, time.time()-t)
t = time.time()
for i in range(2, len(score_list)+1):
    for phand in combinations(your_hand, i):
        for ehand in combinations(opponent_hand, i):
            for cards in combinations(score_list, i):   
                # by symmetry, if you swap game-states with your opponent, the value of the game for you should be negated.
                # the following condition can be added, but solution.txt will lack around half its probability vectors.
                # however, it is still usable by searching the position with hands switched.
                """if (ehand, phand, cards) in f:
                   f[(phand, ehand, cards)] = f[(ehand, phand, cards)]*-1
                else:"""
                value = 0 # the expected value of your hand if you play perfectly
                # consider all possible upcards (a random one appears) and average the results to obtain the expected value
                for card in cards:
                    c = computeStrategy((phand, ehand, cards), card, f, optimal, m, fout)
                    value += c
                value = value / len(cards) # finish averaging the value by dividing
                f[(phand, ehand, cards)] = value
    # prints the processing time of each segment
    print (i, time.time()-t)
    t = time.time()

# prints the probability vector for the game's opening indexed by the first upcard
for i in score_list: 
    print (i, optimal[((your_hand, opponent_hand, score_list), i)])

fout.close()
