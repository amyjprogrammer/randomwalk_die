import matplotlib.pyplot as plt

from die import Die

# Two dice
die_1 = Die()
die_2 = Die()


#storing results of rolls in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

plt.style.use('fivethirtyeight')

x = range(2, max_result+1)
y = frequencies

plt.bar(x, y)

plt.title('Results of rolling two D6 1000 times')
plt.xlabel("Result")
plt.ylabel('Frequency of Result')
plt.tight_layout()

plt.show()
