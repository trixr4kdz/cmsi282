from random import shuffle
import time

MILLISECONDS = 1000

start_time = time.time() * MILLISECONDS

def bozosort (items):
 	while not sorted(items) == items:
 		shuffle (items)
 	return items

starting_list = input("Enter a list: \n")
# starting_list = [100,2]
print (bozosort(starting_list))

end_time = time.time() * MILLISECONDS

def print_runtime():
	runtime = end_time - start_time
	if runtime > 1000:
		print(str(runtime / 1000) + " seconds")
	else:
		print(str(runtime) + " milliseconds")

print_runtime()