#RPS.py
#Name: Eduardo Esau Hernandez Abreo
#Date: 02/05/2025
#Assignment: lab 3 
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  player = input("Enter choise (R/P/S): ")

  computer = random.choice( ["R", "P", "S"] )

  if player == "R" and computer == "R":
    print("You tie")
    ties = ties + 1
  elif player == "R" and computer == "P":
    print("You Losses")
    losses = losses + 1 
  elif player == "R" and computer == "S":
    print("You Win")
    wins = wins + 1
  else:
    print("That is Invalid Choise")
    print("try again")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
