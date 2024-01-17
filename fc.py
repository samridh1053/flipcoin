import random
num_flips = 1000
triplet_dict = {'HHH': 0, 'HHT': 0, 'HTH': 0, 'THH': 0, 'HTT': 0, 'THT': 0, 'TTH': 0, 'TTT': 0}
for _ in range(num_flips):
    result1 = random.choice(['H', 'T'])
    result2 = random.choice(['H', 'T'])
    result3 = random.choice(['H', 'T'])
    triplet_combination = result1 + result2 + result3
    triplet_dict[triplet_combination] += 1
percentage_HHH = (triplet_dict['HHH'] / num_flips) * 100
percentage_HHT = (triplet_dict['HHT'] / num_flips) * 100
percentage_HTH = (triplet_dict['HTH'] / num_flips) * 100
percentage_THH = (triplet_dict['THH'] / num_flips) * 100
percentage_HTT = (triplet_dict['HTT'] / num_flips) * 100
percentage_THT = (triplet_dict['THT'] / num_flips) * 100
percentage_TTH = (triplet_dict['TTH'] / num_flips) * 100
percentage_TTT = (triplet_dict['TTT'] / num_flips) * 100
print(f'HHH: {percentage_HHH:.2f}%')
print(f'HHT: {percentage_HHT:.2f}%')
print(f'HTH: {percentage_HTH:.2f}%')
print(f'THH: {percentage_THH:.2f}%')
print(f'HTT: {percentage_HTT:.2f}%')
print(f'THT: {percentage_THT:.2f}%')
print(f'TTH: {percentage_TTH:.2f}%')
print(f'TTT: {percentage_TTT:.2f}%')
