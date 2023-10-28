class Shirt:
    # Define the class methods
    # Instantiate class attributes in __init__ method
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    # Create a method to enable a user to change shirt price
    def change_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price

    # Create a method to calculate discount according to discount rate given
    def discount(self, discount):
        return self.price * discount
# Initialize 3 shirt objects
shirt_one = Shirt("red", "S", "short sleeve", 15)
shirt_two = Shirt("orange", "M", "short sleeve", 25)
shirt_three = Shirt("Purple", "XL", "short sleeve", 10)
shirt_four = shirt_one
print(shirt_one)
print(shirt_four)
shirt_one_price = shirt_four.price
# Use change_price method to change price of shirt_one
shirt_one.change_price(5)
print("The new price of shirt one is: {}".format(shirt_one.get_price()))
# Check to see if attribute references changes once its value is changed
print(shirt_one_price)

# Calculate the combined discounts using the rates given
print(f"The total discount is: {shirt_one.discount(.14)+shirt_two.discount(.06)+shirt_three.discount(.05)+shirt_four.discount(.10)}")

# print shirt attributes
shirts = [shirt_one, shirt_two, shirt_three, shirt_four]
for _ in shirts:
    print(f"Color: {_.color}\t size: {_.size}\t style: {_.style}\t Price after discount at 10%: {_.get_price() - (_.discount(.10))}")




