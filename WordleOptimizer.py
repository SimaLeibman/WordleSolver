import numpy as np

def best_guess(candidates, allowed_guesses):
    """
    Return the allowed guess with minimum expected partition size
    equivalent to max entropy split.
    """

    best_g = None
    best_score = float("inf")

    cand_arr = np.array(candidates)

    for g in allowed_guesses:

        # hashmap pattern -> count
        counts = {}

        for s in candidates:
            pat = compare(g, s)
            counts[pat] = counts.get(pat, 0) + 1

        # compute expected size metric
        # sum (n/N)^2  (closely tied to entropy)
        N = len(candidates)
        probs = np.array(list(counts.values())) / N
        score = np.sum(probs * probs)

        if score < best_score:
            best_score = score
            best_g = g

    return best_g, best_score