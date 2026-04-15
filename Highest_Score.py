# Using Range function
marks = [100, 200, 200, 200]
total = 0
for i in range(0 , len(marks)):
    total+=marks[i]
print(total)

# Using normal function
fix = [100, 200, 200, 200]
rate = 0
for element in fix:
    rate+=element
print(rate)

# Max from the list
big = [200, 500, 800, 100]
value = 0
for element in range(0, len(big)):
    if(value<= big[element]):
        value = big[element]
print(f"Max value is {value}")




