from random import randint
def randlist(r):
	alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	c = alpha[r]
	return c 
	
def main():
	count = 0
	checklist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	while True: 
		r = randint(0,25)
		print(checklist)
		checklist[r] = 1
		c = randlist(r)
		print(c, end="")
		if (count == 26):
			 break
		count = count + 1
	print()
if __name__=='__main__':
	main()
