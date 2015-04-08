import bozosort
import random
import timer

MILLISECONDS = 1000

def generate_rand_num (num):
	num_list = []
	for i in range(num):
		num_list.append(random.random() * random.random())
	return num_list

def run_trials():
	trials = []
	num_trials = 100

	print 'loading.....'
	for i in range(num_trials):
		starting_list = generate_rand_num(5)
		with timer.Timer() as t:
		    bozosort.bozosort(starting_list)
		    if (len(starting_list) >= 8) and (i == num_trials // 2):
		    	print '		Halfway done!'
		    else:
		    	print '.....'
		runtime = t.secs * MILLISECONDS
		trials.append(runtime)

	print (sum(trials)/num_trials)

run_trials()