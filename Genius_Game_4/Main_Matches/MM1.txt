# **Main Match 1: Social Snake**

*Maneuver your snakes across three grids to collect the most apples and garnets. Be wary of collisions, though, or you’ll lose apples!* 

### **Setup**

Main Match 1 will be played on three square grids: Grid A, Grid B, and Grid C, with sizes 15 x 15, 18 x 18, and 20 x 20, respectively. Every space of each grid contains either apples or garnets. The game will be played in two **phases**: in the first phase, Grid A is played on, and in the second phase, Grids B and C are played on at the same time; this means players must submit for both. Each phase lasts for at most 5 rounds.

For each grid, players will choose three possible starting positions, ordered in a priority list (first choice, second choice, and third choice). Players will then be assigned to the starting position highest in their priority list unless that space appears on another player’s priority list at an equal or higher priority level (i.e. they will get their first choice unless it appears in another player’s priority list as a first choice, second choice unless it appears in another list as a first or second choice, and similarly for their third choice).

If a player is not assigned a space through the above process, their starting position will be randomized. All apples and garnets on starting spaces will disappear into the void.

In addition, at the beginning of the game, please publicly claim a color (that has not been claimed by someone else) within the set that will be posted in #mm1-announcements.

### **Gameplay**

After the starting positions are decided, they will be publicly revealed. Each player controls a snake’s **Head** on each grid, initially located at their starting position. As they move their Head across the board, any space formerly occupied by their Head will become their **Body**. Each snake has a color corresponding to the player controlling it.

For each round, players submit a **movement sequence** comprising the individual up-down-left-right **moves** of their Heads for that round. Each move in a sequence moves the Head one space in that direction. For the first three rounds of each phase, movement sequences are limited to a single cardinal direction; for example, LLL, UU, and DDDDD are valid sequences, but LU, RRRDR, and DRUUL are not. In the fourth and fifth rounds, this restriction is removed. There is no restriction on the number of moves which can be made in a single round.

Moves resolve simultaneously for all movement sequences, in order. For example, if three movement sequences are ULLU, RDDRD, and LLLUR, the sets of moves will resolve in the following order: [U, R, L], [L, D, L], [L, D, L], [U, R, U], and [none, D, R]. 

After each individual UDLR move, every former location of a Head is replaced with a Body of the same color. This is repeated for every move until all move sequences in the round are resolved.

If after a round there are no items remaining on the grid that are possible to obtain, the grid will no longer be played on for the remainder of the phase.

A **collision** occurs if after a move, a Head moves onto a space with another Head or Body. All Heads involved in a collision give all the apples they earned on that grid in that round to the Body they have collided with (if there is no such Body, all Heads lose their apples for that round). The Heads also have their last moves (that caused the collision) taken back, and have their movement sequences terminated. The backtrack occurs immediately after the collision and before the next move of a normal movement sequence. Heads can move again on later rounds. 

After each move, Heads collect any apples or other items on the space they moved onto, unless a collision occurred on that space, in which case all items on that space vanish. This repeats for all moves in the movement sequence.

It is possible to collide into one’s own snake - this is equivalent to not moving. 

To aid in your understanding of the rules, several example scenarios with varying movement submissions have been posted in #mm1-examples.

### **Winners**

The player with the most apples over all three grids will receive Three Tokens of Life. The player with the second most apples wins Two Tokens of Life, and the player with the third most apples wins a single Token of Life. If there is a tie for first, all tied players would receive one Token of Life, and no other players receive a ToL. If there is a tie for second or third, all tied players would receive one Token of Life, provided that this would not cause the total ToL to exceed 6; if it does, none of the said tied players nor players with less apples receive a ToL. This tie rule for second and third is processed first for the players with the second most number of apples, then for the players with the third most number of apples. In addition, if the number of ToLs awarded to the players with the most and second most number of apples is 6, then the player with the third most apples, even if it is unique, will not receive a ToL.

The player with the least apples will become the Elimination Candidate. If this is a tie, the player(s) with the most apples will vote on who becomes the EC. If this vote is a tie, the player with the least apples, most votes, and least garnets will be the EC. If this is still a tie, screw you I flip a coin.

A garnet is awarded at the end of the Main Match if a player collects 200 apples. For every 50 apples after that, players earn an additional garnet. 

### **Results**

At the end of each round, all processed player moves, collisions, and the current grid state will be revealed. Attempted moves that don’t go through (moves that occur after collisions) will not be revealed. 

### **Garnets**

Garnets may be used to make a premoves. A premove will occur x moves before the first move, where x is the number of garnets you have spent on that move. Premoves resolve simultaneously; if two players both use a 1 garnet premove, their moves will resolve at the same time (but one move ahead of a normal sequence).

### **Submissions**

You have 24 hours of pregame, in which no submissions are due except for your color choice.

You have 24 hours after the pregame to submit your priority list(s) of starting positions. Priority lists should list the coordinates of each space chosen, from first to third.

You have 24 hours each round to make a movement submission. In the first phase, you only need to submit one movement sequence; in the second phase, you must submit two different movement sequences, one for each grid. You may choose not to submit. 

Invalid submissions (moving in more than one direction in the first three rounds of a phase, moving off the board, failing to submit) will be counted as a non-submission.
