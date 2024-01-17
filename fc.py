import random
num_flips = 1000
singlet_dict = {'Heads': 0, 'Tails': 0}
for _ in range(num_flips):
    result = random.choice(['Heads', 'Tails'])
    singlet_dict[result] += 1
percentage_heads = (singlet_dict['Heads'] / num_flips) * 100
percentage_tails = (singlet_dict['Tails'] / num_flips) * 100
print(f'Heads: {percentage_heads:.2f}%')
print(f'Tails: {percentage_tails:.2f}%')
