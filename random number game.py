import random
num1 = random.randint(0,11)
num2 = random.randint(0,51)
num3 = random.randint(0,101)

print("1 -- easy level")
print("2 -- medium level")
print("3 -- hard level")
print("\n")

choice=int(input("entre your choice -->"))

while True:
	if choice==1:
		num=int(input("entre a number between 1 & 10 -->"))
		if num<num1:
			print("too low")
			
		elif num>num1:
			print("too high")
			
		elif num==num1:
			print("you win")
			break
			
	elif choice==2:
		num=int(input("entre a number between 1 & 50 -->"))
		if num<num2:
			print("too low")
			
		elif num>num2:
			print("too high")
			
		elif num==num2:
			print("you win")
			break
			
	elif choice ==3:
		num=int(input("entre a number between 1 & 100 -->"))
		if num<num3:
			print("too low")
			
		elif num>num3:
			print("too high")
			
		elif num==num3:
			print("you win")
			break
	