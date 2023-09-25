from org.transcrypt.stubs.browser import *
import random

# 原始代码：https://github.com/Data-Driven-World/d2w_mini_projects/blob/master/mp_sort/app/static/library.py
# 运行过程：
# cd mp_sort 
# python -m pipenv shell
# cd app/static
# python -m transcrypt -b -n library
# cd ..
# cd ..
# flask run 

def gen_random_int(number, seed):
	result = list(range(number))
	random.seed(seed)
	random.shuffle(result)
	return result

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	# pass

	array = gen_random_int(number,seed)
	# convert the items into one single string
	# the number should be separated by a comma
	# and a full stop should end the string.
	# pass

	array_str = ', '.join(map(str, array))
	# array_str = 1

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

# @app.route('/generate', methods=['POST'])
# def generate():
#     number = 10
#     seed = 200
#     array = gen_random_int(number, seed)
#     array_str = ', '.join(map(str, array))
#     return jsonify({'generated_array': array_str})

def bubble_sort(arr):
	n = len(arr)
	for i in range(n-1):
		swapped = False
		for j in range(n-i-1): #last elements already in place
			if(arr[j]>arr[j+1]):
				arr[j],arr[j+1]=arr[j+1],arr[j]
				swapped = True
		if(swapped==False):
			break

def insertion_sort(arr):
	# i 2 j 1 
	# arr[1] 5 arr[2] 4,arr[3] 3 key
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# array_str = None
	# document.getElementById("sorted").innerHTML = array_str

	generatedNumbers = document.getElementById("generate").textContent
	generatedArray = generatedNumbers.split(', ').map(Number)
	bubble_sort(generatedArray)
	sorted_array_str = ', '.join(map(str, generatedArray))
	document.getElementById("sorted").innerHTML = sorted_array_str
	

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	# value = document.getElementsByName("numbers")[0].value
	value = document.getElementById("numbers").value

	# # Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# # Your code should start from here
	# # store the final string to the variable array_str
	# # pass
	inputString = document.getElementById("numbers").value
	generatedArray = inputString.replace(" ","").split(',').map(float)
	bubble_sort(generatedArray)
	array_str = ', '.join(map(str, generatedArray))+ '.'

	# document.getElementById("sorted").innerHTML = array_str
	document.getElementById("sorted").innerHTML = array_str


