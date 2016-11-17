
def largest_num(n, div):

	if div == 0:
		return "enter a positive interger"

	else:
		number = int("9" * n)
		while number % div != 0:
			number -= 1

		return number