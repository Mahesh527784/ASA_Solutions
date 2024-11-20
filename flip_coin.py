import random

def flip_coin(num_flips):
    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        if random.choice(['heads', 'tails']) == 'heads':
            heads_count += 1
        else:
            tails_count += 1

    heads_probability = heads_count / num_flips
    tails_probability = tails_count / num_flips

    return heads_probability, tails_probability

# Number of times to flip the coin
num_flips = 1000

heads_prob, tails_prob = flip_coin(num_flips)

print(f"Probability of heads: {heads_prob}")
print(f"Probability of tails: {tails_prob}")