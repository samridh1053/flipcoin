import random
num_flips = int(input("Enter the no of flips: "))

singlet_dict = {'Heads': 0, 'Tails': 0}
for _ in range(num_flips):
    result = random.choice(['Heads', 'Tails'])
    singlet_dict[result] += 1
percentage_heads = (singlet_dict['Heads'] / num_flips) * 100
percentage_tails = (singlet_dict['Tails'] / num_flips) * 100

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

sorted_singlet = sorted(singlet_dict.items(), key=lambda x: x[1], reverse=True)
sorted_doublet = sorted(doublet_dict.items(), key=lambda x: x[1], reverse=True)
sorted_triplet = sorted(triplet_dict.items(), key=lambda x: x[1], reverse=True)

print("Singlet Combinations:")
for item in sorted_singlet:
    print(f"{item[0]}: {item[1]:.2f}%")

print("\nDoublet Combinations:")
for item in sorted_doublet:
    print(f"{item[0]}: {item[1]:.2f}%")

print("\nTriplet Combinations:")
for item in sorted_triplet:
    print(f"{item[0]}: {item[1]:.2f}%")

winning_combination = max(sorted_singlet, key=lambda x: x[1])[0]
print(f"\nThe winning combination is: {winning_combination}")
