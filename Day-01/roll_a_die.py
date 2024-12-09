import random

def roll_die(num_rolls):
    counts = [0] * 6  # List to store counts for numbers 1 to 6

    for _ in range(num_rolls):
        roll = random.randint(1, 6)  # Simulate rolling a die
        counts[roll - 1] += 1  # Increment the count for the rolled number

    probabilities = [count / num_rolls for count in counts]  # Calculate probabilities

    return probabilities

# Number of times to roll the die
num_rolls = 1000

probabilities = roll_die(num_rolls)

for i, prob in enumerate(probabilities, start=1):
    print(f"Probability of rolling {i}: {prob}")