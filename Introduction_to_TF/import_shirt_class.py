# Access Shirt class in this program
from shirt_class import Shirt

# Instantiate two objects of class Shirt
shirt_one = Shirt('red', 'M', 'long sleeved', 45)
shirt_two = Shirt('orange', 'S', 'short sleeved', 30)

print(shirt_one.price)
print(shirt_one.color)
# Access method change_price from our program
shirt_two.change_price(45)
print(shirt_two.price)
shirt_one.size = 'L'
print(shirt_one.size)



