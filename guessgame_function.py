with open('test.txt',mode= 'w+') as gamefile:

	gamefile.seek(0)
	curr_highscore = float(gamefile.read())
cup = ['','o','',]
token = 0
from random import shuffle 


def guess_func():
	guess = ''
	while guess not in ['0','1','2']:
		guess = input("pick a number : 0,1, or 2 \n")
	return int(guess)
def cuproll(cup, index):
	shuffle(cup)
	print(f"\n correct order is {cup}")
	if cup[index]== 'o':
		print("YOU WON\n ")
		token = 1
	else:
		print('YOU LOST \n')
		token = 0
	return token

go_on=1

loop = 'y'
tot_chance = 0
tot_points = 0
while loop == 'y':
	tot_chance+=1
	#shuffle(cup)
	token1 = cuproll(cup,guess_func())
	if token1 ==1:
		tot_points+=1
	elif token1 == 0:
		pass
	loop = 'z'
	while loop not in ['y','y','n','N']:
		loop =input("do you want to continue : y or n \n")
		shuffle(cup)
	
score = (tot_points/tot_chance)*100		
if curr_highscore < score:

	gamefile.write(str(score))
else :
	pass
print(f'TOTAL POINT {tot_points}\n TOTAL CHANCE {tot_chance}\n SCORE {score:1.3f}')
gamefile.close()