# given a non-empty list of integers, every element appears twice except for one. find the one

list = ['1', '1', '2', '2', '3', '4', '4', '5', '5', '6', '6', '7', '7']

data = {}

for item in list:
    if item not in data:
        data[item] = 1
    else:
        data[item] += 1

def unique(value = 1):
    for k, v in data.items():
        if v == value:
            return k

print(unique())
