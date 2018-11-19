
PlayerA=input("First player, please select rock, paper, or scissors")
while (PlayerA != "rock") and (PlayerA != "paper") and (PlayerA != "scissors"):
    print(PlayerA)
    PlayerA = input("First player, please select rock, paper or scissors")


PlayerB=input("Second player, please select rock, paper, or scissors")
while (PlayerB != "rock") and (PlayerB != "paper") and (PlayerB != "scissors"):
    print(PlayerB)
    PlayerB = input("Second player, please select rock, paper or scissors")

if PlayerA == "paper":
    if PlayerB == "rock":
        print("Player A Wins")
    if PlayerB =="scissors":
        print("Player B Wins")
    if PlayerB =="paper":
        print("Tie, play again")

if PlayerA == "scissors":
    if PlayerB == "paper":
        print("Player A Wins")
    if PlayerB =="rock":
        print("Player B Wins")
    if PlayerB == "scissors":
        print("Tie, play again")

if PlayerA == "rock":
    if PlayerB == "scissors":
        print("Player A Wins")
    if PlayerB =="paper":
        print("Player B Wins")
    if PlayerB =="rock":
        print("Tie, play again")