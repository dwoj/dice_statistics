from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

dice_1 = Dice()
dice_2 = Dice()

results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Fraquency'}
my_layout = Layout(title='Results of 1000 rolls of two six-sided dices',
    xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename = 'd6_d6.html')