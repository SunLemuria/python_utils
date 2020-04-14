# generate random numbers in python
import random

# a random float number in [0, 1]
a = random.random()
# a random float number in a given range [10, 20]
b = random.uniform(10, 20)
# a random integer in a given range [10, 20],in fact it returns "random.randrange(10, 21)"
c = random.randint(10, 20)  # step is not modifiable
# a random integer in a given range [10, 20], not including the stop number
d = random.randrange(10, 20, step=1)

ll = [5, 'hello', 9, 'xit', 3, "Python"]
# randomly choose an element
e = random.choice(ll)
# shuffle ll
random.shuffle(ll)
# sample 3 elements from ll, return a list of sampled elements
random.sample(ll, 3)
