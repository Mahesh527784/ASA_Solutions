import random

def draw_card(num_draws):
    # A standard deck has 4 aces
    ace_count = 0
    deck_size = 52

    for _ in range(num_draws):
        # Simulate drawing a card
        card = random.randint(1, deck_size)
        # Assume cards 1, 14, 27, 40 are Aces
        if card in [1, 14, 27, 40]:
            ace_count += 1

    ace_probability = ace_count / num_draws
    return ace_probability

# Number of times to draw a card
num_draws = 1000

ace_prob = draw_card(num_draws)

print(f"Probability of drawing an Ace: {ace_prob}")