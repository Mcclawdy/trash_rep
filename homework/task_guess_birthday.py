date = int(input())
month = 0
result = 0
for i in range(1, 13):
    if (date - i) % 50 == 0:
        month += i
        result += (((date - i) // 50) -  5) // 2

print(f'{result} {month}')
        
