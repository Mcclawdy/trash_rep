number = input()
even = 0
odd = 0
for num in range(0, len(number)):
    if int(num) == 0 or int(num) % 2 == 0:
        even += int(number[num])
    else:
        odd += int(number[num])
print(even - odd)