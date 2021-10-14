from shirt import Shirt

shirt_one = Shirt('red', 'M', 'long_sleeved', 45)
shirt_two = Shirt('orange', 'S', 'short_sleeved', 30)

print(shirt_one.price)
print(shirt_one.color)

#Uses a method to change the new_price
#it gives more flexibility to implementing changes

shirt_two.change_price(45)
print(shirt_two.price)

#updating attributes directly. This is not encouraged
#Accessing attributes directly would be frowned upon in many other languages, but not in Python
shirt_one.color = 'yellow'
shirt_one.size = 'L'
shirt_one.price = 43
