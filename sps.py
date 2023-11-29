import random
print("0.stone")
print("1.paper")
print("2.scissor")
user_num=int(input("enter the value:"))
computer_num=random.randint(0,2)
print("computer number is:",computer_num)
if(user_num<4):
	if(user_num==computer_num):
		print("draw the game")
	elif(user_num==2 and computer_num==0):
		print("computer won the match")
	elif(user_num==0 and computer_num==2):
		print("user won the match")
	elif(user_num>computer_num):
		print("user won the match")
	elif(user_num<computer_num):
		print("computer won the match")
	
	else:
		print("both are not matched")

else:
	print("invalid the user_num")
	
				
	
		

