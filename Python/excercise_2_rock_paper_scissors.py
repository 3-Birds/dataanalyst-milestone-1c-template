# Write a Python function that return the player who wins in rock, paper, scissors game.
# The functions receives two attributes. Firs is choice of Player1, second is choice of Player 2.
# The possible inputs can be rock, paper and scissors. The game does not accept anything else. The scissors wins against paper,
# paper wins against rock, the rock wins against scissors.
# If the value of player1 is stronger than value of player2, return "Player 1 won!", if Player 2 is stronger, return "Player 2 won!", 
# if the two input is same, write "Draw!".
# If one of input is not one of rock, paper or scissors, return "Wrong input!"


# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"
# "paper", "x" --> "Wrong input!"


def rps(player1:str, player2:str) -> str:
    pass