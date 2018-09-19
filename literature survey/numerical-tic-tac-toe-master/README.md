# Numerical Tic-tac-toe

A 4x4 numerical tic-tac-toe game written in python 3. 

Numerical tic-tac-toe is similar to normal tic-tac-toe, except instead of X's and O's the two players are given the numbers:

- {1, 3, 5, 7, 9, 11, 13, 15}
- {2, 4, 6, 8, 10, 12, 14, 16}

Respectively.

The players take turns (the odd player goes first) and each round a player puts one unused number on an open spot on the board. The goal is to have 4 numbers in a line sum to 34 (the average of te numbers 1 - 16).

There's two ways to play:

1. The computer against a human player, with the player choosing to go first or second.

2. The computer plays itself, talking alternating moves, allowing a human to watch by pressing a key to continue for each successive move.

### Implementation
This implementation uses iterative deepening search and alpha-beta pruning. The algorithm searches down the tree to a specified depth and an evaluation function is used to evaluate all board states at that depth. Alpha-beta pruning is used to trim branches as these values are propagated back up to the root node. 

The search algorithm starts at depth 0 and repeats the algorithm at increasing depths. After two seconds have been reached an exception is thrown and the best move from the last full depth search is used.

### The evaluation function
The evaluation function splits the board into 10 vectors: 4 row, 4 column and 2 diagonal vectors. Then, it calculates
how many even and odd values are in each vector. It also calculates whose turn it is to move. If the number of even
values is equal to the number of odd values on the board then it is MAXes turn to go. Vectors that are favorable to MAX
increase the score and vectors that are unfavorable decrease the score. For example, if it is maxes turn to go, then a vector
with 2 even and 1 odd is favorable because there is a chance MAX can add an odd to that vector that will sum to 34. 
See search.py for full implementation details.

The evaluation function does not check whether or not the vectors on the board could be winning vectors when 
combined with values that have not been placed because some experiments with this approach proved too computationally 
expensive and notably decreased the search depth. However, this idea could still be worth exploring.
 
There is an interesting paper included in the doc directory that discusses other possible strategies for a 
better evaluation function.



### References

***Artificial Intelligence: A Modern Approach* (AIMA)** (3rd Edition) by Stuart J. Russel and Peter Norvig

Section 5.2 Optimal Decisions in Games

https://github.com/aimacode/aima-python/blob/master/games.py
