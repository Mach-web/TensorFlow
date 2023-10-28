## demo.py

import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)

import math
print(f"The factorial of 7 is: {math.factorial(7)}")
result = math.exp(3)
print("The exponent of 3 is: {}".format(result))
