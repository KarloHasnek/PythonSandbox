from random import randint
print("Dice roll simulator")
n = int(input("Number of rolls: "))
num_1, num_2, num_3, num_4, num_5, num_6 = 0, 0, 0, 0, 0, 0
for i in range(n):
    throw = randint(1, 6)
    if throw == 1:
        num_1 += 1
    elif throw == 2:
        num_2 += 1
    elif throw == 3:
        num_3 += 1
    elif throw == 4:
        num_4 += 1
    elif throw == 5:
        num_5 += 1
    else:
        num_6 += 1

avg_1 = round((num_1 / n)*100, 2)
avg_2 = round((num_2 / n)*100, 2)
avg_3 = round((num_3 / n)*100, 2)
avg_4 = round((num_4 / n)*100, 2)
avg_5 = round((num_5 / n)*100, 2)
avg_6 = round((num_6 / n)*100, 2)
print(f'After rolling a dice {n} times...')
print("------------------------------------------------------------------------------")
print(f'Number 1 showed up {num_1} times or shown in percentage: {avg_1}%')
print(f'Number 2 showed up {num_2} times or shown in percentage: {avg_2}%')
print(f'Number 3 showed up {num_3} times or shown in percentage: {avg_3}%')
print(f'Number 4 showed up {num_4} times or shown in percentage: {avg_4}%')
print(f'Number 5 showed up {num_5} times or shown in percentage: {avg_5}%')
print(f'Number 6 showed up {num_6} times or shown in percentage: {avg_6}%')
