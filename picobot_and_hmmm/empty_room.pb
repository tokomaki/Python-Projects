# PicoBot program that instructs the bot to cover the entirety of an 
# empty rectangular room.

# Go North as possible
0 X*** -> N 0

# If North cell is a wall stay put and change to state 1
0 N*** -> X 1

# Continue to go East
1 *X** -> E 1

# If East cell is a wall move South and change to state 2
1 *E** -> S 2

# Continue to go South
2 ***X -> S 2

# If South cell is a wall move West and change to state 3
2 ***S -> W 3

# state 3 with nothing N: go one step N
3 x*** -> N 3  

# state 3 with something to the N: go W + into st 4 
# ** This will crash if picobot has a wall to the W! **
3 N*** -> W 4 


# state 4 with nothing to the S: go one step S
4 ***x -> S 4   

# state 4 with something to the S: stay put + into state 3
4 ***S -> X 3
