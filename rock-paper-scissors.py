gameList = ["rock","scissors","paper"]
scores = {"player_1":0,"player_2":0}


while True:
  player_1_choise = input("Your choise player 1: ").lower().strip()
  player_2_choise = input("Your choise player 2: ").lower().strip()
  if (player_1_choise or player_2_choise) not in gameList:
    print("Invalid input,please try again!")
    choise = input("Do you want to play again?(Yes/NO): ").lower()
    if choise != "yes":
      break
    else:
      continue
  if player_1_choise==player_2_choise:
    scores["player_1"]+= 0
    scores["player_2"]+=0
    print("It's a tie!")
  elif player_1_choise=="rock" and player_2_choise=="paper":
    scores["player_2"]+=1
    print("Player 2 wins!") 
  elif player_1_choise=="paper" and player_2_choise=="rock":
    scores["player_1"]+=1
    print("Player 1 wins!") 
  elif player_1_choise=="rock" and player_2_choise=="scissors":
    scores["player_1"]+=1
    print("Player 1 wins!") 
  elif player_1_choise=="scissors" and player_2_choise=="rock":
    scores["player_2"]+=1
    print("Player 2 wins!") 
  elif player_1_choise=="paper" and player_2_choise=="scissors":
    scores["player_2"]+=1
    print("Player 2 wins!")          
  else: 
    scores["player_1"]+=1
    print("Player 1 wins!") 
  choise = input("Do you want to play again?(Yes/NO): ").lower()
  if choise != "yes":
    break
print("The score for player 1 is: ",scores["player_1"])
print("The score for player 2 is: ",scores["player_2"])




 

