import random
print("Choose any of one from \n rock \n paper \n scissors")
player1=input("player1:")
rand_num= random.randint(0,2)
if rand_num==0:
	player2="rock"
elif rand_num==1:
	player2="paper"
else:
	player2="scissors"
print("player2:" + player2)		



if player1=="rock" and player2 == "scissors":
	print("player1 wins!!")
elif player1=="rock" and player2 == "paper":
	print("player2 wins!!")
elif player1=="scissors" and player2=="paper":
	print("player1 wins!!")
elif player1=="scissors" and player2=="rock":
	print("player2 wins!!")
elif player1=="paper" and player2=="rock":
    print("player1 wins")
elif player1=="paper" and player2=="scissors":
	print("player2 wins")
elif player1 == player2:
	print("Match tie!")
