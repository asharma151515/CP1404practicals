import random

NUM_QUICK_PICKS = 5
MIN_NUM = 1
MAX_NUM = 45
NUM_PER_QUICK_PICK = 6

# Function to generate a single quick pick
def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUM, MAX_NUM + 1), NUM_PER_QUICK_PICK))

# Ask the user how many quick picks they wish to generate
num_quick_picks = int(input("How many quick picks? "))

# Generate and display the quick picks
for _ in range(num_quick_picks):
    quick_pick = generate_quick_pick()
    print(" ".join(f"{num:2d}" for num in quick_pick))


