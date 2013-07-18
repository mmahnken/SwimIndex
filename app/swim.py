import random
from decimal import Decimal
from random import choice


def choose_yardage(lower_bound, upper_bound):
	# Return a number between two inputs rounded to nearest 100.
	y = random.randint(lower_bound, upper_bound)
	return round(y, -2)

def weighted_yardage(num_sets):
	num_sets = Decimal(num_sets)
	multipliers = []
	check = random.random()
	y = None
	while y == None:
		if check > 0.1 and check < 0.8:
			y = check
		else:
			check = random.random()
	set1 = round(y, 1)
	multipliers.append(set1)
	remaining = 1.0 - set1
	y = Decimal(remaining)/Decimal(Decimal(num_sets)-1)
	set_mult = round(y, 1)
	for i in range(num_sets-1):
		multipliers.append(set_mult)
	return multipliers



def set_maker(total_yardage, num_sets):
	if total_yardage <= 1100:
		warmup = choose_yardage(100, 300)
		cooldown = choose_yardage(100, 300)
		print warmup
		print cooldown
	else:
		warmup = choose_yardage(200, 500)
		print warmup
		cooldown = choose_yardage(200, 600)
		print cooldown
	main_set = Decimal(total_yardage) - (Decimal(warmup) + Decimal(cooldown))
	random_decimal_list = weighted_yardage(num_sets)
	print random_decimal_list
	sets = []
	goal = main_set
	for decimal in random_decimal_list:
		this_set = Decimal(decimal) * Decimal(main_set)
		this_set = Decimal(this_set)
		this_set = round(this_set, -2)
		sets.append(this_set)
		main_set = Decimal(main_set) - Decimal(this_set)
	x = 0
	for s in sets:
		x += s
	if goal != x:
		to_add = Decimal(goal) - Decimal(x)
		short_set = min(sets)
		index = sets.index(short_set)
		new_set = Decimal(short_set) + Decimal(to_add)
		sets[index] = new_set
	main = []
	warmcool = []
	warmcool.append(warmup)
	warmcool.append(cooldown)
	for s in sets:
		main.append(s)
	workout = [main, warmcool]
	return workout

def make_set(num, yards):
	easy = 0
	if num % yards == 0:
		quant = num/yards
		print quant
		# set_made = str(quant) + " X " + str(yards)
		set_made = [quant, yards, easy] 
		return set_made
	if num % yards != 0:
		if num % 2 != 0:
			easy += 100
			quant = (num-100)/yards
			print quant
		else:
			easy1 = num%yards
			easy += easy1
			quant = num / (yards - easy1)	
			print quant
		easy += num % yards 
		#set_made = str(quant) + " X " + str(yards) + ", " + str(easy) + " recovery"
		set_made = [quant, yards, easy] 
		return set_made 

def workout_sets(list_of_sets):
	set_types = [25, 50, 75, 100, 200, 300]
	workout_sets = []
	for s in list_of_sets:
		set_type = None
		while set_type is None:
			yards = choice(set_types)
			if yards <= s:
				set_type = yards
			else: 
				set_type = None
		set_made = make_set(s, set_type)
		workout_sets.append(set_made)
	return workout_sets

#def convert_workout(list, old_total, new_total):
	 













