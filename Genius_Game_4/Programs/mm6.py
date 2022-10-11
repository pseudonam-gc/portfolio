# Given a 15x15 text file consisting of "." and 3-digit binary strings delimited by spaces, print the next iteration of the grid supposing Game of Life rules are applied.
# In this particular variant, each binary string is a living cell, and each period is empty space. 
# Cells created in the next iteration spawn with strings that match the majority of their three neighbors' values for each index.
# For instance, if a newly created cell has neighbors 001, 101, and 111, it would have the string 101.
# Written by pseudonam

# Parses file input from mm6.txt

fin = open('mm6.txt', 'r')
gamelist = []
with fin as f:
    content = f.readlines()
content = [x.strip() for x in content]
for i in range(len(content)):
    content[i] = content[i].split()
    gamelist.append(content[i])

# Various print functions 

def profprint():
    for i in range(len(gamelist)):
        x = ""
        for j in range(len(gamelist[i])):
            x += str(gamelist[i][j])
            x += " " 
        print (x)
    print ("")

def find_neighbors(inlist, posi, posj): # Finds the neighbors of a given node
    neighborlist = []
    vsearch = [posi]
    hsearch = [posj]
    if posi > 0:
        vsearch.append(posi-1)
    if posj > 0:
        hsearch.append(posj-1)
    if posi < 14:
        vsearch.append(posi+1)
    if posj < 14:
        hsearch.append(posj+1)
    for i in vsearch:
        for j in hsearch:
            if not (i == posi and j == posj):
                inp = inlist[i][j]
                if inp != '.':
                    neighborlist.append(inp)
    return neighborlist

def movestate():
    # Makes a copy of gamelist, and then proceeds to fill it
    newlist = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(15):
        for j in range(15):
            # For each space, find the neighbor count
            x = find_neighbors(gamelist, i, j) 
            # The cell is certainly dead if it has >3 or <2 neighbors
            if len(x)>3 or len(x)<2:
                newlist[i].append(".")
            elif gamelist[i][j] != ".":
                # If it was living last iteration, it still necessarily survives.
                newlist[i].append(gamelist[i][j])
            else:
                # The only remaining case is that it is being created.
                # Fill the string number with the correct 3-digit binary string. Then add it to the grid.
                if len(x) == 3:
                    indices = [[],[],[]]
                    for k in x:
                        for l in range(len(k)):
                            indices[l].append(k[l])
                    number = ""
                    for k in range(3):
                        if indices[k].count("0") >= 2:
                            number+="0"
                        else:
                            number+="1"
                    newlist[i].append(number)
                else:
                    newlist[i].append(".")
    return newlist

# This prints the grid, then proceeds to print the modified grid.
profprint()
x = movestate()
gamelist = x
profprint()
