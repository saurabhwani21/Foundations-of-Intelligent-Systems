The file ttt.py performs regular Minimax version of Tic Tac Toe and the file ttyAB.py performs the Minimax Alpha-Beta version of Tic Tac Toe. 
Following are two outputs for each version of the games.
The player has to enter location of the spot where he wants to place his game piece.
The counter in the output states the number of states at that given time. 
The game continues until the user types "exit", else if the user hits enter after every game a new game will start. 
Message is displayed for the player whose turn it is to play.
If the user wins, "Human wins!" message is displayed.
If the AI wins, "AI wins!" message is displayed.









Minimax Tic Tac Toe :

Output 1:

Let's start!

 | | 
 | | 
 | | 
Enter the location.1

 |X| 
 | | 
 | | 
counter=  63904

O|X| 
 | | 
 | | 
Enter the location.7

O|X| 
 | | 
 |X| 

O|X| 
 | | 
 |X| 
counter=  64802

O|X| 
 |O| 
 |X| 
Enter the location.8

O|X| 
 |O| 
 |X|X

O|X| 
 |O| 
 |X|X
counter=  64844

O|X| 
 |O| 
O|X|X
Enter the location.3

O|X| 
X|O| 
O|X|X

O|X| 
X|O| 
O|X|X
counter=  64847

O|X|O
X|O| 
O|X|X
AI wins!
Type 'exit' to terminate or hit enter to continue.


_______________________________________________________

Output 2:

Let's start!

 | | 
 | | 
 | | 
Enter the location.0

X| | 
 | | 
 | | 
counter=  59704

X| | 
 |O| 
 | | 
Enter the location.8

X| | 
 |O| 
 | |X

X| | 
 |O| 
 | |X
counter=  60756

X|O| 
 |O| 
 | |X
Enter the location.7

X|O| 
 |O| 
 |X|X

X|O| 
 |O| 
 |X|X
counter=  60802

X|O| 
 |O| 
O|X|X
Enter the location.2

X|O|X
 |O| 
O|X|X

X|O|X
 |O| 
O|X|X
counter=  60806

X|O|X
 |O|O
O|X|X
Enter the location.3

X|O|X
X|O|O
O|X|X

X|O|X
X|O|O
O|X|X
Its a tie!
Type 'exit' to terminate or hit enter to continue.

_______________________________________________________

Minimax Tic Tac Toe (Alpha Beta):

Output 1:

Let's start!

 | | 
 | | 
 | | 
User's turn.
Enter the location.1

 |X| 
 | | 
 | | 
AI's turn.
counter=  1396

O|X| 
 | | 
 | | 
User's turn.
Enter the location.0
Try again.7

O|X| 
 | | 
 |X| 
AI's turn.

O|X| 
 | | 
 |X| 
counter=  1510

O|X| 
 |O| 
 |X| 
User's turn.
Enter the location.8

O|X| 
 |O| 
 |X|X
AI's turn.

O|X| 
 |O| 
 |X|X
counter=  1530

O|X| 
 |O| 
O|X|X
User's turn.
Enter the location.3

O|X| 
X|O| 
O|X|X
AI's turn.

O|X| 
X|O| 
O|X|X
counter=  1532

O|X|O
X|O| 
O|X|X
AI wins!
Type 'exit' to terminate or hit enter to continue.

_______________________________________________________

Output 2:


Let's start!

 | | 
 | | 
 | | 
User's turn.
Enter the location.2

 | |X
 | | 
 | | 
AI's turn.
counter=  1550

 | |X
 |O| 
 | | 
User's turn.
Enter the location.1

 |X|X
 |O| 
 | | 
AI's turn.

 |X|X
 |O| 
 | | 
counter=  1615

O|X|X
 |O| 
 | | 
User's turn.
Enter the location.8

O|X|X
 |O| 
 | |X
AI's turn.

O|X|X
 |O| 
 | |X
counter=  1629

O|X|X
 |O|O
 | |X
User's turn.
Enter the location.3

O|X|X
X|O|O
 | |X
AI's turn.

O|X|X
X|O|O
 | |X
counter=  1631

O|X|X
X|O|O
O| |X
User's turn.
Enter the location.7

O|X|X
X|O|O
O|X|X
AI's turn.

O|X|X
X|O|O
O|X|X
Its a tie!
Type 'exit' to terminate or hit enter to continue.
