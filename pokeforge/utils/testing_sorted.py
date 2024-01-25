
names_to_be_sorted = ["one", "two", "Three", "four", 'five', "six"]

data_to_be_sorted = [0.1, 0.8, 0.5, 0.7, 1.0, 0.0]

all_to_be_sorted = list(zip(names_to_be_sorted, data_to_be_sorted))

sorthed = sorted(all_to_be_sorted, key=lambda x: abs(x[1] - 0.5))

top_x = [creature for creature, _ in sorthed[:3]]

print(top_x)