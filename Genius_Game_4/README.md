# Genius Game 4  

Genius Game 4 is an Online Reality Game hosted over Discord with over 25 individually-designed games, inspired by the Korean show The Genius. These games feature strategic planning, alliances, psychology, and quick thinking. 

Many of the overarching game mechanics are explained in the archived introduction post below. Rules for various games as well as some screenshots are located in various subfolders.

### Introduction Post

Welcome to Genius Game 4, the fourth (or technically fifth) iteration of the Genius Game series.  Based off of the South Korean show The Genius, this ORG (Online Reality Game) consists of thirteen players competing in a myriad of challenges testing their strategic and social prowess. 

The ORG is divided into 12 **episodes**, with the first eleven episodes being divided into a **Main Match** (MM) and a **Death Match** (DM). In Main Matches, players vie to win immunity from the Death Match while avoiding losing and becoming the **Elimination Candidate** (EC). The winner(s) of the Main Match will receive a **Token of Life** (ToL), an item that grants immunity from the Death Match for that episode. Oftentimes a player will win more than one ToL, in which case they must give away all but one ToL to any player who is not the Elimination Candidate. You are allowed to give away ToLs such that you have none remaining; however, this means you are not immune and therefore may be picked for the DM. When all ToLs have been given out, the Elimination Candidate will select a player without a ToL as his/her **Death Match Opponent** (DMO) to compete with in the Death Match.

The Death Match is a 1v1 skill-based game between the Elimination Candidate and Death Match Opponent to decide who will be eliminated from the ORG. In this ORG, all Death Matches will be completely 1-on-1; that is, **players not in the Death Match will have no impact on it once it begins** (before the actual Death Match begins, other players may aid the Death Match participants with practice, advice, etc.). The winner of the Death Match will rejoin the rest of the players in the next episode, while the loser is eliminated from Genius Game 4. With regards to DM practice, you may only practice with other players. However, spectators may offer to host games if they please, but they cannot provide advice to or practice with players.

**Garnets** are the currency of the game. Players begin the game with 3 garnets and can earn more through performing well in Main Matches. Garnets can be used during Main Matches to purchase advantages to give them an edge over other players. The garnets of players eliminated in Death Matches are discarded.
 
The final episode is a best-of-5 series of **Final Matches**. These Final Matches will consist of both previously played games and entirely new games. Before the Final Matches begin, the finalists will bid on special items specific to each game with their garnets. Eliminated players will choose a finalist to support, giving them a set number of garnets,  depending on their placing. 13th place will be able to give 10 garnets, 12th place 11 garnets, and so on until 3rd place can give 20 garnets to a finalist of their choosing. Aside from the items, the Final Matches will be identical in format to the Death Matches - they will be purely 1-on-1 games between the two finalists. The player who wins three of the Final Matches will be crowned the winner of Genius Game 4.

### Creation

The game lasted around two-thirds of a year, but planning and drafting began in 2018. 

The game was ran by three hosts, one of which was myself. I was in charge of creating and balancing the 11 Main Matches, though I did write rounds for certain Death Matches and implemented three of the five Final Matches.

Many designs were created and thrown out; I had personally written around 25 Main Matches, but only 11 were used in the final iteration. Combined, the 11 chosen Main Matches had over 10,000 words.

The Main Matches were planned with the following criteria in mind:

- Anti-Majority: There was no easy way for a majority of players to easily gang up on a minority of players to prevent the minority from winning (in this case, receiving a Token of Life). This prevents Main Matches from becoming a curbstomp and allows socially isolated players counterplay.

- Minimal Luck: There is minimal luck involved in the final result of a game. If luck was present, its effect was diminished through the use of bidding or other mechanics. Psychological aspects (ex. *reading* players from their personalities and past decisions) do not count as luck, as just like in Poker, it is a skill that can be honed over time.

- Social Planning: Players should benefit from making social connections with other players, and can use these connections to help or betray their allies. Communication should be a large part of the ORG.

- Strategic Depth: The games have many distinct strategies that can lead to success. The main difficulty is finding the optimal strategy and implementing it successfully.

### Implementation

Many of the Main Matches took around a week and had deadlines every 24 hours. Death Matches were done live. 

Certain Main Matches had a program specificially written for them in order to process submissions: the more notorious ones were Main Matches 2, 6, 9, and 10, 9 being by far the hardest (requiring four separate input files). I have code for Main Match 6, though my other programs are forever lost on a former laptop's hard drive. 

The same applied to certain Death Matches; in fact, the other host specifically programmed a Discord bot to host a handful of them. I do not have access to their code. 

The game eventually ended in a draw at the Final 2, after both players were tied 2-2 in Finals. One player was unable to continue because of a serious family issue, and the game unfortunately had to finish early. 

### mm6.py Sample Output

```python3 mm6.py
. . . . . . . . . . . . . . . 
. . . 111 . . . . . . . . . . . 
. . 111 . 011 . . . . . . 010 . . . 
. . 111 . 011 . . . . . . 010 . . . 
. . 111 . 011 . . . . . . 010 . . . 
. . . 011 . . . . . . . 010 . . . 
. . . . . . . . . . . 110 . . . 
. . . 100 . . . . . . . 110 . . . 
. . 100 100 000 . 101 . . . . 110 . . . 
. . . 100 . 101 . . . . . . . . . 
. . . . . . 000 . . . . 001 001 . . 
. . . . . 000 101 101 . . . 001 . . . 
. . . . . . 000 . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 

. . . . . . . . . . . . . . . 
. . . 111 . . . . . . . . . . . 
. . 111 . 011 . . . . . . . . . . 
. 111 111 . 011 011 . . . . 010 010 010 . . 
. . 111 . 011 . . . . . 010 010 010 . . 
. . . 011 . . . . . . 010 010 010 . . 
. . . . . . . . . . 110 110 110 . . 
. . 100 100 100 . . . . . 110 110 110 . . 
. . 100 . . 101 . . . . . . . . . 
. . 100 100 . 101 101 . . . . 001 001 . . 
. . . . 100 . . 101 . . . 001 001 . . 
. . . . . 000 . 101 . . . 001 001 . . 
. . . . . 000 000 101 . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
```

(The former is the initial grid; the latter is the generated grid.)

### Screenshots

Pictures of various ORG events are shown below. 

#### Main Match 1

![MM1](./Screenshots/MM1_pic.png?raw=true "MM1")

#### Main Match 6

![MM6](./Screenshots/MM6_pic.png?raw=true "MM6")

#### Death Match 6

![DM6](./Screenshots/DM6_pic.png?raw=true "DM6")

#### Closing

![Closing](./Screenshots/Closing.png?raw=true "Closing")

