import pygal
from die import Die


# Create a D6

# Create two D6 dice.

die_1 = Die()
die_2 = Die()

# Make some rolls, and store result
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyse the results.

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')

# print(frequencies)