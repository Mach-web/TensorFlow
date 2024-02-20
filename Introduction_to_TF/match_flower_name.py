# Write your code
f=open('flowers.txt', 'r')
file_data=f.readlines()
f.close()
# HINT: create a dictionary from flowers.txt
flower = {}
for flwr in file_data:
    flower_full_name = flwr.split(":")[1].strip()
    flower[flwr.split(":")[0]] = flower_full_name
# HINT: create a function to ask for user's first and last name
name = input("Enter your First [space] Last name only: ")
first_letter = name[0].upper()
# print the desired output
print("Unique flower name with the first letter: {}".format(flower[first_letter]))



