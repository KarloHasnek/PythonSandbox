from random import randint
print("Heads/Tails probability")
n = int(input("Number of throws: "))
heads_br = 0
tails_br = 0
for i in range(n):
    throw = randint(0, 1)
    if throw == 0:
        heads_br += 1
    else:
        tails_br += 1
p_h = (heads_br / n)*100
p_t = (tails_br / n)*100
print(f'After flipping coin for {n} times...')
print("------------------------------------------------------------------------------")
print(f'Number of times \'Heads\' appeared: {heads_br} or shown as percentage: {p_h}%')
print(f'Number of times \'Tails\' appeared: {tails_br} or shown as percentage: {p_t}%')
