from random import randint

def bozosort (items):
 	while not sorted(items) == items:
 		switch(items)
 	return items

def switch(items):
 	num1 = randint(0, len(items) - 1)
 	num2 = randint(0, len(items) - 1)
 	items[num1], items[num2] = items[num2], items[num1]
 	return items

items = [2,1,2,5]
print bozosort(items)