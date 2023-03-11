name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
height_converted = round(height * 2.54)
weight = 180 #lbs
weight_converted = round(weight * 0.4535924)
eyes = 'Blue'
teeth = 'white'
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall or {height_converted} centimeters tall.")
print(f"He's {weight} pounds heavy or {weight_converted} kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")