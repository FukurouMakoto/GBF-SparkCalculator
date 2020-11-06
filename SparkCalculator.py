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
def sparkCalculator(total): 
	return f"You can make a total of {str(int(totalDraws(crystals, tix, tenrolls)))} draws."

print('Welcome to Spark Calculator')
crystals = input('How many crystals do you have? ')
tix = input('How many single roll tickets do you have? ')
tenrolls = input('Finally, how many 10 roll tickets do you have? ')
total = totalDraws(crystals, tix, tenrolls)
print(sparkCalculator(total))
print(how_many_rolls(total))





