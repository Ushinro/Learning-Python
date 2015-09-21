name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 # Inches
metric_height = height * 2.540 # cm
weight = 180 # lbs
metric_weight = weight / 2.205 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)

print("He's %d inches tall or %r centimeters." % (height, metric_height))
print("He's %d pounds heavy or %r kilograms." % (weight, metric_weight))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# This line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight))