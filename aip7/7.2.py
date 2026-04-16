list = [1,2,3,3,7,5,7,8]
count = {}
for item in list:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
for item in count:
    if count[item] > 1:
        print(f"Повторяющийся элемент: {item}")
