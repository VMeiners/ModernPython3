#ask for age
age = input("How old are you: ")
if age:
	age = int(age)
	#ages between 18 and 21 wear wristband
	if age >= 18 and age < 21:
		print("You can enter, but need a wristband!")
	#21 and over can drink, normal entry
	elif age >=21:
		print("You are good to enter and can drink!")
	#too young, sorry
	else: 
		print("Too young, wee one! No entry.")
else:
	print("Please enter an age!")