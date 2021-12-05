import random
print(random.random())
print(random.randint(1,12))
l = [1,2,3,4,5,6,7]
random.shuffle(l)
print(l)

print(random.choice(l))
print(random.choices(l))
