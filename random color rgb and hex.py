from random import *

def chex(c):
    if c <= 15:
        return '0' + hex(c)[2:]
    else:
        return hex(c)[2:]

r = randint(1, 255)
g = randint(1, 255)
b = randint(1, 255)

print(f'r = {r}, g = {g}, b = {b}')
print(f'hex = #{chex(r)}{chex(g)}{chex(b)}')
