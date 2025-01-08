Array1 = [1, 2, 3]
Array2 = [-1, -3]
Array3 = [1, 2, 'merry merry', 4 , 5 , 'have a go']

import random
Array4 = []
while len(Array4) < 10:
	Array4.append(random.randint(-10, 10))

print(Array4)


def solution(check_array):
	integer = 1
	print("________________________________________")
	print("\n You are working with Arrary: ", check_array)
	### DataCheck verifies all data in list matching.
	for n in range(len(check_array)):
		if type(check_array[n]) == int:
			print("DataCheck", n ,": True")
			check_array[n] = int(check_array[n])
		else:
			print("DataCheck: False")
			print("Invalid list entry are defaulted to [0]")
			check_array[n] = 0
	
	print(check_array)
	
	### ListCheck verifies if integer in array
	if integer in check_array:
		while integer in check_array:
			print("\n Check: False")
			print("Integer in Array")
			integer += 1
		print(integer)
		return
	else:
		print("\n Check: True")
		print("Integer not in Array")
		print(integer)
		return
		


print("\n Test")		
solution(Array1)
solution(Array2)
solution(Array3)
solution(Array4)
						
		
