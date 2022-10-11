# **Main Match 3: Ghost Ladder In the Sky**

*A mysterious pair of floating ladder rails has appeared in the sky, and it’s up to you to assemble the rungs! Some unexpected visitors are here to tag along, though…*

### **Setup**

Main Match 3 will be played over 7 rounds. Players begin the game with 100 **Height**, which is used to create **rungs** on a **ladder** to score points.

### **Gameplay**

Each round, players submit a nonnegative integer amount of their remaining Height. Each player also has a corresponding **ghost** that submits the **midpoint** Height between the player’s submission for the current round and the player’s submission for the previous round, with ghosts submitting 0 in the first round. Non-integer ghost submissions are rounded towards the player’s previous submission. Ghost submissions are automatic and do **not** use up any of their owner’s Height.

At the end of each round, a **ladder** is formed by all the Heights submitted that round by either a player or a ghost. Each submitted **positive** Height creates a **rung** of that Height on the ladder. A **chain** is a set of rungs whose Heights are consecutive **decreasing** integers. Each player scores points equal to the length of the longest chain beginning from the rung at the Height they submitted.

Submissions of players and ghosts, as well as the scoreboard, are **not** made public. However, the total amount of Height spent by **players** each round (ghosts not included) is revealed. At the end of the game the final point totals are revealed.

Twice throughout the game, players may choose to be informed of their ranking on the scoreboard. They will receive results at the beginning of the **next** round, with points earned during the current round taken into effect. If there is a tie, the highest rank in the tie is used. 

Players may also choose to be informed of their current score by spending 2 garnets. Each additional purchase costs 2 more garnets than the last. Unlike the rank-checker, there is no delay before receiving results.

### **Winners**

The player with the most points after the final round wins two Tokens of Life, and the player with the second-most points wins one ToL. If there is a tie for first place, all of those who are tied win one ToL, with no further ToLs being given out. If there is a sole winner and a tie for second place, only two ToLs are given out; the sole winner chooses which of the tied players wins the other ToL.

A garnet is awarded at the end of the Main Match for every 20 points a player has scored. 

The player with the lowest score is the Elimination Candidate, with ties broken by a plurality vote among those who **won** a ToL in the Main Match (being given a ToL does not count as winning it). If there is a tie in voting, the player with the most votes and whose voters have the highest total of garnets (after garnet rewards are given out) becomes the EC. If this is still a tie, the EC is randomized.

### **Garnets**

A garnet can be used to increase your submission for a round by 3. You can use multiple garnets in a single round. Garnets cannot be used to increase ghost submissions (although increasing your player submission will affect your ghost’s submission for the next round). The increased Height from garnets is taken into account when the total Height spent in a round is revealed.

### **Submissions**

You have 24 hours each round to submit a nonnegative integer value less than or equal to your remaining Height. Your remaining Height will decrease by this amount when the round ends. Invalid and blank submissions are treated as a submission of 0.
