def totalDraws(crystals, tix, tenrolls):
	totalDraws = ((int(tix)*300) + (int(tenrolls)*3000) + int(crystals)) / 300
	return totalDraws

def how_many_rolls(total):
	if total == 300:
		return "You can spark a character!"
	elif total > 300: 
		leftover = total - 300
		return f"You can spark a character and have {str(int(leftover))} draws leftover to draw for whomever you want!"
	elif total < 300:
		untilCanSpark = 300 - int(total)
		return f"Sorry, you need {str(int(untilCanSpark))} draws until you can spark a character..."	

def sparkCalculator(crystals, tix, tenrolls): 
	return f"You can make a total of {str(int(totalDraws(crystals, tix, tenrolls)))} draws."

def test_for_negative(num):
	if num < 0:
		return True
	else: 
		return False
def main():
	print('Welcome to Spark Calculator')
	crystals = input('How many crystals do you have? ')
	tix = input('How many single roll tickets do you have? ')
	tenrolls = input('Finally, how many 10 roll tickets do you have? ')
	for item in [crystals, tix, tenrolls]:
		if test_for_negative(int(item)):
			print("Invalid input. Please don't use negative numbers.")
			main()
	total = totalDraws(crystals, tix, tenrolls)
	print(sparkCalculator(crystals, tix, tenrolls))
	print(how_many_rolls(total))

if __name__ == "__main__":
	main()

