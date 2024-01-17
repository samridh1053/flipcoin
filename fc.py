import random
num_flips = 1000
doublet_dict = {'HH': 0, 'HT': 0, 'TH': 0, 'TT': 0}
for _ in range(num_flips):
    result1 = random.choice(['H', 'T'])
    result2 = random.choice(['H', 'T'])
    doublet_combination = result1 + result2
    doublet_dict[doublet_combination] += 1
percentage_HH = (doublet_dict['HH'] / num_flips) * 100
percentage_HT = (doublet_dict['HT'] / num_flips) * 100
percentage_TH = (doublet_dict['TH'] / num_flips) * 100
percentage_TT = (doublet_dict['TT'] / num_flips) * 100
print(f'HH: {percentage_HH:.2f}%')
print(f'HT: {percentage_HT:.2f}%')
print(f'TH: {percentage_TH:.2f}%')
print(f'TT: {percentage_TT:.2f}%')
