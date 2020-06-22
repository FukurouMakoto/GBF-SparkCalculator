def sparkCalculator(crystals, tix, tenrolls):
	totalDraws = ((int(tix)*300) + (int(tenrolls)*3000) + int(crystals)) / 300
	print(f"You can make a total of {str(int(totalDraws))} draws.")
	if totalDraws == 300: 
		print('You can spark a character!')
	elif totalDraws > 300: 
		leftover = totalDraws - 300
		print(f'You can spark a character and have {str(int(leftover))} draws leftover to draw for whoever you want!')
	elif totalDraws < 300:
		untilCanSpark = 300 - int(totalDraws) 
		print('Sorry, you do not have enough to spark.')
		print(f'{str(int(untilCanSpark))} draws needed until you can spark a character.')





print('Welcome to Spark Calculator')
crystals = input('How many crystals do you have? ')
tix = input('How many single roll tickets do you have? ')
tenrolls = input('Finally, how many 10 roll tickets do you have? ')
sparkCalculator(crystals, tix, tenrolls)