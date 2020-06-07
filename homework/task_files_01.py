n = int(input())
p = int(input())


share = ''
power = ''
with open ("data.txt") as data:
    data = data.readline()
    data = data.split(' ')
    for i in data:
        if int(i) % n  == 0:
            share += f'{i} '
        power += f'{int(i) ** p} '
with open ("out-1.txt", "a") as out1:
    out1.writelines(share.strip())

with open ("out-2.txt", "a") as out2:
    out2.writelines(power.strip())
