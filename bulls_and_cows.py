from random import randint
unique=[]
random = [randint(0,9) for p in range(0,4)]
print random
bull=0
print "bull = ",bull
cow=0
print "cow = ",cow
print "Computer has generated a random number between 0000-9999."
guess = -1
while (guess != random):
	guess = raw_input("Can you make a guess ?")
	isdigi = guess.isdigit()
	if (isdigi and (int(guess)>=0 and int(guess)<=9999) and len(guess)<=4):
		guess=guess.zfill(4)
		guess = map(int,guess)
		if(guess == random):
			print "WOW HO HO. You are awesome."
			bull=4
		else:
			print "OOPS!!You aren't lucky. Try again"
			for i,(j,k) in enumerate(zip(guess,random)):
				if(j == k):
					bull=bull+1
					unique.append(i)
				else:
					for l,m in enumerate(random):
						if (l not in unique and j==m and m!=guess[l]):
							cow=cow+1
							unique.append(l)
							break

		print "bull = ",bull
		print "cow = ",cow
		bull=0
		cow=0
		unique=[]
	else:
		print "tiger"
