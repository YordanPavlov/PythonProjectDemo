import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3456)
# Simulating a random walk 1000 times

all_walks = []
for x in range(1000):
    random_walk = [0]
    for y in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

    np_aw_t = np.transpose(np.array(all_walks))
    ends = np_aw_t[-1, :]
    plt.hist(ends)
    plt.show()
    # Probability of reaching the 60th step on the 100th throw
    print(np.mean(ends >= 60))
    # Alternative print(len(ends[ends >= 60]) / 1000)