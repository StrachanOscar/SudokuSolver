# A Sudoku Solver

### A program written in Python that solves a Sudoku using a backtracking algorithm. 

The program was written in Python because of its convenience but I'll convert it to C++ in the near future. Understanding the recursive nature of the 
backtracking algorithm was a challenge but ultimately rewarding. The helper functions were simple to implement. 

**Future iterations:**
1. Implement a function that produces a randomized and valid Sudoku game for the user. This would most likely involve randomly generating a fully complete game and then removing cells. The algorithm should be able to solve all generated games. 
2. Implement a difficulty feature whereby users can specify the level of difficulty they would like in their game. Difficulty would be directly proportional to the starting number of empty cells.
3. Develop a GUI for the program. Users should be able to create their own game or generate a random one with a specified difficulty. The game should be solved for the user when they hit a particular key.
4. Implement a scoring feature and timer. Points added for correct moves and deducted for incorrect ones. Final score is multiplied in relation to their final time (shorter times equal a higher multiplier, etc).
5. Further develop the GUI with added responsiveness and visual appeal. E.g. a skippable animation for the solving algorithm.
