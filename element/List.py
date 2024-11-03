# Generates a list of squares of even numbers between 1 and 10
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares)
