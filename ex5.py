my_name = 'Gede P. W. Rajeg'
my_age = 31
my_height = 170 # cm
my_weight = 65 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cm tall.")
print(f"He's {my_weight} kg heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# Study drills 2
# Convert cm and kg to respectively inches and pounds
my_height_inch = my_height * 0.393701
my_height_inch = round(my_height_inch, 2)
my_weight_pound = my_weight * 2.20462
my_weight_pound = round(my_weight_pound, 2)

print(f"Let's talk about {my_name}.")
print(f"He's {my_height_inch} inches tall.")
print(f"He's {my_weight_pound} pounds heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
